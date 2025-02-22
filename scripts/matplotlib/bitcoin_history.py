import pandas as pd
import matplotlib.pyplot as plt

file = open("C:\\Users\\Yanga\\Datasets\\BTC-USD.csv", "rb")
df = pd.read_csv(file)

plt.style.use("fivethirtyeight")

df.set_index("Date", inplace=True)
df = df["High"]


plt.figure(figsize=(8,8))
df.plot(kind="line")

plt.title("Bitcoin Price", fontsize="xx-large", weight="bold")
plt.xticks(rotation=30, weight="bold", fontsize="small")
plt.yticks([5_000, 10_000, 15_000, 20_000, 25_000, 30_000, 35_000, 40_000],
           ["", "$10,000", "", "$20,000", "", "$30,000", "", "$40,000"],
           fontsize="small")

plt.xlabel("")
plt.ylabel("")

plt.grid(b=True, which="both")
plt.tight_layout()
plt.show()
