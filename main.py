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


def average(lst):
    avg = sum(lst) / len(lst)
    return avg

def main():
    print(f"The Maximum temperature is:",max(temperature))
    print(f"The Minimum temperature is:",min(temperature))
    print(f"The Average temperature is:",average(temperature))
    print(f"The Average Humidity is:",average(humidity))

if __name__ == '__main__':
    main()