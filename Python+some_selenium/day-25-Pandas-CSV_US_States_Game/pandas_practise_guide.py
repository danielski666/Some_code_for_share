# with open("weather_data.csv") as data_f:
#     data = data_f.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_f:
#     data = csv.reader(data_f)
#     temperatures = [int(row[1]) for row in data if row[1] != "temp"]
#     # for row in data:
#     #     if row[1] != "temp": temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# average_temp = sum(temp_list)/len(temp_list)
# average = data["temp"].mean()
# print(round(average_temp, 2))
# print(average)
#
# print(data["temp"].max())
# print(data.condition)

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
monday = data[data.day == "Monday"]
print(monday.condition)
#
# print(monday.temp*9/5+32)
#
# data_dict = {
#     "students": ["Amy", "Luke", "James"],
#     "scores": [76, 56, 65]
# }
# students_csv = pandas.DataFrame(data_dict)
# students_csv.to_csv("students.csv")
# print(students_csv)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrels = {
    "Fur Color": [],
    "Count": []
}
colors = ["Gray", "Cinnamon", "Black"]
for color in colors:
    squirrel_list = data[data["Primary Fur Color"] == color]
    squirrels["Fur Color"].append(color)
    squirrels["Count"].append(len(squirrel_list))

squirrels_csv = pandas.DataFrame(squirrels)
print(squirrels_csv)
squirrels_csv.to_csv("squirrels_color_count.csv")