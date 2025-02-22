import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

file = open("C:\\Users\\Yanga\\Datasets\\annual_global_temp.csv")
df = pd.read_csv(file)

plt.style.use("seaborn")

df.set_index("Source", inplace=True)
df = df.loc["GISTEMP"]
df.set_index("Year", inplace=True)


df.plot(kind="line", legend=None, linewidth=2)
plt.plot([2016, 2016], [-0.55, 4], color="black", linestyle="--", linewidth=1, alpha=0.6)
plt.plot([1875, 2100], [2.0, 2.0], color="red", linestyle="--", linewidth=1)
#plt.plot([2016, 2100], [0.999, 1.85], color="#ffc400", linestyle="-", linewidth=1)
#plt.plot([2016, 2090], [0.999, 4], color="#ff7700", linestyle="-", linewidth=1)
#plt.plot([2016, 2036], [0.999, 4], color="#ff2600", linestyle="-", linewidth=1)


plt.title("Global Warming", fontsize="xx-large", weight="bold")
plt.xlabel("")
plt.ylabel("Temperature Anomaly since 1880")
plt.show()
