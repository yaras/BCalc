import argparse
import json
import abc
import sys

from bcalc.config import Config
from bcalc.pensja_printer import PensjaPrettyPrinter

class Pensja:

    KOSZTY_MIEJSCOWE_PARAM = 'koszty_miejscowe'
    WALUTA_PARAM = 'waluta'

    EMERYTALNA_PARAM = 'emerytalna_pracownik'
    RENTOWA_PARAM = 'rentowa_pracownik'
    CHOROBOWA_PARAM = 'chorobowa_pracownik'

    EMERYTALNA_PRACODAWCA_PARAM = 'emerytalna_pracodawca'
    RENTOWA_PRACODAWCA_PARAM = 'rentowa_pracodawca'
    WYPADKOWA_PRACODAWCA_PARAM = 'wypadkowa_pracodawca'
    FP_PRACODAWCA_PARAM = 'fp_pracodawca'
    FGSP_PRACODAWCA_PARAM = 'fgsp_pracodawca'

    PODATEK_PARAM = 'podatek'
    KWOTA_ZMNIEJSZAJACA_PARAM = 'kwota_zmniejszajaca'

    ZDROWOTNA_POBIERANA_PARAM = 'zdrowotna_pobierana'
    ZDROWOTNA_ODLICZANA_PARAM = 'zdrowotna_odliczana'

    def __init__(self, config, brutto, zasilek_chorobowy=0):

        if isinstance(config, Config):
            self.parametry = config.getAll()
        else:
            self.parametry = config

        self.__verify_parametry()

        self.waluta = self.parametry[self.WALUTA_PARAM]
        self.przychod = float(brutto)
        self.zasilek_chorobowy = zasilek_chorobowy;

        self.dochod = self.przychod - self.parametry[self.KOSZTY_MIEJSCOWE_PARAM]

        self.emerytalna = self.parametry[self.EMERYTALNA_PARAM] * self.przychod
        self.rentowa = self.parametry[self.RENTOWA_PARAM] * self.przychod
        self.chorobowa = self.parametry[self.CHOROBOWA_PARAM] * self.przychod
        self.zus_razem = self.emerytalna + self.rentowa + self.chorobowa

        self.emerytalna_pracodawca = self.parametry[self.EMERYTALNA_PRACODAWCA_PARAM] * self.przychod
        self.rentowa_pracodawca = self.parametry[self.RENTOWA_PRACODAWCA_PARAM] * self.przychod
        self.wypadkowa_pracodawca = self.parametry[self.WYPADKOWA_PRACODAWCA_PARAM] * self.przychod
        self.fp_pracodawca = self.parametry[self.FP_PRACODAWCA_PARAM] * self.przychod
        self.fgsp_pracodawca = self.parametry[self.FGSP_PRACODAWCA_PARAM] * self.przychod

        self.zus_razem_pracodawca = self.emerytalna_pracodawca + self.rentowa_pracodawca + self.wypadkowa_pracodawca + self.fp_pracodawca + self.fgsp_pracodawca

        self.podstawa_opodatkowania = self.dochod + self.zasilek_chorobowy - self.zus_razem

        self.podstawa = round(self.podstawa_opodatkowania)
        self.zaliczka_przed = round(self.podstawa_opodatkowania * self.parametry[self.PODATEK_PARAM], 2) - self.parametry[self.KWOTA_ZMNIEJSZAJACA_PARAM]

        self.podstawa_skladek = self.przychod + self.zasilek_chorobowy - self.zus_razem

        self.skl_zdrowotna_pobierana = self.podstawa_skladek * self.parametry[self.ZDROWOTNA_POBIERANA_PARAM]
        self.skl_zdrowotna_odliczana = self.podstawa_skladek * self.parametry[self.ZDROWOTNA_ODLICZANA_PARAM]

        self.podatek = round(self.zaliczka_przed - self.skl_zdrowotna_odliczana, 0)
        self.netto = round(self.przychod - self.zus_razem - self.skl_zdrowotna_pobierana - self.podatek + self.zasilek_chorobowy, 2)

        self.razem_pracodawca = self.przychod + self.zus_razem_pracodawca

    def __verify_parametry(self):
        required = [
            self.KOSZTY_MIEJSCOWE_PARAM,
            self.WALUTA_PARAM,
            self.EMERYTALNA_PARAM,
            self.RENTOWA_PARAM,
            self.CHOROBOWA_PARAM,
            self.EMERYTALNA_PRACODAWCA_PARAM,
            self.RENTOWA_PRACODAWCA_PARAM,
            self.WYPADKOWA_PRACODAWCA_PARAM,
            self.FP_PRACODAWCA_PARAM,
            self.FGSP_PRACODAWCA_PARAM,
            self.PODATEK_PARAM,
            self.KWOTA_ZMNIEJSZAJACA_PARAM,
            self.ZDROWOTNA_POBIERANA_PARAM,
            self.ZDROWOTNA_ODLICZANA_PARAM
        ]

        missing = [p for p in required if p not in self.parametry]

        if missing:
            raise Exception('W parametrach nie zdefiniowano: {}'.format(', '.join(missing)))

class BruttoCalc:
    def __init__(self, netto):
        self.netto = netto
        self.rangeGenerator = SimpleRangeGenerator()

    def calc(self, config):
        minBrutto = self.netto
        maxBrutto = 2 * self.netto

        for brutto in self.rangeGenerator.create_range(minBrutto, maxBrutto, 0.01):
            roundedBrutto = round(brutto, 2)
            pensja = Pensja(config, roundedBrutto)

            if pensja.netto >= self.netto:
                return roundedBrutto

class SimpleRangeGenerator:
    def create_range(self, minValue, maxValue, step):
        if minValue >= maxValue:
            raise Exception('Expected minValue to be lower than maxValue: {} vs. {}'.format(minValue, maxValue))

        if step <= 0:
            raise Exception('Expected step to be greater than 0')

        current = minValue

        while current < maxValue:
            yield current
            current += step

def main():
    parser = argparse.ArgumentParser(description='Kalkulator pensji. Jako parametr wejściowy należy podać albo brutto, albo netto.')

    parser.add_argument('-b', '--brutto', help='Wartość wynagrodzenia brutto')
    parser.add_argument('-n', '--netto', help='Wartość wynagrodzenia netto', type=float)
    parser.add_argument('-c', '--config', help='Nazwa plików z dodatkowymi parametrami', nargs='*')
    parser.add_argument('--param', help='Nadpisanie wybranego parametru (format: PARAMETR=WARTOŚĆ)', nargs='*')
    parser.add_argument('--zasilek-chorobowy', help='Opcjonalny zasiłek chorobowy otrzymany w danym miesiącu', default=0.0, type=float)

    args = parser.parse_args()

    if not args.brutto and not args.netto:
        print('Nie podano ani brutto, ani netto')
        sys.exit(1)

    if args.brutto and args.netto:
        print('Podano zarówno netto, jak i brutto. Nalezy podać tylko jedną wartość.')
        sys.exit(1)

    config = Config()

    if args.config:
        config.override(args.config)

    if args.param:
        config.override_single(args.param)

    if args.netto:
        bruttoCalc = BruttoCalc(args.netto)
        brutto = bruttoCalc.calc(config.getAll());
    else:
        brutto = args.brutto

    pensja = Pensja(config.getAll(), brutto, args.zasilek_chorobowy)

    printer = PensjaPrettyPrinter()

    print(printer.format(pensja))

if __name__ == '__main__':
    main()
