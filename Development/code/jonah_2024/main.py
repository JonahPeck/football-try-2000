def major_language(country_name):
    country_language = {
        "China": "Mandarin",
        "India": "Hindi",
        "United States": "English",
        "Indonesia": "Indonesian",
        "Pakistan": "Urdu",
        "Brazil": "Portuguese",
        "Nigeria": "English",
        "Bangladesh": "Bengali",
        "Russia": "Russian",
        "Mexico": "Spanish",
        "Japan": "Japanese",
        "Ethiopia": "Amharic",
        "Philippines": "Filipino",
        "Egypt": "Arabic",
        "Vietnam": "Vietnamese",
        "DR Congo": "French",
        "Turkey": "Turkish",
        "Iran": "Persian",
        "Germany": "German",
        "Thailand": "Thai"
        # Add more countries and their major languages as needed
    }
    
    # Filter the dictionary to include only the 20 most populated countries
    top_20_countries = [
        "China", "India", "United States", "Indonesia", "Pakistan",
        "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico",
        "Japan", "Ethiopia", "Philippines", "Egypt", "Vietnam",
        "DR Congo", "Turkey", "Iran", "Germany", "Thailand"
    ]
    
    if country_name in top_20_countries:
        return f"The major language spoken in {country_name} is {country_language[country_name]}."
    else:
        return "Country not found or not within the 20 most populated countries."

# Example usage:
country_name = input("Enter a country name: ")
print(major_language(country_name))

#going to bed
