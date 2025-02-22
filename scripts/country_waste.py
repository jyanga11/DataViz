import matplotlib.pyplot as plt
import pandas as pd

file = open("../data/country_waste.csv")
df = pd.read_csv(file)

df_waste = df[['country_name', ]]

print(df.head(5))
