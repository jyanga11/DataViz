import pandas as pd
import matplotlib.pyplot as plt

file = open("C:\\Users\\Yanga\\Datasets\\NBA Field goal attempts per game.xlsx", "rb")


plt.style.use('Solarize_Light2')

df = pd.read_excel(file)
df.set_index("Player", inplace=True)
df.plot(kind="barh", legend=None)
plt.gca().invert_yaxis()


plt.title("NBA All-Time Most Field Goal Attempts\n", fontsize="xx-large")
plt.xlabel("Career FGA")
plt.ylabel("")
plt.xticks([0, 5000, 10000, 15000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000, 30000],
           ["0", "5,000", "10,000", "15,000", "20,000", "21,000", "22,000", "23,000", "24,000", "25,000",
           "26,000", "27,000", "28,000", "29,000", "30,000"])


plt.show()
