import numpy as np

data1 = np.array([10, 20, 30, 40, 50])
data2 = np.array([12, 24, 33, 47, 55])

mean_val = np.mean(data1)

median_val = np.median(data1)

std_dev = np.std(data1)

variance = np.var(data1)

correlation_matrix = np.corrcoef(data1, data2)
correlation_coefficient = correlation_matrix[0, 1]

print("Data:", data1)
print("Mean:", mean_val)
print("Median:", median_val)
print("Standard Deviation:", std_dev)
print("Variance:", variance)
print("Correlation Coefficient (data1 vs data2):", correlation_coefficient)
