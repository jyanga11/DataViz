import pandas as pd
import matplotlib.pyplot as plt

file = open("C:\\Users\\Yanga\\Datasets\\Megaregions.xlsx", "rb")
df = pd.read_excel(file)
df.set_index("City Cluster", inplace=True)
df.sort_values(by="Population", ascending=False, axis=0, inplace=True)

df_populations = df["Population"]
df_populations = df_populations.head(15)

plt.style.use("ggplot")
plt.figure(figsize=(8,6))
df_populations.plot(kind="barh", color="#00d419")
plt.gca().invert_yaxis()

plt.title("Major City Clusters\n", fontsize="xx-large", weight="bold")
plt.ylabel("")
plt.xlabel("Population in millions", fontsize="large")
plt.xticks([20_000_000, 40_000_000, 60_000_000, 80_000_000, 100_000_000, 120_000_000, 140_000_000],
           ["20", "40", "60", "80", "100", "120", "140"], fontsize="large")
plt.yticks(weight="bold", fontsize="large")

plt.tight_layout()
plt.show()
