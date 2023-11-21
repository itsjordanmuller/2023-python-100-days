# Convert temperature from Celsius to Fahrenheit
def CelsiusToFahrenheit(temp):
    return (temp * 9 / 5) + 32


print("\nWeather Dictionary Exercise\n")

# Dictionary of temperatures in Celsius for each day
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

# Convert each day's temperature to Fahrenheit
weather_f = {day: CelsiusToFahrenheit(temp) for (day, temp) in weather_c.items()}

# Print the weather forecast in Fahrenheit
print(weather_f)
