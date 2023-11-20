# List to store travel logs
travel_log = [
    {"country": "France", "visits": 12, "cities": ["Paris", "Lille", "Dijon"]},
    {"country": "Germany", "visits": 5, "cities": ["Berlin", "Hamburg", "Stuttgart"]},
]


# Function to add a new country to the travel log
def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)


# Add Canada to travel log
add_new_country("Canada", 2, ["Vancouver", "Toronto"])

print("\nTravel Log\n")

# Display updated travel log
print(travel_log)
