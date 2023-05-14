import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = '../data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #Get high temperatures from this file.
    dates, highs =[], [] #1
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d') #2
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)


#Plot the high temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red') #3

#Format plot.
plt.title("Daily high temperatures - 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate() #4
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
plt.show()

