import csv
from dataclasses import dataclass


@dataclass
class LocalWeather:
    location: str
    max_temperature: int
    min_temperature: int
    avg_temperature: float
    avg_humidity: float

    @classmethod
    def weather_by_location(cls, location: str, temp: list, humid: list) -> 'LocalWeather':
        max_temp = max(temp)
        min_temp = min(temp)
        avg_temp = average(temp)
        avg_humid = average(humid)

        return cls(
            location = location,
            max_temperature = max_temp,
            min_temperature = min_temp,
            avg_temperature = avg_temp,
            avg_humidity = avg_humid
        )
    
    def print_metrics(self):
        print(f"Location:{self.location}")
        print(f"Maximum temperature: {self.max_temperature}")
        print(f"Minimum temperature: {self.min_temperature}")
        print(f"Average temperature: {self.avg_temperature}")
        print(f"Avearge humidity: {self.avg_humidity}")


def average(lst):
    return sum(lst) / len(lst)


def file_reader(filename: str) -> dict:
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)

        weather_data = {}

        for row in reader:
            location = row[3]

            if location not in weather_data:
                weather_data[location] = {'temp': [], 'humid': []}

            weather_data[location]['temp'].append(float(row[1]))
            weather_data[location]['humid'].append(float(row[2]))

    return weather_data

def analyze_weather_data(weather_data: dict) -> list[LocalWeather]:
    weather_metrics = []

    for location, data in weather_data.items():
        temp = data['temp']
        humid = data['humid']

        weather = LocalWeather.weather_by_location(location, temp,humid)
        weather_metrics.append(weather)

    return weather_metrics


if __name__ == "__main__":
    weather_data = file_reader("weather_data_with_location.csv")
    weather_metrics = analyze_weather_data(weather_data)
    for weather in weather_metrics:
        weather.print_metrics()
        print()