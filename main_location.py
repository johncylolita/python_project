import csv
from dataclasses import dataclass, field

@dataclass
class Local_Weather:
    filename: str
    temperature: list = field(init=False)
    humidity: list = field(init=False)
    location: list = field(init=False)
    new_data: dict = field(init=False)

    def __post_init__(self):
        self.temperature, self.humidity, self.location = self.file_reader(self.filename)
        self.new_data = self.group_by(self.temperature, self.humidity, self.location)

    @classmethod
    def file_reader(cls, filename):
        with open(filename, "r") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)

            temperature = []
            humidity = []
            location = []

            for row in reader:
                temperature.append(float(row[1]))
                humidity.append(int(row[2]))
                location.append(row[3])

        return temperature, humidity, location

    @classmethod
    def group_by(cls, temperature, humidity,location):
        from collections import defaultdict
        new_data = defaultdict(list)
        for temp, humid, loc in zip(temperature, humidity, location):
            new_data[loc].append((temp,humid))
        return new_data
    
    @staticmethod
    def average(lst):
        return sum(lst) / len(lst)

    @classmethod
    def metrics(cls,new_data):
        for loc, data in new_data.items():
            temp = [i for i,j in data]
            humid = [j for i,j in data]
            print(f"Location:{loc}")
            print(f"Maximum temperature: {max(temp)}")
            print(f"Minimum temperature: {min(temp)}")
            print(f"Average temperature: {cls.average(temp)}")
            print(f"Avearge humidity: {cls.average(humid)}")
            


if __name__ == '__main__':
    weather_analysis = Local_Weather('weather_data_with_location.csv')
    Local_Weather.metrics(weather_analysis.new_data)