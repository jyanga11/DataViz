import pandas as pd
import matplotlib.pyplot as plt

file = open("C:\\Users\\Yanga\\Datasets\\population_country.csv")
df = pd.read_csv(file)
df.set_index("Country", inplace=True)
plt.style.use("seaborn-darkgrid")
plt.figure(figsize=(10, 10))

india = df.loc['India']
china = df.loc['China']
nigeria = df.loc['Nigeria']
united_states = df.loc['United States']
indonesia = df.loc['Indonesia']
brazil = df.loc['Brazil']

india.plot(kind="line", linewidth=3, color="#ff0000")
china.plot(kind="line", linewidth=3, color="orange")
nigeria.plot(kind="line", linewidth=3, color="#00d600")
united_states.plot(kind="line", linewidth=3, color="#00eeff")
indonesia.plot(kind="line", linewidth=3, color="#9d00bd")
brazil.plot(kind="line", linewidth=3, color="#0015ff")


plt.title("Projected Populations by 2050\n", fontsize="xx-large", weight="bold")
plt.legend(fontsize="medium", loc=2)
plt.xticks([0, 2, 4, 6, 8, 10, 12, 14, 16], ["1970", "1980", "1990", "2000", "2010", "2020", "2030", "2040", "2050"], rotation="horizontal", fontsize="x-large")
plt.yticks([250, 500, 750, 1000, 1250, 1500, 1750], ["250 million", "500 million", "750 million", "1 billion", "1.25 billion", "1.5 billion", "1.75 billion"])
plt.ylabel("")
plt.plot([10, 10], [20, 1760], color="black", linestyle=":", linewidth=1, alpha=0.8)
plt.show()
