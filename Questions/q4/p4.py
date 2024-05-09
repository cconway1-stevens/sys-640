import os
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# Function to create directory if it doesn't exist
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Read data from file
with open("data.txt", "r") as file:
    data = file.read()
    data = np.array([int(num) for num in data.split()])

print("DATA SET\n\n", data, "\n\n")

# (a) Compute mean, median
mean = np.mean(data)
median = np.median(data)

# Find mode
unique_values, counts = np.unique(data, return_counts=True)
max_count = np.max(counts)
modes = unique_values[counts == max_count]

# (b) Calculate range, variance, and standard deviation
data_range = np.ptp(data)
variance = np.var(data, ddof=1)
std_dev = np.sqrt(variance)

# (c) Construct the intervals ±s, ±2s, ±3s
mean_std = mean + np.array([-1, 1]) * std_dev
mean_2std = mean + np.array([-2, 2]) * std_dev
mean_3std = mean + np.array([-3, 3]) * std_dev

# Count the number of observations in each interval
count_s = np.sum((data >= mean_std[0]) & (data <= mean_std[1]))
count_2s = np.sum((data >= mean_2std[0]) & (data <= mean_2std[1]))
count_3s = np.sum((data >= mean_3std[0]) & (data <= mean_3std[1]))

# Proportions for each interval
prop_s = count_s / len(data)
prop_2s = count_2s / len(data)
prop_3s = count_3s / len(data)

# Outliers detection based on ±3s
outliers = data[(data < mean_3std[0]) | (data > mean_3std[1])]

# (d) Box plot for the data
plt.boxplot(data, vert=False)
plt.title("Boxplot of Worker-Hours")
plt.xlabel("Worker-Hours")
plt_path = os.path.join("results", "boxplot.png")
create_directory("results")
plt.savefig(plt_path)
plt.close()

# (e) 70th percentile
percentile_70 = np.percentile(data, 70)
percentile_interpretation = f"70% of the recorded worker-hours are less than or equal to {percentile_70} hours."

# (f) Histogram of modes and their frequencies
plt.hist(modes, bins=len(modes))
plt.title("Histogram of Modes and Their Frequencies")
plt.xlabel("Mode")
plt.ylabel("Frequency")
plt_path = os.path.join("results", "modes_histogram.png")
plt.savefig(plt_path)
plt.close()

# Compile all results in a dictionary
results_dict = {
    "Mean": mean,
    "Median": median,
    "Modes": modes.tolist(),
    "Mode Frequencies": max_count,
    "Range": data_range,
    "Variance": variance,
    "Standard Deviation": std_dev,
    "±1 Standard Deviation": {
        "Interval": mean_std,
        "Count": count_s,
        "Proportion": prop_s
    },
    "±2 Standard Deviations": {
        "Interval": mean_2std,
        "Count": count_2s,
        "Proportion": prop_2s
    },
    "±3 Standard Deviations": {
        "Interval": mean_3std,
        "Count": count_3s,
        "Proportion": prop_3s
    },
    "Outliers": outliers,
    "70th Percentile": percentile_70,
    "Interpretation of 70th Percentile": percentile_interpretation
}

# Convert results to DataFrame
results_df = pd.DataFrame.from_dict(results_dict, orient='index')
results_df.columns = ['Value']

# Save results to CSV
results_csv_path = os.path.join("results", "results.csv")
results_df.to_csv(results_csv_path)

print(results_dict)
print("\nResults saved to:", results_csv_path)
