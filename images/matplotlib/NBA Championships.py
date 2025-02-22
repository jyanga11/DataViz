import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

file = open("C:\\Users\\Yanga\\Datasets\\NBA Franchise Championships.xlsx", "rb")

df = pd.read_excel(file)

plt.style.use('Solarize_Light2')

df_top_five = df[:5]

other = pd.DataFrame(data = {
    'Franchise' : ['Other'],
    'Championships' : [df['Championships'][5:].sum()]
})

df_top_five = pd.concat([df_top_five, other])

df_top_five.set_index("Franchise", inplace=True)


pie = df_top_five["Championships"].plot(kind="pie", subplots=True,
                                  colors=["gold", "green", "red", "blue", "gray", "lightgray"])


plt.title("\nNBA Franchise Championships\n", fontsize="xx-large")
plt.ylabel("")

plt.show()
