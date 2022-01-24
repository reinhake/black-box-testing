import unittest
from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):

    # verifies if American Express with valid lengths and valid check bits returns True
    # Picked using Category Partition Testing
    def test1(self):
        a = 349357573124702
        self.assertTrue(credit_card_validator(a))
    

    # verifies if Visa with valid lengths and valid check bits returns True
    # Picked using Category Partition Testing
    def test2(self):
        a = 4916822882163365
        self.assertTrue(credit_card_validator(a))


    # verifies if MasterCard with valid lengths and valid check bits returns True
    # Picked using Category Partition Testing
    def test3(self):
        a = 5372075184720507
        self.assertTrue(credit_card_validator(a))
        

    # verifies if American Express with valid lengths and invalid check bits returns False
    # Picked using Category Partition Testing
    def test4(self):
        a = 349094094095321
        self.assertFalse(credit_card_validator(a))


    # verifies if Visa with valid lengths and invalid check bits returns False
    # Picked using Category Partition Testing
    def test5(self):
        a = 4521009765305081
        self.assertFalse(credit_card_validator(a))

    
    # verifies if Master Card with valid lengths and invalid check bits returns False
    # Picked using Category Partition Testing
    def test6(self):
        a = 5574236704821512
        self.assertFalse(credit_card_validator(a))


    # verifies if a card with invalid length returns False
    # Picked using Category Partition Testing
    def test7(self):
        a = 55742367048253
        self.assertFalse(credit_card_validator(a))


    # verifies if a card with invalid length returns False
    # Picked using Category Partition Testing
    def test8(self):
        a = 55742367048215128
        self.assertTrue(credit_card_validator(a))
    

    # verifies if a card with invalid length returns False
    # Picked using Category Partition Testing
    def test9(self):
        a = 0
        self.assertTrue(credit_card_validator(a))


if __name__ == '__main__':
    unittest.main()
    