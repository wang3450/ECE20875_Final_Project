import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn import linear_model
import statsmodels.api as sm
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.patches as mpatches


temp_dictionary = {}
df = pd.read_csv('nyc-east-river-bicycle-counts.csv')
highTemp = list(df['High Temp (°F)'])  #reads a column into a pandas object and converts to list
lowTemp = list(df['Low Temp (°F)'])
totalRiders = list(df['Total'])

temp_dictionary['High Temp'] = highTemp
temp_dictionary['Low Temp'] = lowTemp
temp_dictionary['Total'] = totalRiders

data = DataFrame(temp_dictionary,columns=['High Temp','Low Temp','Total'])

X = data[['High Temp', 'Low Temp']].astype(float)
Y = data['Total'].astype(float)

regression = linear_model.LinearRegression()
regression.fit(X,Y)

print('Intercept: \n', regression.intercept_)
print('Coefficients: \n', regression.coef_)

#GUI
root = tk.Tk()
canvas1 = tk.Canvas(root, width = 500, height = 300)
canvas1.pack()

intercept_result = ('Intercept: ', regression.intercept_)
intercept_label = tk.Label(root, text=intercept_result, justify='center')
canvas1.create_window(260, 220, window=intercept_label)

coefficient_result = ('Coefficients: ', regression.coef_)
coefficient_label = tk.Label(root, text=coefficient_result, justify='center')
canvas1.create_window(260, 240, window=coefficient_label)

label1 = tk.Label(root, text='Enter High Temp: ')
canvas1.create_window(120,100,window=label1)

entry1 = tk.Entry(root)
canvas1.create_window(270, 100, window=entry1)

label2 = tk.Label(root, text='Enter Low Temp: ')
canvas1.create_window(120, 120, window=label2)

entry2 = tk.Entry(root)
canvas1.create_window(270,120,window=entry2)

def values():
    global newHighTemp
    newHighTemp = float(entry1.get())

    global newLowTemp
    newLowTemp = float(entry2.get())

    prediction = ('Predicted Index: ', regression.predict([[newHighTemp ,newLowTemp]]))
    prediction_label = tk.Label(root, text=prediction, bg = 'orange')
    canvas1.create_window(260, 280, window=prediction_label)

button = tk.Button(root, text='Predict Number of Total Riders',command=values,bg='orange')
canvas1.create_window(270, 150, window=button)

figure1 = plt.Figure(figsize=(5,4), dpi = 100)
ax1 = figure1.add_subplot(111)
ax1.scatter(data['High Temp'].astype(float),data['Total'].astype(float), color = 'r')
scatter3 = FigureCanvasTkAgg(figure1, root)
scatter3.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
patch = mpatches.Patch(color = 'red', label='Total Riders')
ax1.legend(handles=[patch])
ax1.set_xlabel('High Temp')
ax1.set_title('High Temperature vs Total Riders')

figure2 = plt.Figure(figsize=(5,4), dpi = 100)
ax2 = figure2.add_subplot(111)
ax2.scatter(data['Low Temp'].astype(float),data['Total'].astype(float), color = 'g')
scatter4 = FigureCanvasTkAgg(figure2, root)
scatter4.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
patch = mpatches.Patch(color = 'green', label='Total Riders')
ax2.legend(handles=[patch])
ax2.set_xlabel('Low Temp')
ax2.set_title('Low Temp vs Total Riders')

root.mainloop()
