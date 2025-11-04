#Matthew Rozendaal
#Assignment 7.2
#Due Date: 11/3/2025


#Create a file called test_cities.py that tests the function you just wrote (remember that you need to import unittest and the function you want to test). Write a method called test_city_country() to verify that calling your function with values such as santiago and chile results in the correct string. Run test_cities.py, and make sure test_city_country() passes. When it passes, take a screenshot of the result and paste in into your Word document.
#Modify your city_country function in city_functions.py so it requires a third parameter, population.
    #  It should now return a single string of the form City, Country - population xxx, such as Santiago, Chile - population 5000000.
#Run test_cities.py again. It should fail. Take a screenshot of the result and paste into your Word document.
#Now modify your city_country function in city_functions.py so that the population parameter is optional.
#Run test_cities.py again. It should pass. Take a screenshot of the result and paste into your Word document.
#Modify your city_country function in city_functions.py so it requires a fourth parameter, language. It should now return a single string of the form City, Country - population xxx, Language, such as Santiago, Chile - population 5000000, Spanish.
#Run test_cities.py again. It should fail. Take a screenshot of the result and paste into your Word document.
#Now modify your city_country function in city_functions.py so that the language argument is optional.
#Run test_cities.py again. It should pass. Take a screenshot of the result and paste into your Word document.
#Run city_functions.py. Call the function at least three times using a City, Country for one, City, Country, Population for the next and City, Country, Population, Language for the last. Excecute city_functions.py and take a screenshot of the result. Paste that screenshot into your Word document.