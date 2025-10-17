"""
Draw the histogram of the following data (Height of student vs. No. of students)
"""
import matplotlib.pyplot as plt
heights = [135, 140, 145, 150, 155]
students = [4, 12, 16, 8]
l=[137.5] * 4 + [142.5] * 12 + [147.5] * 16 + [152.5] * 8
print(l)
heights = [(heights[i] + heights[i + 1]) / 2 for i in range(len(heights) - 1)]
plt.hist([137.5] * 4 + [142.5] * 12 + [147.5] * 16 + [152.5] * 8,bins=heights)
plt.show()
