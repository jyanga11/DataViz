import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

file1 = open("C:\\Users\\Yanga\\Datasets\\life-expectancy.csv") #Life expectancy
file2 = open("C:\\Users\\Yanga\\Datasets\\average-real-gdp-per-capita-across-countries-and-regions.csv") #GDP per capita
file3 = open("C:\\Users\\Yanga\\Datasets\\economic-inequality-gini-index.csv") #GINI coefficient

df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)
df3 = pd.read_csv(file3)

df1.set_index("Year", inplace=True)
df1 = df1.loc[2015]
df1.set_index("Entity", inplace=True)
life_expectancy = df1["Life expectancy"]

df2.set_index("Year", inplace=True)
df2 = df2.loc[2015]
df2.set_index("Entity", inplace=True)
gdp_per_capita = df2["Real GDP per capita in 2011US$, multiple benchmarks (Maddison Project Database (2018))"]

df3.set_index("Year", inplace=True)
df3 = df3.loc[2010]
df3.set_index("Entity", inplace=True)
gini_coefficient = df3["GINI index (World Bank estimate)"]


#plt.scatter(life_expectancy, gdp_per_capita)


#plt.show()
