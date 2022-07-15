import matplotlib.pyplot as plt
import pandas as pd
df =  pd.read_csv('BEDDATA.csv')
seekingProgram_data = df["Seeking Bos Equity Program"]

yesCount = 0;
noCount = 0;


for x in seekingProgram_data:
	if x == "Yes":
		yesCount = yesCount + 1;
		
	elif x == "No":
		noCount = noCount + 1;

total = yesCount + noCount;
		
labels = 'Seeking: '+ str(yesCount), 'Not Seeking: ' + str(noCount)
sizes = [yesCount, noCount]
colors = ["Green","Red"]
explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'No')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, colors=colors, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title("Boston Cannabis Facility Registry June 2021 - July 2022: \n" + "Dispensaries Seeking Boston Equity Program", fontsize=12, bbox={'facecolor':'green', "alpha":0.3, 'pad':5})

plt.figtext(0.5, 0.075,"Total Dispensaries: "+ str(total), ha="center", fontsize=10, bbox={"facecolor":"green", "alpha":0.3, "pad":5})



plt.figtext(0.5, 0.01,"Data Source: https://data.boston.gov/dataset/cannabis-registry/resource/5de268d6-e3a5-4f5c-b43a-0d293b377b50", ha="center", fontsize=10, bbox={"facecolor":"green", "alpha":0.3, "pad":5})






plt.show()