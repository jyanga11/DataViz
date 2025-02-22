import pandas as pd
import matplotlib.pyplot as plt

file = open("C:\\Users\\Yanga\\Datasets\\letter_frequency_arabic.csv", errors="ignore")
df = pd.read_csv(file)

for num in df["Frequency"]:
    num = float(num)


df.plot(kind="bar", color="#03d100", figsize=(10,8), legend=None)

plt.title("Letter Frequency in Arabic", fontsize="xx-large", weight="bold")

plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
            17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32],
            ["ء", "ؤ", "ئ", "ا", "ب", "ة", "ت", "ث", "ج", "ح", "خ", "د", "ذ", "ر", "ز", "س",
             "ش", "ص", "ض", "ط", "ظ", "ع", "غ", "ف", "ق", "ك", "ل", "م", "ن", "ه", "و", "ى", "ي"],
           rotation="horizontal", fontsize="x-large", weight="bold")
plt.yticks([2, 4, 6, 8, 10, 12, 14, 16],
           ["2%", "4%", "6%", "8%", "10%", "12%", "14%", "16%"])

plt.xlabel("")
plt.ylabel("Frequency", fontsize="large")


plt.tight_layout()
plt.show()
