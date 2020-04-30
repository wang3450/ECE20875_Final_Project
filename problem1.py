import pandas as pd
from matplotlib import pyplot as plt
import numpy
import statistics

df = pd.read_csv('nyc-east-river-bicycle-counts.csv') #reads in the csv file
brooklyn = list(df['Brooklyn Bridge'])  #reads a column into a pandas object and converts to list
manhattan = list(df['Manhattan Bridge'])
wills = list(df['Williamsburg Bridge'])
queens = list(df['Queensboro Bridge'])
x_vars = [0]*210
for i in range(len(x_vars)):
    x_vars[i] = i+1

fig, axs = plt.subplots(2, 2)
fig.suptitle("Bike Data Across All Bridges")
axs[0, 0].plot(x_vars, brooklyn,'tab:orange', label="Brooklyn")
axs[0,0].set(xlim =(0,210), ylim=(0, 10000))
axs[0,0].legend(loc="upper left")


axs[0, 1].plot(x_vars, manhattan,'tab:green', label="Manhattan")
axs[0,1].set(xlim =(0,210), ylim=(0, 10000))
axs[0,1].legend(loc="upper left")


axs[1, 0].plot(x_vars, wills,'tab:blue', label="Williamsburg")
axs[1,0].set(xlim =(0,210), ylim=(0, 10000))
axs[1,0].legend(loc="upper left")


axs[1, 1].plot(x_vars, queens,'tab:red', label="Queensboro")
axs[1,1].set(xlim =(0,210), ylim=(0, 10000))
axs[1,1].legend(loc="upper left")


for ax in axs.flat:
    ax.set(xlabel='Day Number', ylabel='Num of Bikes')


brooklyn_hist = {};
for i in brooklyn:
    brooklyn_hist[i] = brooklyn_hist.get(i, 0) + 1

manhattan_hist = {};
for i in manhattan:
    manhattan_hist[i] = manhattan_hist.get(i, 0) + 1

wills_hist = {};
for i in wills:
    wills_hist[i] = wills_hist.get(i, 0) + 1

queens_hist = {};
for i in queens:
    queens_hist[i] = queens_hist.get(i, 0) + 1


b_edges = [0]*15
count = 0
for i in range(15):
    b_edges[i] = count
    count += 266

m_edges = [0]*15
count = 0
for i in range(15):
    m_edges[i] = count
    count+= 467

w_edges = [0]*15
count = 0
for i in range(15):
    w_edges[i] = count
    count+= 533

q_edges = [0]*15
count = 0
for i in range(15):
    q_edges[i] = count
    count+= 333

fig, axs = plt.subplots(2, 2)
fig.suptitle("Bridge Histograms")

axs[0,0].hist(df['Brooklyn Bridge'], b_edges,color="orange",label="Brooklyn")
axs[0,0].legend(loc="upper left")

axs[0,1].hist(df['Manhattan Bridge'], m_edges,color="green",label="Manhattan")
axs[0,1].legend(loc="upper left")

axs[1,0].hist(df['Williamsburg Bridge'], w_edges,label="Williamsburg")
axs[1,0].legend(loc="upper left")

axs[1,1].hist(df['Queensboro Bridge'], q_edges,color="red",label="Queensboro")
axs[1,1].legend(loc="upper left")

for ax in axs.flat:
    ax.set(xlabel='Num of Bikers', ylabel='Frequency')



print("Frequency Data: ")
print("************************************")
print("Brooklyn Mean: ",statistics.mean(brooklyn))
print("Brooklyn Min: ",min(brooklyn))
print("Brooklyn Max: ",max(brooklyn))
print("Brooklyn Difference: ",max(brooklyn)-min(brooklyn))
print("Brooklyn STDEV: ",statistics.stdev(brooklyn))
count = 0
for i in brooklyn:
    if i >= statistics.mean(brooklyn) - statistics.stdev(brooklyn) and i <= statistics.mean(brooklyn) + statistics.stdev(brooklyn):
        count = count + 1
print("Brooklyn Data within 1 STDEV: ", (count / len(brooklyn))*100)
count = 0
for i in brooklyn:
    if i >= statistics.mean(brooklyn) - 2 * statistics.stdev(brooklyn) and i <= statistics.mean(brooklyn) + 2 * statistics.stdev(brooklyn):
        count = count + 1
print("Brooklyn Data within 2 STDEV: ", (count / len(brooklyn))*100)

print("************************************")
print("Manhattan Mean: ",statistics.mean(manhattan))
print("Manhattan Min: ",min(manhattan))
print("Manhattan Max: ",max(manhattan))
print("Manhattan Difference: ",max(manhattan)-min(manhattan))
print("Manhattan STDEV: ",statistics.stdev(manhattan))
count = 0
for i in manhattan:
    if i >= statistics.mean(manhattan) - statistics.stdev(manhattan) and i <= statistics.mean(manhattan) + statistics.stdev(manhattan):
        count = count + 1
print("Manhattan Data within 1 STDEV: ", (count / len(manhattan))*100)
count = 0
for i in manhattan:
    if i >= statistics.mean(manhattan) - 2 * statistics.stdev(manhattan) and i <= statistics.mean(manhattan) + 2 * statistics.stdev(manhattan):
        count = count + 1
print("Manhattan Data within 2 STDEV: ", (count / len(manhattan))*100)

print("************************************")
print("Williamsburg Mean: ",statistics.mean(wills))
print("Williamsburg Min: ",min(wills))
print("Williamsburg Max: ",max(wills))
print("Williamsburg Difference: ",max(wills)-min(wills))
print("Williamsburg STDEV: ",statistics.stdev(wills))
count = 0
for i in wills:
    if i >= statistics.mean(wills) - statistics.stdev(wills) and i <= statistics.mean(wills) + statistics.stdev(wills):
        count = count + 1
print("Williamsburg Data within 1 STDEV: ", (count / len(wills))*100)
count = 0
for i in wills:
    if i >= statistics.mean(wills) - 2 * statistics.stdev(wills) and i <= statistics.mean(wills) + 2 * statistics.stdev(wills):
        count = count + 1
print("Williamsburg Data within 2 STDEV: ", (count / len(wills))*100)

print("************************************")
print("Queensboro Mean: ",statistics.mean(queens))
print("Queensboro Min: ",min(queens))
print("Queensboro Max: ",max(queens))
print("Queensboro Difference: ",max(queens)-min(queens))
print("Queensboro STDEV: ",statistics.stdev(queens))
count = 0
for i in wills:
    if i >= statistics.mean(queens) - statistics.stdev(queens) and i <= statistics.mean(queens) + statistics.stdev(queens):
        count = count + 1
print("Queensboro Data within 1 STDEV: ", (count / len(queens))*100)
count = 0
for i in queens:
    if i >= statistics.mean(queens) - 2 * statistics.stdev(queens) and i <= statistics.mean(queens) + 2 * statistics.stdev(queens):
        count = count + 1
print("Queensboro Data within 2 STDEV: ",(count / len(queens))*100)
plt.show()
