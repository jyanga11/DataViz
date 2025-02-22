import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

file = open("C:\\Users\\Yanga\\Datasets\\incarceration_rates.xlsx", "rb")
df = pd.read_excel(file)

df.set_index("Country", inplace=True)

plt.style.use("dark_background")

plt.figure(figsize=(8,8))
df.plot(kind="barh", legend=None, color="red")

plt.gca().invert_yaxis()
plt.title("Highest Incarceration Rates", weight="bold", fontsize="xx-large")
plt.xlabel("\nPrisoners per 100,000 citizens", fontsize="large")
plt.ylabel("")
plt.xticks()
plt.yticks(fontsize="large")
plt.grid(alpha=0.2)

plt.tight_layout()
plt.show()
