import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn import linear_model
import statsmodels.api as sm

temp_dictionary = {}
df = pd.read_csv('nyc-east-river-bicycle-counts.csv')
highTemp = list(df['High Temp (°F)'])  #reads a column into a pandas object and converts to list
lowTemp = list(df['Low Temp (°F)'])
totalRiders = list(df['Total'])

temp_dictionary['High Temp'] = highTemp
temp_dictionary['Low Temp'] = lowTemp
temp_dictionary['Total'] = totalRiders

data = DataFrame(temp_dictionary,columns=['High Temp','Low Temp','Total'])

plt.scatter(data['High Temp'],data['Total'],color="red")
plt.title('Total Riders vs High Temp', fontsize=14)
plt.xlabel('High Temp', fontsize=14)
plt.ylabel('Total Riders', fontsize=14)
plt.grid(True)
plt.show()

plt.scatter(data['Low Temp'],data['Total'],color="green")
plt.title('Total Riders vs Low Temp', fontsize=14)
plt.xlabel('Low Temp', fontsize=14)
plt.ylabel('Total Riders', fontsize=14)
plt.grid(True)
plt.show()

X1 = data[['High Temp','Low Temp']]
Y1 = data['Total']

regr = linear_model.LinearRegression()
regr.fit(X1, Y1)

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)

X2 = sm.add_constant(X1)
model = sm.OLS(Y1,X2).fit()
print(model.summary())
