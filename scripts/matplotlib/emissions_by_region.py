import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

file = open("C:\\Users\\Yanga\\Datasets\\annual-co-emissions-by-region.csv", "rb")
df = pd.read_csv(file)

#plt.style.use("classic")

df.set_index("Entity", inplace=True)

years = list(range(1850,2019))

df_africa = df.loc["Africa"]
df_africa = df_africa["Annual CO2 emissions"]
df_africa = df_africa.tail(169)

df_asia = df.loc["Asia"]
df_asia = df_asia["Annual CO2 emissions"]
df_asia = df_asia.tail(169)

df_europe = df.loc["Europe"]
df_europe = df_europe["Annual CO2 emissions"]
df_europe = df_europe.tail(169)

df_north_america = df.loc["North America"]
df_north_america = df_north_america["Annual CO2 emissions"]
df_north_america = df_north_america.tail(169)

df_south_america = df.loc["South America"]
df_south_america = df_south_america["Annual CO2 emissions"]
df_south_america = df_south_america.tail(169)

regions = [df_asia, df_europe, df_north_america, df_africa, df_south_america]
labels = ["Asia", "Europe", "North America", "Africa", "South America"]

plt.figure(figsize=(8,6))
plt.stackplot(years, df_asia, df_europe, df_north_america, df_africa, df_south_america, labels=labels)

plt.title("Annual CO2 Emissions by Region", fontsize="xx-large", weight="bold")
plt.legend(loc="upper left", fontsize="large")
plt.yticks([5000, 10_000, 15_000, 20_000, 25_000, 30_000, 35_000],
           ["5b tons", "10b tons", "15b tons", "20b tons",
           "25b tons", "30b tons", "35b tons"], fontsize="medium")
plt.xticks(fontsize="large")

plt.show()
