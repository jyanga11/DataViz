import pandas as pd
import matplotlib.pyplot as plt

file = open("C:\\Users\\Yanga\\Datasets\\refugees_displaced.xlsx", "rb")
df = pd.read_excel(file)

plt.style.use("fivethirtyeight")

countries = []
for country in df["Country"]:
    countries.append(country)

values = []
for num in df["Displaced"]:
    values.append(num)

labels = ["6.6m", "3.7m", "2.7m", "2.2m", "1.1m"]

df.set_index("Country", inplace=True)


df.plot(kind="barh", legend=None, color="#ff3333")
plt.gca().invert_yaxis()

plt.title("Displaced Refugees", fontsize="large", weight="bold")
plt.yticks(weight="bold", fontsize="small")
#plt.xticks([1_000_000, 2_000_000, 3_000_000, 4_000_000, 5_000_000, 6_000_000],
#           ["1 million", "2 million", "3 million", "4 million", "5 million", "6 million"])
plt.xticks([], [])
plt.xlabel("")
plt.ylabel("")

for index, value in enumerate(values):
    plt.text(value-1_000_000, index+0.05, labels[index],
             color="white", weight="bold", fontsize="medium")

plt.grid(None)

plt.tight_layout()
plt.show()
