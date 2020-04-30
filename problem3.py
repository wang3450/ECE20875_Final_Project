import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import statistics
from pandas import DataFrame
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import statsmodels.api as sm

df = pd.read_csv('nyc-east-river-bicycle-counts.csv') #read in csv file using pandas
totalRiders = list(df['Total'])                       #load total and precipitation columns as string lists
precipitation = list(df['Precipitation'])

#clean data
for i in range(len(precipitation)):                     #cleaned the data for S and T
    if precipitation[i] == 'T':
        precipitation[i] = '0'
    if '(S)' in precipitation[i]:
        precipitation[i] = precipitation[i][:-4]

temp_dictionary = {}                                    #created dictionary
temp_dictionary['Precipitation'] = precipitation        #keys are columns names
temp_dictionary['Total'] = totalRiders                  #values are data in the forms of lists

data = DataFrame(temp_dictionary,columns=['Precipitation','Total'])     #created data frame from the dictionary

plt.scatter(data['Precipitation'].astype(float),data['Total'].astype(float),color="red")    #plotted the data
plt.title('Total Riders vs Precipitation', fontsize=14)

plt.xlabel('Precipitation', fontsize=14)
plt.ylabel('Total Riders', fontsize=14)
# plt.grid(True)

for i in range(len(precipitation)):                 #clean the lists so that they are floats instead of str
    precipitation[i] = float(precipitation[i])

for i in range(len(totalRiders)):
    totalRiders[i] = float(totalRiders[i])

X = np.array(precipitation).reshape(-1,1)                       #reshaped the independent variable because theres only one feature
Y = np.array(totalRiders)
transformer = PolynomialFeatures(degree=7, include_bias=False)     #created a polynmial regression model
transformer.fit(X)
X_ = transformer.transform(X)
model = LinearRegression()
model.fit(X_, Y)

r_sq = model.score(X_, Y)
intercept, coefficients = model.intercept_, model.coef_
print("intercept: " ,intercept)
print("coefficients: " ,coefficients)
print("r2 value:",r_sq)

X2 = sm.add_constant(X)                                             #ccreated a linear regression model
model2 = sm.OLS(Y,X2)
results = model2.fit()
print(results.summary())
plt.show()
