import pandas as pd
import matplotlib.pyplot as plot
# Read the CSV file into a Pandas dataframe
dataframe = pd.read_csv('data.csv')
print("Statistics of Data:\n{} \n".format(dataframe.describe()))
# Check for null values
print("Number of null Values in data per column: \n{} \n".format(dataframe.isnull().sum()))

# Replace null values with the mean
dataframe.fillna(dataframe.mean(), inplace=True)

# Aggregate data for two columns
columns = ['Duration', 'Calories']
agg = dataframe[columns].agg(['min', 'max', 'count', 'mean'])
print("Aggrigate data of two columns (Duration, Calories) : \n {} \n".format(agg))

# Filter data with calories between 500 and 1000
dataframe_500_1000 = dataframe[(dataframe['Calories'] >= 500) & (dataframe['Calories'] <= 1000)]
print("Data with calories between 500 and 1000: \n {} \n".format(dataframe_500_1000))
# Filter data with calories > 500 and pulse < 100
dataframe_500_pulse = dataframe[(dataframe['Calories'] > 500) & (dataframe['Pulse'] < 100)]
print("Data with calories > 500 and pulse < 100: \n {} \n".format(dataframe_500_pulse))
# Create new dataframe without "Maxpulse" column
dataframe_modified = dataframe.drop('Maxpulse', axis=1)

# Delete "Maxpulse" column from the main dataframe dataframe
dataframe.drop('Maxpulse', axis=1, inplace=True)

# Convert "Calories" column to int datatype
dataframe['Calories'] = dataframe['Calories'].astype(int)

# Scatter plot for "Duration" and "Calories"

plot.scatter(dataframe['Duration'], dataframe['Calories'])
plot.xlabel('Duration')
plot.ylabel('Calories')
plot.show()
