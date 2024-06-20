import csv

#creating the variables to store the individual values
temperature = []
humidity = []

with open("weather_data.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  #to skip the header row

    for row in reader:
        temperature.append(float(row[1]))
        humidity.append(int(row[2]))


def maximum(lst):
    max = lst[0]
    for i in lst:
        if i > max:
            max = i
    return max

def minimum(lst):
    min = lst[0]
    for i in lst:
        if i < min:
            min = i

print(maximum(temperature))
