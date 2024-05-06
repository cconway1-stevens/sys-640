# Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Given data
data = [128, 119, 95, 97, 124, 128, 142, 98, 108, 120,
        113, 109, 124, 132, 97, 138, 133, 136, 120, 112,
        146, 128, 103, 135, 114, 109, 100, 111, 131, 113,
        124, 131, 133, 131, 88, 118, 116, 98, 112, 138,
        100, 112, 11, 150, 117, 122, 97, 116, 92, 122]

# (a) Compute the mean, median, and mode
mean = np.mean(data)
median = np.median(data)
mode = np.argmax(np.bincount(data))

print("Part A:----------------")
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)

# (b) Find the range, variance, and standard deviation
range_data = np.ptp(data)
variance = np.var(data)
std_deviation = np.std(data)
print("Part B:----------------")
print("\nRange:", range_data)
print("Variance:", variance)
print("Standard Deviation:", std_deviation)

# (c) Construct intervals ± s, ± 2s, and ± 3s
s = np.std(data)
intervals = [s, 2*s, 3*s]
count_within_intervals = [np.sum((data >= mean - interval) & (data <= mean + interval)) for interval in intervals]
proportions_within_intervals = [count / len(data) for count in count_within_intervals]
print("Part C:----------------")
print("\nCount within intervals ± s, ± 2s, and ± 3s:", count_within_intervals)
print("Proportions within intervals ± s, ± 2s, and ± 3s:", proportions_within_intervals)

# Detecting outliers
outliers = [obs for obs in data if obs < mean - 3 * s or obs > mean + 3 * s]
print("\nOutliers:", outliers)



# (d) Construct a box plot to detect outliers
print("Part D:----------------")
plt.figure(figsize=(10, 6))
sns.boxplot(data)
plt.title('Box plot of daily worker-hours')
plt.xlabel('Daily Worker-Hours')
plt.grid(True)
plt.show()
#save plot to q4 folder
plt.savefig('Questions/q4/q4.png')
print("Box plot saved in the Questions/q4 folder @", './Questions/q4/q4.png')
# Detecting outliers
outliers = [obs for obs in data if obs < mean - 3 * s or obs > mean + 3 * s]
print("\nOutliers:", outliers)

# (e) Find the 70th percentile
print("Part E:----------------")
percentile_70 = np.percentile(data, 70)
print("\n70th percentile for the data on total daily worker-hours:", percentile_70)
