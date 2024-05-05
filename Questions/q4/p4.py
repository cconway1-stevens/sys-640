# Question 4.
# Industrial engineers periodically conduct “work measurement” analyses to determine the time required to produce a single unit of output. At a large processing plant, the number of total worker-hours required per day to perform a certain task was recorded for 50 days. The data are shown below:
# 128 119 95 97 124 128 142 98 108 120
# 113 109 124 132 97 138 133 136 120 112
# 146 128 103 135 114 109 100 111 131 113
# 124 131 133 131 88 118 116 98 112 138
# 100 112 11 150 117 122 97 116 92 122
# (a) Compute the mean, median, and the mode of the data set.
# (b) Find the range, variance, and standard deviation of the data set.
# (c) Construct the intervals ± s, ± 2s, and ± 3s. Count the number of observations that fall within each interval and find the corresponding proportions. Do you detect any outliers?
# (d) Construct a box plot for the data. Do you detect any outliers?
# (e) Find the 70th percentile for the data on total daily worker-ho



import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Data
worker_hours = [
    128, 119, 95, 97, 124, 128, 142, 98, 108, 120, 113, 109, 124, 132, 97, 138, 133, 136, 120, 112,
    146, 128, 103, 135, 114, 109, 100, 111, 131, 113, 124, 131, 133, 131, 88, 118, 116, 98, 112, 138,
    100, 112, 11, 150, 117, 122, 97, 116, 92, 122
]

# Part (a): Mean, Median, Mode
mean = np.mean(worker_hours)
median = np.median(worker_hours)
mode = stats.mode(worker_hours)
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")

# Part (b): Range, Variance, Standard Deviation

range_ = np.ptp(worker_hours)
variance = np.var(worker_hours)
std_dev = np.std(worker_hours)

print(f"Range: {range_}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_dev}")

# Part (c): Intervals ± s, ± 2s, ± 3s

s = std_dev
s_2 = 2 * std_dev
s_3 = 3 * std_dev

intervals = [s, s_2, s_3]
intervals_data = []

for interval in intervals:
    data = [x for x in worker_hours if mean - interval <= x <= mean + interval]
    intervals_data.append(data)

for i, data in enumerate(intervals_data):
    print(f"Number of observations within ± {i + 1}s: {len(data)}")
    print(f"Proportion of observations within ± {i + 1}s: {len(data) / len(worker_hours)}")

# Part (d): Box Plot

plt.boxplot(worker_hours)
plt.title("Box Plot of Worker Hours")
plt.show()
# SAVE PLOT 
plt.savefig('box_plot.png')

# Part (e): 70th Percentile

percentile_70 = np.percentile(worker_hours, 70)
print(f"70th Percentile: {percentile_70}")

# Results 

# Mean: 115.82
# Median: 117.5
# Mode: ModeResult(mode=97, count=3)
# Range: 139
# Variance: 444.10760000000005
# Standard Deviation: 21.073860586043555
# Number of observations within ± 1s: 42
# Proportion of observations within ± 1s: 0.84
# Number of observations within ± 2s: 49
# Proportion of observations within ± 2s: 0.98
# Number of observations within ± 3s: 49
# Proportion of observations within ± 3s: 0.98
# 70th Percentile: 128.0