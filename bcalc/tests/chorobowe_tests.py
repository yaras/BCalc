import unittest

from bcalc.config import Config
from bcalc.chorobowe import WynagrodzenieChorobowe

class WynagrodzenieChoroboweTests(unittest.TestCase):
    def testWynagrodzenieChorobowe(self):
        ch = WynagrodzenieChorobowe(Config(), [3050, 3050, 3050, 3050, 3050, 3050, 3050, \
                3330, 3330, 3330, 3330, 3330], 8)

        self.assertAlmostEqual(ch.podstawa, 2732.52, 2)

    def testWynagrodzenieChoroboweDziennie(self):
        ch = WynagrodzenieChorobowe(Config(), [3050, 3050, 3050, 3050, 3050, 3050, 3050, \
            3330, 3330, 3330, 3330, 3330], 8)

        self.assertAlmostEqual(ch.zasilek_dziennie, 72.87, 2)

    def testWynagrodzenieChorobowe(self):
        ch = WynagrodzenieChorobowe(Config(), [3050, 3050, 3050, 3050, 3050, 3050, 3050, \
            3330, 3330, 3330, 3330, 3330], 8)

        self.assertAlmostEqual(ch.wynagrodzenie_chorobowe, 582.96, 2)

    def testPotracenie(self):
        ch = WynagrodzenieChorobowe(Config(), [3050, 3050, 3050, 3050, 3050, 3050, 3050, \
            3330, 3330, 3330, 3330, 3330], 8)

        self.assertAlmostEqual(ch.potracenie, 888.00, 2)

    def testWynagrodzenie(self):
        ch = WynagrodzenieChorobowe(Config(), [3050, 3050, 3050, 3050, 3050, 3050, 3050, \
            3330, 3330, 3330, 3330, 3330], 8)

        self.assertAlmostEqual(ch.wynagrodzenie, 2442.00, 2)

if __name__ == '__main__':
    unittest.main()
