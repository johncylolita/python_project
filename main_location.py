import csv
from dataclasses import dataclass


@dataclass
class Local_Weather:
    location: str
    max_temp: int
    min_temp: int
    avg_temp: float
    avg_humid: float

    @classmethod
    def weather_by_location(cls, location, max_temp, min_temp, avg_temp, avg_humid):
        return cls(
            location = location,
            max_temp = max_temp,
            min_temp = min_temp,
            avg_temp = avg_temp,
            avg_humid = avg_humid
        )
    
    def print_metrics(self):
        print(f"Location:{self.location}")
        print(f"Maximum temperature: {self.max_temp}")
        print(f"Minimum temperature: {self.min_temp}")
        print(f"Average temperature: {self.avg_temp}")
        print(f"Avearge humidity: {self.avg_humid}")


def average(lst):
    return sum(lst) / len(lst)


def file_reader(filename):
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)

        weather_data = {}

        for row in reader:
            location = row[3]
            temp = float(row[1])
            humid = float(row[2])

            if location not in weather_data:
                weather_data[location] = {'temp': [], 'humid': []}

            weather_data[location]['temp'].append(temp)
            weather_data[location]['humid'].append(humid)

    return weather_data

def analyze_weather_data(weather_data):
    weather_metrics = []

    for location, data in weather_data.items():
        max_temp = max(data['temp'])
        min_temp = min(data['humid'])
        avg_temp = average(data['temp'])
        avg_humid = average(data['humid'])

        weather = Local_Weather.weather_by_location(
            location,
            max_temp,
            min_temp,
            avg_temp,
            avg_humid
        )

        weather_metrics.append(weather)

    return weather_metrics


def print_weather_metrics(weather_metrics):
    for weather in weather_metrics:
        weather.print_metrics()
        print()


if __name__ == "__main__":
    weather_data = file_reader("weather_data_with_location.csv")
    weather_metrics = analyze_weather_data(weather_data)
    # print(weather_metrics)
    print_weather_metrics(weather_metrics)


















    
