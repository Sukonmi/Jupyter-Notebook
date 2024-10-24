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

# 4. Use numpy function to sort the grades in ascending order.
sorted_grades = np.sort(grades)
print(f"The sorted grades are: {sorted_grades}")

# 5. Use numpy function to find the index of the highest grade in the array.
hg_index = np.where(grades == max_grade)
print(f"The index for the highest grade is {hg_index}")

# 6. Use numpy function to count the number of students who scored above 90.
grade_count90 = np.count_nonzero(grades > 90)
print(f"The number of students who scored above 90: {grade_count90} students.")

# 7. Use numpy function to calculate the percentage of students who scored above 90.
total = np.sum(grades)
grade90 = np.sum(grades[np.where(grades > 90)])
percentage1 = round((grade90 / total) * 100)
print(f"The percentage of students that scored above 90 is {percentage1}%")

# 8. Use numpy function to calculate the percentage of students who scored below 75.
grade75 = np.sum(grades[np.where(grades < 75)])
percentage2 = (grade75 / total) * 100
print(f"The percentage of studets that scored below 75 is {percentage2}%")

# 9. Use numpy function to extract all the grades above 90 and put them in a new array called "high_performers".
high_performers = grades[grades > 90]
print(high_performers)

# 10. Create a new array called "passing_grades" that contains all the grades above 75.
passing_grades = grades[grades > 75]
print(passing_grades)