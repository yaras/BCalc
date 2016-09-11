from io import StringIO

from bcalc.printer import Printer

class PensjaPrettyPrinter(Printer):

    def __init__(self, separatorLength=50):
        super().__init__(separatorLength)

    def format(self, pensja):
        val = StringIO()
        self.printLabelValue('Wypłata brutto (1)', pensja.przychod, pensja.waluta, val)
        self.printSeparator(val)

        print('Dochód (2):                        {: >12,.2f} {}'.format(pensja.dochod, pensja.waluta), file=val)
        print('-' * self.separatorLength, file=val)

        if pensja.zasilek_chorobowy > 0:
            print('Zasiłek chorobowy (2a):            {: >12,.2f} {}'.format(pensja.zasilek_chorobowy, pensja.waluta), file=val)
            print('-' * self.separatorLength, file=val)

        print('ZUS (pracownik)', file=val)
        self.printLabelValue('   - emerytalna (3)', pensja.emerytalna, pensja.waluta, val)
        print('   - rentowa (4):                  {: >12,.2f} {}'.format(pensja.rentowa, pensja.waluta), file=val)
        print('   - chorobowa (5):                {: >12,.2f} {}'.format(pensja.chorobowa, pensja.waluta), file=val)
        print('', file=val)
        print('   Razem (6):                      {: >12,.2f} {}'.format(pensja.zus_razem, pensja.waluta), file=val)

        print('', file=val)

        print('ZUS (pracodawca)', file=val)
        print('   - emerytalna (7):               {: >12,.2f} {}'.format(pensja.emerytalna_pracodawca, pensja.waluta), file=val)
        print('   - rentowa (8):                  {: >12,.2f} {}'.format(pensja.rentowa_pracodawca, pensja.waluta), file=val)
        print('   - wypadkowa (9):                {: >12,.2f} {}'.format(pensja.wypadkowa_pracodawca, pensja.waluta), file=val)
        print('   - FP (10):                      {: >12,.2f} {}'.format(pensja.fp_pracodawca, pensja.waluta), file=val)
        print('   - FGSP (11):                    {: >12,.2f} {}'.format(pensja.fgsp_pracodawca, pensja.waluta), file=val)
        print('', file=val)
        print('   Razem (12):                     {: >12,.2f} {}'.format(pensja.zus_razem_pracodawca, pensja.waluta), file=val)
        print('-' * self.separatorLength, file=val)

        print('Podstawa wymiaru składki (13):     {: >12,.2f} {}'.format(pensja.podstawa_skladek, pensja.waluta), file=val)
        print('Składka zdrowotna pobierania (14): {: >12,.2f} {}'.format(pensja.skl_zdrowotna_pobierana, pensja.waluta), file=val)
        print('Składka zdrowotna odliczana (15):  {: >12,.2f} {}'.format(pensja.skl_zdrowotna_odliczana, pensja.waluta), file=val)

        print('-' * self.separatorLength, file=val)

        print('Podatek (16):                      {: >12,.2f} {}'.format(pensja.podatek, pensja.waluta), file=val)

        print('-' * self.separatorLength, file=val)

        print('Wypłata netto (17):                {: >12,.2f} {}'.format(pensja.netto, pensja.waluta), file=val)
        print('Koszt pracodawca (18):             {: >12,.2f} {}'.format(pensja.razem_pracodawca, pensja.waluta), file=val)

        return val.getvalue()
