#importing the necessary modules
import pandas as pd

#reading the csv file
df = pd.read_csv("weather_data.csv")

#to print the first 10 entries of the dataframe
#print(df.head(10))

#to check the size of the dataframe
#print(df.shape)

#to print the columns of the dataframe
#print(df.columns)

#to calculate the max temp
max_temp = df['temperature'].max()

#to calculate the min temp
min_temp = df['temperature'].min()

#to calculate the avg temp
avg_temp = df["temperature"].mean()

#to calculate the avg humidity
avg_humid = df["humidity"].mean()

print(f"Maximum Temperature : {max_temp}")
print(f"Minimum Temperature : {min_temp}")
print(f"Average Temperature : {avg_temp}")
print(f"Average Humidity : {avg_humid}")