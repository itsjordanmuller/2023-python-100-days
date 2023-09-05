# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

import csv

with open("weather_data.csv") as file:
    data = csv.reader(file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)
