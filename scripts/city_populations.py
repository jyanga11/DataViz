import matplotlib.pyplot as plt

file = open("../data/worldcities.csv", encoding="latin-1")

file.seek(0)

cities = []
countries = []
populations = []

header = file.readline().strip().replace("\"", "").split(",")

for line in file:
    line = line.strip().replace("\"", "")
    line = line.split(",")

    cities.append(line[0])
    countries.append(line[4])
    populations.append((line[9]))


for num in range(25799):
    try:
        #print(num)
        populations[num] = int(populations[num])
    except ValueError:
        populations.remove(populations[num])
        countries.remove(countries[num])
        cities.remove(cities[num])


import matplotlib.pyplot as plt

plt.bar(cities, populations)


plt.show()
