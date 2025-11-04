#Matthew Rozendaal
#Assignment 7.2
#Due Date: 11/3/2025

#Write a function that accepts two parameters: a city name and a country name. The function should return a single string of the form City, Country, such as Santiago, Chile. Store the function in a file named city_functions.py. In the same file, call the function at least three times using a City, Country values. Excecute city_functions.py and take a screenshot of the result. Paste that screenshot into your Word document.
#Modify your city_country function in city_functions.py so it requires a third parameter, population. It should now return a single string of the form City, Country - population xxx, such as Santiago, Chile - population 5000000.

def city_country(city: str, country: str, population: int = 0) -> str:
    """Return a formatted city-country string."""
    #return f"{city}, {country}"
    return f"{city}, {country} - population {population}"

# Call the function at least three times
print(city_country("New York", "United States"))
print(city_country("Tokyo", "Japan"))
print(city_country("Davenport", "United States"))
