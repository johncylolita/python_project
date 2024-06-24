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
        self.temperature, self.humidity, self.location = self.file_reader()
        self.new_data = self.group_by()


    def file_reader(self):
        with open(self.filename, "r") as csvfile:
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

    def group_by(self):
        from collections import defaultdict
        new_data = defaultdict(list)
        for temp, humid, loc in zip(self.temperature, self.humidity, self.location):
            new_data[loc].append((temp,humid))
        return new_data
    
    @staticmethod
    def average(lst):
        return sum(lst) / len(lst)

    def metrics(self):
        for loc, data in self.new_data.items():
            temp = [i for i,j in data]
            humid = [j for i,j in data]
            print(f"Location:{loc}")
            print(f"Maximum temperature: {max(temp)}")
            print(f"Minimum temperature: {min(temp)}")
            print(f"Average temperature: {self.average(temp)}")
            print(f"Avearge humidity: {self.average(humid)}")
            


if __name__ == '__main__':
    weather_analysis = Local_Weather('weather_data_with_location.csv')
    weather_analysis.group_by()
    weather_analysis.metrics()