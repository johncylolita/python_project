import csv


class local_weather():

    def __init__(self, filename):
        self.filename = filename
        self.temperature, self.humidity, self.location = self.file_reader()

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
        print(new_data)


    def max_temp(self):
        return max(self.temperature)


    def min_temp(self):
        return min(self.temperature)
    
    def avg_temp(self):
        return sum(self.temperature) / len(self.temperature)

    def avg_humid(self):
        return sum(self.humidity) / len(self.humidity)
    


if __name__ == '__main__':
    weather_analysis = local_weather('weather_data_with_location.csv')
    weather_analysis.group_by()


    print(weather_analysis.max_temp())
    print(weather_analysis.min_temp())
    print(weather_analysis.avg_temp())
    print(weather_analysis.avg_humid())