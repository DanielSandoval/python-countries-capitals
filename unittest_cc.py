import application
import unittest

class Test_CountriesAndCapitals(unittest.TestCase):
    #Function menu_option
    def test_menu_option(self):
        class_country_and_capital = application.country_and_capital()
        self.assertTrue(class_country_and_capital.menu_option("HOLA").lower())
    def test_verify_countrycapital(self):
        class_country_and_capital = application.country_and_capital()
        self.assertEqual(class_country_and_capital.verify_countrycapital("a","b"), "Entered correctly")

if __name__ == "__main__":
    unittest.main()
