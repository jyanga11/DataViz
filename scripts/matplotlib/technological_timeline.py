import matplotlib.pyplot as plt

#plt.style.use("fivethirtyeight")

# Initialize events and corresponding dates
events = ["Isolation", "Comparative Advantage", "Economic Union", "Monetary Union"]
dates = []
levels = [1, -1, 2, -1,
          1, -2, 1.75, -1.5, 2.2, -1.25,
          1, -1.75, 1.8, -1] # Choose nice y axis levels to display each event


# Create stem plot
fig, ax = plt.subplots(figsize=(10,5), tight_layout=True)

# Title plot
plt.title("\nAccelerating Technological Breakthroughs", fontsize="large")

# Set markerline at each date, corresponding to y value in levels
# Set the baseline at y value 0
markerline, stemline, baseline = plt.stem(dates, levels, bottom=0)
markerline.set_markerfacecolor("red")
stemline.set_color("gray")
baseline.set_color("blue")

plt.setp(stemline, "linewidth", 1, alpha=0.4)
plt.setp(baseline, "linewidth", 2)
plt.grid(None)

# Label each event
for i in range(0, len(events)):
    plt.annotate(events[i], (dates[i]+4, levels[i]), weight="bold", fontsize="xx-small")

# Make y axis invisible
ax.get_yaxis().set_visible(False)
for spine in ["left", "top", "right"]:
    ax.spines[spine].set_visible(False)

plt.xticks(fontsize="small")
ax.tick_params(axis="x", direction="in", pad=-140)

plt.show()
print("Hello")
