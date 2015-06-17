import application
import unittest

class Test_CountriesAndCapitals(unittest.TestCase):
    def test_min_countries_and_capitals(self):
        self.assertEqual(application.min_countries_and_capitals("HOLA", "MUNDO"), "Entered correctly")
    def test_write_country(self):
        self.assertTrue(application.write_country("HOLA").islower())

if __name__ == "__main__":
    unittest.main()
