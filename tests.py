import unittest
from credit_card_validator import credit_card_validator

class TestCase(unittest.TestCase):
    def test1(self):
        a = 349094094095321
        self.assertFalse(credit_card_validator(a))
if __name__ == '__main__':
  unittest.main(verbosity=2)