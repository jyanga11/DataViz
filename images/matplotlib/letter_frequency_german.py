import pandas as pd
import matplotlib.pyplot as plt

file = open("C:\\Users\\Yanga\\Datasets\\letter_frequency_latin.xlsx", "rb")
df = pd.read_excel(file)

df.set_index("Letter", inplace=True)

df_eng = df["English"]
df_fre = df["French"]
df_spa = df["Spanish"]
df_ger = df["German"]


plt.figure(figsize=(8,6))
df_ger.plot(kind="bar", color="#03d100")

plt.title("Letter Frequency in German", fontsize="xx-large", weight="bold")
plt.xticks(rotation="horizontal", fontsize="large", weight="bold")
plt.yticks([0.02, 0.04, 0.06, 0.08, 0.10, 0.12, 0.14, 0.16],
           ["2%", "4%", "6%", "8%", "10%", "12%", "14%", "16%"])
plt.xlabel("")
plt.ylabel("Frequency", fontsize="large")

plt.show()
