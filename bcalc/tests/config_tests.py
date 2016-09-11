import unittest

from bcalc.config import Config

class ConfigTests(unittest.TestCase):
    def test_default_load(self):
        config = Config()
        self.assertEqual(111.25, config['koszty_miejscowe'])

    def test_override(self):
        config = Config()
        self.assertEqual(111.25, config['koszty_miejscowe'])

        config['koszty_miejscowe'] = 222
        self.assertEqual(222, config['koszty_miejscowe'])

    def test_override_single(self):
        config = Config()

        config.override_single(['koszty_miejscowe=222'])
        self.assertEqual(222, config['koszty_miejscowe'])
