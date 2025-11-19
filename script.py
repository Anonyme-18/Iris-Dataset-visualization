import pandas as pd
import matplotlib.pyplot as plt

# Chargging dataset
df = pd.read_csv("iris.csv")

# Calculate stats
stats_mean = df.groupby("species").mean(numeric_only=True)
stats_max = df.groupby("species").max(numeric_only=True)
stats_min = df.groupby("species").min(numeric_only=True)

# Variables
variables = ["sepal_width", "sepal_length", "petal_length", "petal_width"]

# Creation of dashboard
plt.figure(figsize=(18, 18))
plot_number = 1

#moyennes
for var in variables:
    plt.subplot(4, 3, plot_number)
    plt.title(f"Moyennes de {var} par espèce")
    plt.bar(stats_mean.index, stats_mean[var])
    plt.xlabel("")
    plt.ylabel("Moyenne")
    plot_number += 1

#Maximum
for var in variables:
    plt.subplot(4, 3, plot_number)
    plt.title(f"Max de {var} par espèce")
    plt.bar(stats_max.index, stats_max[var])
    plt.xlabel("")
    plt.ylabel("Maximum")
    plot_number += 1

#Minimum
for var in variables:
    plt.subplot(4, 3, plot_number)
    plt.title(f"Min de {var} par espèce")
    plt.bar(stats_min.index, stats_min[var])
    plt.xlabel("")
    plt.ylabel("Minimum")
    plot_number += 1

plt.tight_layout()
plt.show()
