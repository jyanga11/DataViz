import matplotlib.pyplot as plt

# Initialize events and corresponding dates
events = ["Event 1", "Event 2", "Event 3", "Event 4", "Event 5"]
dates = [2000, 2010, 2020, 2030, 2040]
levels = [1, -1, 1, -1, 1] # Choose nice y axis levels to display each event


# Create stem plot
fig, ax = plt.subplots(figsize=(10,4), constrained_layout=True)

# Title plot
plt.title("Timeline Title")

# Set markerline at each date, corresponding to y value in levels
# Set the baseline at y value 0
markerline, stemline, baseline = plt.stem(dates, levels, bottom=0)

# Label each event
for i in range(0, len(events)):
    plt.annotate(events[i], (dates[i], levels[i]))

# Make y axis invisible
ax.get_yaxis().set_visible(False)
for spine in ["left", "top", "right"]:
    ax.spines[spine].set_visible(False)

plt.xticks(rotation=30, fontsize="large")

plt.show()
