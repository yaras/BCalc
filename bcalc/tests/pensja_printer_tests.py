import unittest

from bcalc.pensja_printer import PensjaPrettyPrinter

class Dummy:
    pass

class PensjaPrinterTests(unittest.TestCase):
    def testFormat(self):
        pensja = Dummy()

        pensja.waluta = 'zł'
        pensja.przychod = 2000
        pensja.dochod = 123
        pensja.zasilek_chorobowy = 123
        pensja.emerytalna = 123
        pensja.rentowa = 123
        pensja.chorobowa = 123
        pensja.zus_razem = 123
        pensja.emerytalna_pracodawca = 123
        pensja.rentowa_pracodawca = 123
        pensja.wypadkowa_pracodawca = 123
        pensja.fp_pracodawca = 123
        pensja.fgsp_pracodawca = 123
        pensja.zus_razem_pracodawca = 123
        pensja.podstawa_skladek = 123
        pensja.skl_zdrowotna_pobierana = 123
        pensja.skl_zdrowotna_odliczana = 123
        pensja.podatek = 123
        pensja.netto = 123
        pensja.razem_pracodawca = 123

        printer = PensjaPrettyPrinter()
        print(printer.format(pensja))
        ret = printer.format(pensja).split('\n')

        self.assertEqual('Wypłata brutto (1):                    2,000.00 zł', ret[0])
        self.assertEqual('Dochód (2):                              123.00 zł', ret[2])
        self.assertEqual('Zasiłek chorobowy (2a):                  123.00 zł', ret[4])
        self.assertEqual('ZUS (pracownik)', ret[6])
        self.assertEqual('   - emerytalna (3):                     123.00 zł', ret[7])
        self.assertEqual('   - rentowa (4):                        123.00 zł', ret[8])
        self.assertEqual('   - chorobowa (5):                      123.00 zł', ret[9])
        self.assertEqual('   Razem (6):                            123.00 zł', ret[11])
        self.assertEqual('ZUS (pracodawca)', ret[13])
        self.assertEqual('   - emerytalna (7):                     123.00 zł', ret[14])
        self.assertEqual('   - rentowa (8):                        123.00 zł', ret[15])
        self.assertEqual('   - wypadkowa (9):                      123.00 zł', ret[16])
        self.assertEqual('   - FP (10):                            123.00 zł', ret[17])
        self.assertEqual('   - FGSP (11):                          123.00 zł', ret[18])
        self.assertEqual('   Razem (12):                           123.00 zł', ret[20])
        self.assertEqual('Podstawa wymiaru składki (13):           123.00 zł', ret[22])
        self.assertEqual('Składka zdrowotna pobierania (14):       123.00 zł', ret[23])
        self.assertEqual('Składka zdrowotna odliczana (15):        123.00 zł', ret[24])
        self.assertEqual('Podatek (16):                            123.00 zł', ret[26])
        self.assertEqual('Wypłata netto (17):                      123.00 zł', ret[28])
        self.assertEqual('Koszt pracodawca (18):                   123.00 zł', ret[29])


if __name__ == '__unittest__':
    unittest.main()
