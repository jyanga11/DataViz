import pandas as pd
import matplotlib.pyplot as plt


file = open("C:\\Users\\Yanga\\Datasets\\independent_project.xlsx", "rb")
df = pd.read_excel(file)

plt.style.use("fivethirtyeight")

countries = []
for country in df["Country"]:
    countries.append(country)

prices = []
for num in df["Price of Cigarettes"]:
    prices.append(num)

labels = ["$26.65", "$22.82", "$16.50", "$15.11", "$14.93",
          "$12.22", "$11.68", "$11.37", "$10.86"]


df.set_index("Country", inplace=True)
df = df["Price of Cigarettes"]


plt.figure(figsize=(8,6))
df.plot(kind="barh", color="purple")
plt.gca().invert_yaxis()

for index, value in enumerate(prices):
    plt.text(value-4.7, index+0.15, labels[index],
             color="white", weight="bold", fontsize="large")

plt.title("Average Price of Cigarettes\n", fontsize="xx-large", weight="bold")
plt.ylabel("")
plt.xticks([], [])
plt.yticks(weight="bold")


plt.grid(None)
plt.tight_layout()
plt.show()
