import pandas as pd
import matplotlib.pyplot as plt

file = open("C:\\Users\\Yanga\\Datasets\\cigarette-consumption-map.csv", "rb")
df = pd.read_csv(file)

df.set_index("COUNTRY", inplace=True)
df = df["Cigarette consumption"]


plt.figure(figsize=(8,6))
df.head(10).plot(kind="barh", color="purple", alpha=1)
plt.gca().invert_yaxis()

plt.title("Cigarette Consumption", fontsize="xx-large", weight="bold")
plt.xlabel("Cigarettes consumption per capita")
plt.ylabel("")
plt.xticks(fontsize="large")
plt.yticks(fontsize="large")

plt.grid(alpha=0.2)
plt.tight_layout()
plt.show()
