import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

file = open("C:\\Users\\Yanga\\Datasets\\Vaccines.xlsx", "rb")
df = pd.read_excel(file)

plt.style.use("bmh")
plt.figure(figsize=(8, 6))

df.set_index("Vaccine", inplace=True)
df_doses = df["Doses promised for 2021"]
df_prices = df["Price per dose"]

df_doses.plot(kind="barh")
plt.gca().invert_yaxis()


plt.title("Covid Vaccines Planned for Delivery in 2021\n", fontsize="xx-large", weight="bold")
plt.xlabel("\nNumber of Doses", fontsize="large")
plt.ylabel("")
plt.xticks([500_000_000, 1_000_000_000, 1_500_000_000, 2_000_000_000, 2_500_000_000, 3_000_000_000], ["0.5 billion", "1 billion", "1.5 billion", "2 billion", "2.5 billion", "3 billion"], fontsize="large")
plt.yticks(fontsize="large")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
