# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# average_temp = data["temp"].mean()
# max_temp = data["temp"].max()

# def Average(list):
#     return sum(list) / len(list)


# average_temp = Average(temp_list)
# print(average_temp)
# print(max_temp)

# Get Data in Columns
# print(data["condition"])
# print(data.condition)

# Get Data in Rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])


# def CelsiusToFahrenheit(temp):
#     return (temp * 9 / 5) + 32


# monday = data[data.day == "Monday"]
# print(CelsiusToFahrenheit(monday.temp[0]))

# Create a data frame from scratch
data_dict = {"students": ["Amy", "James", "Jordan"], "scores": [76, 56, 65]}
dataFrame = pandas.DataFrame(data_dict)
print(dataFrame)
dataFrame.to_csv("score_data.csv")
