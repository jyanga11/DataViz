import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import math

file = open("C:\\Users\\Yanga\\Datasets\\meat-consumption-vs-gdp-per-capita.csv")
df = pd.read_csv(file)

plt.style.use("ggplot")

df.drop(["Code"], axis=1, inplace=True)


df.rename(columns={"Entity" : "Country",
                   "Meat food supply quantity (kg/capita/yr) (FAO, 2020)" : "Meat Consumption (kg/capita/yr)",
                   "Total population (Gapminder, HYDE & UN)" : "Population",
                   "GDP per capita, PPP (constant 2011 international $)" : "GDP per capita"
                   }, inplace=True)

df.set_index("Year", inplace=True)

df2 = df.loc[2017]
df2.set_index("Country", inplace=True)

df2.drop(["World", "Upper middle income", "Sub-Saharan Africa (excluding high income)", "Sub-Saharan Africa (IDA & IBRD)",
         "Sub-Saharan Africa", "South Asia (IDA & IBRD)", "South Asia", "Small states", "Pre-demographic dividend", "Post-demographic dividend",
         "Other small states", "Pacific island small states", "Oceania", "OECD members", "Middle income", "Middle East & North Africa (excluding high income)",
         "Middle East & North Africa (IDA & IBRD)", "Middle East & North Africa", "Low income", "Lower middle income", "Low & middle income", "Least developed countries: UN classification",
         "Latin America & Caribbean (excluding high income)", "Latin America & Caribbean (IDA & IBRD)", "Latin America & Caribbean", "Latin America",
         "Late-demographic dividend", "IDA only", "IDA total", "IDA blend", "IDA & IBRD total", "IBRD only", "High income", "Heavily indebted poor countries (HIPC)",
         "Fragile and conflict affected situations", "European Union", "Europe & Central Asia (excluding high income)", "Europe & Central Asia (IDA & IBRD)",
         "Europe & Central Asia", "Europe", "Euro area", "East Asia & Pacific (excluding high income)", "East Asia & Pacific", "East Asia & Pacific (IDA & IBRD)",
         "Early-demographic dividend", "Central Europe and the Baltics", "Caribbean small states", "Africa", "Asia", "Arab World", "North America"
         ], axis=0, inplace=True)

gdp = df2["GDP per capita"]
meat_consumption = df2["Meat Consumption (kg/capita/yr)"]
population = []
Populations = df2["Population"]
for num in Populations:
    if num > 1_000_000_000:
        population.append(5000)
    elif 200_000_000 < num < 1_000_000_000:
        population.append(700)
    elif 80_000_000 < num < 200_000_000:
        population.append(400)
    elif 30_000_000 < num < 80_000_000:
        population.append(40)
    elif 5_000_000 < num < 30_000_000:
        population.append(30)
    elif 900_000 < num < 5_000_000:
        population.append(200)
    else:
        population.append(10)

scatter = plt.scatter(gdp, meat_consumption, s=population,
            edgecolor='black', linewidth=1, alpha=0.9)

plt.xscale("log")


plt.title("Meat Consumption versus GDP\n", fontsize="xx-large")
plt.grid(which="both", axis="y")
plt.ylabel("Meat Consumption\nkg/capita/yr", fontsize="large")
plt.xlabel("\nGDP per capita (log)", fontsize="large")
plt.xticks([10**3, 10**4, 10**5], ["$1,000", "$10,000", "$100,000"])

plt.annotate("India", xy=(6_700, 4), fontsize="small", color="black")
plt.annotate("China", xy=(10_500, 65), fontsize="small", color="black")
plt.annotate("US", xy=(50_000, 123), fontsize="small", color="black")
plt.annotate("Ethiopia", xy=(1_750, 1), fontsize="small", color="black")
plt.annotate("Brazil", xy=(12_000, 98), fontsize="small", color="black")


plt.tight_layout()
plt.show()
