import pandas as pd
import matplotlib.pyplot as plt

file = open("C:\\Users\\Yanga\\Datasets\\Electricity generation by source - World.csv")
df = pd.read_csv(file)

plt.style.use("seaborn-bright")

sources = [df["Coal"], df["Natural gas"], df["Hydro"], df["Oil"], df["Wind"], df["Solar"]]
labels = ["Coal", "Gas", "Hydro", "Oil", "Wind", "Solar"]


plt.figure(figsize=(8,6))
plt.stackplot(df["Year"], sources, labels=labels)
plt.legend(loc="upper left")

plt.title("Electricity Production by Source", fontsize="xx-large", weight="bold")
plt.xticks(fontsize="large")
plt.yticks([5_000_000, 10_000_000, 15_000_000, 20_000_000, 25_000_000],
           ["5 million", "10 million", "15 million", "20 million", "25 million"],
           fontsize="medium")

plt.xlabel("")
plt.ylabel("Gigawatt Hours (GWh)", fontsize="large")

plt.tight_layout()
plt.show()
