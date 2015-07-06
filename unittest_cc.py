import application
import unittest

class Test_CountriesAndCapitals(unittest.TestCase):
    #Function 1: validation_min
    def test_validation_min(self):
        class_country_and_capital = application.country_and_capital()
        self.assertTrue(class_country_and_capital.validation_min("HOLA").islower())
    #Function 2: validation_menu
    def test_validation_menu(self):
        class_country_and_capital = application.country_and_capital()
        self.assertEqual(class_country_and_capital.validation_menu("COUNTRY"), "Valid Input")
    #Function 3: verify_countrycapital
    def test_verify_countrycapital(self):
        class_country_and_capital = application.country_and_capital()
        self.assertEqual(class_country_and_capital.verify_countrycapital("a","b"), "Entered correctly")

if __name__ == "__main__":
    unittest.main()
