import argparse
import sqlite3
import os.path

from bcalc.pensja import Pensja
from bcalc.config import Config

def connect(db):
    if not os.path.exists(db):
        print('Baza {} nie istnieje. Nastąpi jej utworzenie'.format(db))

        conn = sqlite3.connect(db)

        c = conn.cursor()

        c.execute('''CREATE TABLE wyplaty (data TEXT PRIMARY KEY, brutto REAL, netto REAL,
                    premia REAL, wynagrodzenie_urlopowe REAL, wynagrodzenie_chorobowe REAL, dni_urlopu INTEGER, nadgodzin REAL)''')

        c.execute('''CREATE TABLE wyplaty_calc (data TEXT PRIMARY KEY, netto REAL)''')

        c.execute('''CREATE VIEW v_wyplaty AS
                    SELECT data,
                        round(ifnull(brutto, 0)
                            + ifnull(premia, 0)
                            + ifnull(wynagrodzenie_urlopowe, 0)
                            + ifnull(wynagrodzenie_chorobowe, 0), 2) brutto,
                        ifnull(wynagrodzenie_chorobowe, 0) wynagrodzenie_chorobowe,
                        ifnull(dni_urlopu, 0) dni_urlopu,
                        ifnull(nadgodzin, 0) nadgodzin
                    FROM wyplaty;''')

        c.execute('''CREATE VIEW v_diff AS
                    SELECT w.data, w.brutto, w.netto, c.netto calc_netto, round(w.netto - c.netto, 1) diff
                    FROM wyplaty w
                    LEFT OUTER JOIN wyplaty_calc c ON w.data = c.data''')

    return sqlite3.connect(db)

def pensja(path, config, force):
    db = connect(path)

    try:
        c = db.cursor()

        if force:
            c.execute('delete from wyplaty_calc')

        inserted = 0

        for row in c.execute('''select data, brutto
                                    from v_wyplaty w1
                                    where
                                        not exists (select 1 from wyplaty_calc w2 where w1.data = w2.data)
                                    order by w1.data'''):

            p = Pensja(config, row[1])

            c_updater = db.cursor()
            c_updater.execute('insert into wyplaty_calc (data, netto) values (?, ?)', [ row[0], p.netto ])

            inserted += 1

        print('Wstawiono rekordów: {}'.format(inserted))
        db.commit()
    finally:
        db.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Skrypt do wypełniania bazy danych z wypłatami')

    parser.add_argument('-d', '--db', help='Nazwa wejściowej bazy danych', required=True)
    parser.add_argument('-m', '--mode', help='Tryb wyliczeń: pensja', required=True)
    parser.add_argument('-c', '--config', help='Dodatkowy plik konfiguracyjny', nargs='*')
    parser.add_argument('-f', '--force', help='Nadpisuje wszystkie wartości', action='store_true')

    args = parser.parse_args()

    config = Config('config.json')

    if args.config:
        config.override(args.config)

    if args.mode == 'pensja':
        pensja(args.db, config, args.force)
    else:
        raise Exception('Nieznany tryb: {}'.format(args.tryb))
