import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plot

# Import the data
dataframe = pd.read_csv('Salary_Data.csv')

# Split the data into train and test partitions
X = dataframe[['YearsExperience']]
y = dataframe[['Salary']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0)

# Train and predict the model
reg = LinearRegression()
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)

# Calculate the mean squared error
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error: ", mse)

# Visualize the train and test data using scatter plot
plot.scatter(X_train, y_train, color='black')
plot.scatter(X_test, y_test, color='red')
plot.plot(X_train, reg.predict(X_train), color='orange')
plot.xlabel('Years of Experience')
plot.ylabel('Salary')
plot.title('Training and Test data')
plot.show()
