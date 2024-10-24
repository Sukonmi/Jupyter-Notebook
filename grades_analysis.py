# 1. Import the numpy library and create the "grades" array as specified above.
import numpy as np

grades = np.array([85, 90, 88, 92, 95, 80, 75, 98, 89, 83])
print(grades)

# 2. Use numpy functions to calculate the mean, median, and standard deviation of the grades.
# Mean
mean = np.mean(grades)
print(f"The mean is {mean}")

# Median
median = np.median(grades)
print(f"The median is {median}")

# Standard deviation
sd = round(np.std(grades), 3)
print(f"The standard deviation is {sd}")

# 3. Use numpy function to find the maximum and minimum of the grades.
# Maximum value
max_grade = np.max(grades)
print(f"The maximum grade is {max_grade}")

# Minimum value
min_grade = np.min(grades)
print(f"The minimum grade is {min_grade}")