#importing the necessary libraries
import csv

#creating the variables to store the individual values
temperature = []
humidity = []

#to open the csv file
with open("weather_data.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  #to skip the header row

    for row in reader:
        temperature.append(float(row[1]))
        humidity.append(int(row[2]))

# #to sort the temperature and calculate the max and min
# sorted_temperature = sorted(temperature)
# max_temperature = sorted_temperature[-1]
# min_temperature = sorted_temperature[0]
# print(max_temperature)
# print(min_temperature)



#to calculate the average of temperature and humidity
avg_temperature = sum(temperature) / len(temperature)
avg_humidity = sum(humidity) / len(humidity)



print(f"The Maximum temperature is:",max(temperature))
print(f"The Minimum temperature is:",min(temperature))
print(f"The Average temperature is:",avg_temperature)
print(f"The Average Humidity is:",avg_humidity)


