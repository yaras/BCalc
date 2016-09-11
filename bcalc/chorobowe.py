import argparse
from argparse import RawTextHelpFormatter

from bcalc.config import Config
from bcalc.chorobowe_printer import WynagrodzenieChorobowePrettyPrinter

class WynagrodzenieChorobowe:
    CHOROBOWE_PARAM = 'chorobowe'
    EMERYTALNA_PARAM = 'emerytalna_pracownik'
    RENTOWA_PARAM = 'rentowa_pracownik'
    CHOROBOWA_PARAM = 'chorobowa_pracownik'
    WALUTA_PARAM = 'waluta'

    def __init__(self, config, pensje, choroba):
        self.parametry = config

        self.pensje = [float(p) for p in pensje[:12]]
        self.choroba = int(choroba)

        self.waluta = self.parametry[self.WALUTA_PARAM]
        self.procent_skladki = self.parametry[self.EMERYTALNA_PARAM] + self.parametry[self.RENTOWA_PARAM] + self.parametry[self.CHOROBOWA_PARAM]

        self.srednia = round(sum(self.pensje) / len(self.pensje), 2)
        self.podstawa = self.srednia * (1.00 - self.procent_skladki)

        self.zasilek_dziennie = round(self.podstawa * self.parametry[self.CHOROBOWE_PARAM] / 30, 2)
        self.wynagrodzenie_chorobowe = self.choroba * self.zasilek_dziennie

        ostatnia_pensja = self.pensje[-1:][0]

        self.potracenie = round(ostatnia_pensja / 30 * self.choroba, 2)

        self.wynagrodzenie = ostatnia_pensja - self.potracenie

        self.wynagrodzenie_zasilek = self.wynagrodzenie + self.wynagrodzenie_chorobowe

def main():
    parser = argparse.ArgumentParser(description='Wyliczanie zasiłku chorobowego.')

    parser.add_argument('-p', '--pensje', help='Wynagrodzenia brutto (ostatnie 12 miesięcy)', nargs='+')
    parser.add_argument('-c', '--choroba', help='Liczba dni choroby', required=True)
    parser.add_argument('--config', help='Nazwa plików z dodatkowymi parametrami', nargs='*')
    parser.add_argument('--param', help='Nadpisanie wybranego parametru (format: PARAMETR=WARTOŚĆ)', nargs='*')

    args = parser.parse_args()

    config = Config()

    if args.config:
        config.override(args.config)

    if args.param:
        config.override_single(args.param)

    wynagrodzenie = WynagrodzenieChorobowe(config, args.pensje, args.choroba)
    printer = WynagrodzenieChorobowePrettyPrinter()
    print(printer.format(wynagrodzenie))

if __name__ == '__main__':
    main()
