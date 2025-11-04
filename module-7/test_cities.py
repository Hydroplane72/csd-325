#Create a file called test_cities.py that tests the function you just wrote (remember that you need to import unittest and the function you want to test). 
# Write a method called test_city_country() to verify that calling your function with values such as santiago and chile results in the correct string. 
# Run test_cities.py, and make sure test_city_country() passes. When it passes, take a screenshot of the result and paste in into your Word document.
import unittest
from city_functions import city_country

class TestCityFunctions(unittest.TestCase):
    def test_city_country(self):
        """Test city_country function with city and country."""
        #result = city_country("Santiago", "Chile", 5000000)
        #self.assertEqual(result, "Santiago, Chile - population 5000000")
        result = city_country("Santiago", "Chile")
        self.assertEqual(result, "Santiago, Chile - population 0, ")