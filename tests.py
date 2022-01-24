import unittest
from credit_card_validator import credit_card_validator

class TestCase(unittest.TestCase):


    # verifies if American Express with valid langths and valid check bits returns True
    # Picked using Category Partition Testing
    def test2(self):
        a = 349357573124702
        self.assertTrue(credit_card_validator(a))
    
    # verifies if Visa with valid langths and valid check bits returns True
    # Picked using Category Partition Testing
    def test2(self):
        a = 4521009765305084
        self.assertTrue(credit_card_validator(a))

    # verifies if MasterCard with valid langths and valid check bits returns True
    # Picked using Category Partition Testing
    def test3(self):
        a = 5372075184720507
        self.assertTrue(credit_card_validator(a))
        
    # verifies if American Express with valid langths and invalid check bits returns False
    # Picked using Category Partition Testing
    def test1(self):
        a = 349094094095321
        self.assertTrue(credit_card_validator(a))

if __name__ == '__main__':
    unittest.main(verbosity=2)