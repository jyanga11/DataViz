import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

file = open("../data/Data Income Mountains  - v2 - by Gapminder - 20180504___2.xlsx", "rb")

xls = pd.ExcelFile(file)
df = pd.read_excel(xls, "Data regions by year")
df = df.drop(columns=["geo", "Extreme poverty rate", "Total", "Share of people on Level 1", "Share of people on Level 2", "Share of people on Level 3",
                        "Share of people on Level 4", "Share of people on Level 5", "Unnamed: 12", "Share of people on Level 4 or above", "Unnamed: 14",
                        "Unnamed: 4", "Unnamed: 15", "People in extreme poverty count'", "Unnamed: 17", "population"])
df = df.iloc[:, :7]
df.set_index("year", inplace=True)


df_1995 = df.loc[1995]
df_2019 = df.loc[2019]

df_1970 = df.loc[1970]
df_1970 = df_1970.reset_index()
df_1970 = df_1970.iloc[:, 1:]
df_1970 = df_1970.transpose()


plt.stackplot(df_1970.columns.values, df_1970.index.values)
plt.show()
