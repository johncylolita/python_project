import csv


def file_reader(filename):
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)

        temperature = []
        humidity = []

        for row in reader:
            temperature.append(float(row[1]))
            humidity.append(int(row[2]))

    return temperature, humidity


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

def sum_lst(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

def average(lst):
    avg = sum_lst(lst) / len(lst)
    return avg


if __name__ =="__main__":
    temperature, humidity = file_reader("weather_data.csv")
    print(f"The Maximum temperature is:",max(temperature))
    print(f"The Minimum temperature is:",min(temperature))
    print(f"The Average temperature is:",average(temperature))
    print(f"The Average humidity is:",average(humidity))
