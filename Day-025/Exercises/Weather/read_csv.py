# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

import csv

with open("weather_data.csv") as file:
    data = csv.reader(file)
    print(data)
