import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

file = open("C:\\Users\\Yanga\\Datasets\\Vaccines.xlsx", "rb")
df = pd.read_excel(file)

plt.style.use("bmh")
plt.figure(figsize=(8,6))

df.set_index("Vaccine", inplace=True)
df_doses = df["Doses promised for 2021"]
df_prices = df["Price per dose"]


df_prices.plot(kind="barh")
plt.gca().invert_yaxis()


plt.title("Price of Covid Vaccines\n", fontsize="xx-large", weight="bold")
plt.ylabel("")
plt.xlabel("\nEstimated price per dose", fontsize="large")
plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80], ["USD", "$10", "$20", "$30", "$40", "$50", "$60", "$70", "$80"], fontsize="large")
plt.yticks(fontsize="large")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
