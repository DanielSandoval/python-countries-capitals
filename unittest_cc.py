import application
import unittest

class Test_CountriesAndCapitals(unittest.TestCase):
    def test_country(self):
        self.assertTrue(application.country("Hola").islower())
    def test_capital(self):
        self.assertTrue(application.capital("Hola").islower())
    def test_write_country(self):
        self.assertTrue(application.write_country("Hola").islower())

if __name__ == "__main__":
    unittest.main()
