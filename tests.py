import unittest
from credit_card_validator import credit_card_validator

class TestCase(unittest.TestCase):
    #verifies if MasterCard with valid langths and invalid check bits returns False
    #Picked using Category Partition Testing
    def test1(self):
        a = 349094094095321
        self.assertTrue(credit_card_validator(a))
    
    def test2(self):
        a = 4521009765305084
        self.assertTrue(credit_card_validator(a))
if __name__ == '__main__':
  unittest.main(verbosity=2)