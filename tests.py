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


    # verifies if a card with invalid starting bits returns False
    # Picked using Category Partition Testing
    def test7(self):
        a = 237423670482533
        self.assertFalse(credit_card_validator(a))


    # verifies if a card with invalid starting bits returns False
    # Picked using Category Partition Testing
    def test8(self):
        a = 23742367048215128
        self.assertFalse(credit_card_validator(a))
    

    # verifies if a card with invalid length returns False
    # Picked using Category Partition Testing
    def test9(self):
        a = 42
        self.assertFalse(credit_card_validator(a))
        self.assertFalse(credit_card_validator(513))
        self.assertFalse(credit_card_validator(554))
        self.assertFalse(credit_card_validator(349))
        self.assertFalse(credit_card_validator(372))



    # verifies if a American Express with invalid length returns False
    # Picked using Category Partition Testing
    def test10(self):
        a = 3493575731247028
        self.assertFalse(credit_card_validator(a))


    # verifies if a Visa with invalid length returns False
    # Picked using Category Partition Testing
    def test11(self):
        a = 406570033553282
        self.assertFalse(credit_card_validator(a))

    
    # verifies if a MasterCard with invalid length returns False
    # Picked using Category Partition Testing
    def test12(self):
        a = 537207584445483
        self.assertFalse(credit_card_validator(a))


    # verifies if a American Express with inproper prefixes but proper check bits fails
    # Picked using Category Partition Testing
    def test12(self):
        a = 357423670482150
        self.assertFalse(credit_card_validator(a))


    # verifies if American Express with valid lengths and valid check bits returns True
    # Picked using Category Partition Testing
    def test13(self):
        a = 379357573124705
        self.assertTrue(credit_card_validator(a))


    # verifies if MasterCard with valid lengths and valid check bits returns True
    # Picked using Category Partition Testing
    def test14(self):
        a = 2221075184720507
        self.assertTrue(credit_card_validator(a))


    # verifies if a visa with a decimal returns false
    # Picked using Category Partition Testing
    def test15(self):
        a = 491682288.163365
        self.assertFalse(credit_card_validator(a))


    # verifies if MasterCard with valid lengths and valid check bits returns True
    # Picked using Category Partition Testing
    def test16(self):
        a = 2720075184720503
        self.assertTrue(credit_card_validator(a))


    # verifies if Mastercard with valid lengths and valid check bits returns True
    # Picked using Category Partition Testing
    def test17(self):
        a = 5193575731247059
        self.assertTrue(credit_card_validator(a))


    # verifies if Mastercard with valid lengths and valid check bits returns True
    # Picked using Category Partition Testing
    def test18(self):
        a = 5593575731247055
        self.assertTrue(credit_card_validator(a))


    # verifies if Mastercard with invalid prefix but proper checksum returns false
    # Picked using Category Partition Testing
    def test19(self):
        a = 5093575731247050
        self.assertFalse(credit_card_validator(a))


    # verifies if Mastercard with invalid prefix but proper checksum returns false
    # Picked using Category Partition Testing
    def test20(self):
        a = 51935757312470501
        self.assertFalse(credit_card_validator(a))


    # verifies if Visa with invalid prefix but proper checksum returns false
    # Picked using Category Partition Testing
    def test21(self):
        a = 49357573124705015
        self.assertFalse(credit_card_validator(a))

    


if __name__ == '__main__':
    unittest.main()
