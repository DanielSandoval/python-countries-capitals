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
        self.assertEqual(class_country_and_capital.validation_menu("COUNTRY"), "country")
        self.assertEqual(class_country_and_capital.validation_menu("EXIT"), "exit")
        self.assertEqual(class_country_and_capital.validation_menu("COUNTRIES"), "countries")
        self.assertEqual(class_country_and_capital.validation_menu("CAPITALS"), "capitals")
        self.assertEqual(class_country_and_capital.validation_menu("ALL"), "all")
    #Function 3: verify_countrycapital
    def test_verify_countrycapital(self):
        class_country_and_capital = application.country_and_capital()
        self.assertEqual(class_country_and_capital.verify_countrycapital("a","b"), "Entered correctly")
    #Function 4: verify_add
    def test_verify_add(self):
        class_country_and_capital = application.country_and_capital()
        self.assertEqual(class_country_and_capital.verify_add("francia","paris"), "Added correctly")

if __name__ == "__main__":
    unittest.main()
