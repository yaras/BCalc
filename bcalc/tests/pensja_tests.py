import unittest

from bcalc.pensja import Pensja, BruttoCalc, SimpleRangeGenerator

class TestBase(unittest.TestCase):
    def setUp(self):
        self.parametry = {
          "waluta": "zł",
          "koszty_miejscowe": 111.25,
          "wspolczynnik_emerytalna_pracownik": 0.5,

          "emerytalna_pracownik": 0.0976,
          "rentowa_pracownik": 0.015,
          "chorobowa_pracownik": 0.0245,

          "emerytalna_pracodawca": 0.0976,
          "rentowa_pracodawca": 0.065,
          "wypadkowa_pracodawca": 0.0180,
          "fp_pracodawca": 0.0245,
          "fgsp_pracodawca": 0.0010,

          "podatek": 0.18,

          "kwota_zmniejszajaca": 46.33,

          "zdrowotna_pobierana": 0.09,
          "zdrowotna_odliczana": 0.0775,
        }

class PensjaTests(TestBase):
    def testEmerytalna(self):
        p = Pensja(self.parametry, 13000)
        self.assertAlmostEqual(p.emerytalna, 1268.80, 2)

    def testRentowa(self):
        p = Pensja(self.parametry, 13000)
        self.assertAlmostEqual(p.rentowa, 195.00, 2)

    def testChorobowa(self):
        p = Pensja(self.parametry, 13000)
        self.assertAlmostEqual(p.chorobowa, 318.50, 2)

    def testZusRazem(self):
        p = Pensja(self.parametry, 13000)
        self.assertAlmostEqual(p.zus_razem, 1782.3, 2)

    def testPodstawaOpodatkowania(self):
        p = Pensja(self.parametry, 13000)
        self.assertAlmostEqual(p.podstawa_opodatkowania, 11106.45, 2)

    def testPodstawa(self):
        p = Pensja(self.parametry, 13000)
        self.assertAlmostEqual(p.podstawa, 11106.00, 2)

    def testZaliczkaPrzed(self):
        p = Pensja(self.parametry, 13000)
        self.assertAlmostEqual(p.zaliczka_przed, 1952.83, 2)

    def testPodstawaSkladek(self):
        p = Pensja(self.parametry, 1850)
        self.assertAlmostEqual(p.podstawa_skladek, 1596.37, 2)

    def testZdrowotnaPobierana(self):
        p = Pensja(self.parametry, 13000)
        self.assertAlmostEqual(p.skl_zdrowotna_pobierana, 1009.59, 2)

    def testZdrowotnaOdliczana(self):
        p = Pensja(self.parametry, 13000)
        self.assertAlmostEqual(p.skl_zdrowotna_odliczana, 869.37, 2)

    def testPodatek(self):
        p = Pensja(self.parametry, 13000)
        self.assertAlmostEqual(p.podatek, 1083.00, 2)

    def testNetto(self):
        p = Pensja(self.parametry, 13000)
        self.assertAlmostEqual(p.netto, 9125.11, 2)

    def testEmerytalnaPracodawca(self):
        p = Pensja(self.parametry, 1850)
        self.assertAlmostEqual(p.emerytalna_pracodawca, 180.56, 2)

    def testRentowaPracodawca(self):
        p = Pensja(self.parametry, 1850)
        self.assertAlmostEqual(p.rentowa_pracodawca, 120.25, 2)

    def testWypadkowaPracodawca(self):
        p = Pensja(self.parametry, 1850)
        self.assertAlmostEqual(p.wypadkowa_pracodawca, 33.30, 2)

    def testFPPracodawca(self):
        p = Pensja(self.parametry, 1850)
        self.assertAlmostEqual(p.fp_pracodawca, 45.33, 2)

    def testFGSPPracodawca(self):
        p = Pensja(self.parametry, 1850)
        self.assertAlmostEqual(p.fgsp_pracodawca, 1.85, 2)

    def testZusPracodawca(self):
        p = Pensja(self.parametry, 1850)
        self.assertAlmostEqual(p.zus_razem_pracodawca, 381.29, 2)

    def testRazemPracodawca(self):
        p = Pensja(self.parametry, 1850)
        self.assertAlmostEqual(p.razem_pracodawca, 2231.28, 2)

    def testComplex(self):
        p = Pensja(self.parametry, 1456, 152.80)

        self.assertEqual(p.waluta, 'zł')
        self.assertAlmostEqual(p.przychod, 1456, 2)
        self.assertAlmostEqual(p.zasilek_chorobowy, 152.80, 2)

        self.assertAlmostEqual(p.zus_razem, 199.62, 2)

        self.assertAlmostEqual(p.podstawa, 1298, 2)
        self.assertAlmostEqual(p.zaliczka_przed, 187.3, 2)

        self.assertAlmostEqual(p.podatek, 78, 2)
        self.assertAlmostEqual(p.netto, 1204.36, 2)

class BruttoCalcTests(TestBase):
    def test_brutto_from_netto_simple(self):
        netto = 9125.11
        expectedBrutto = 13000

        calc = BruttoCalc(netto)
        actualBrutto = calc.calc(self.parametry)

        self.assertAlmostEqual(expectedBrutto, actualBrutto, 2)

class SimpleRangeGeneratorTests(unittest.TestCase):
    def test_generate(self):
        generator = SimpleRangeGenerator()
        self.assertEqual([1, 3, 5, 7, 9], list(generator.create_range(1, 10, 2)))

if __name__ == '__main__':
    unittest.main()
