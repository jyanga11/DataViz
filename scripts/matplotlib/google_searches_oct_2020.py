import matplotlib.pyplot as plt

file = open("../data/relatedQueries.csv")
file.seek(0)

google_searches = []
popularity_scores = []

file.readline()
file.readline()

for line in file:
    line = line.strip().split(",")

    google_searches.append(line[0])
    popularity_scores.append(int(line[1]))

    if len(google_searches) == 25:
        break

file.close()

plt.bar(google_searches, popularity_scores)

plt.title("Most Popular Google Searches of October")
plt.xlabel("Search Query")
plt.ylabel("Popularity Score (0-100)")
plt.xticks(rotation=90)

plt.show()
