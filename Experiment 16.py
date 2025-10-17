"""
Calculate the S.D. and coefficient of variation (C. V.) for the following table:
Class:
[0-10 10-20 20-30 30-40 40-50 50-60 60-70 70-80]
[5,15,25,35,45,55,65,75]
Frequency:
[5,10,20,40,30,20,10,5]
"""
mid_points=[5,15,25,35,45,55,65,75]
frequency=[5,10,20,40,30,20,10,5]
mean=0
for i in range(len(mid_points)):
    mean+=frequency[i]*mid_points[i]
mean=mean/sum(frequency)
print(mean)
variance=0
for i in range(len(mid_points)):
    variance+=frequency[i]*(mid_points[i]-mean)**2
variance=variance/sum(frequency)
standard_deviation=variance**0.5
coefficient_variation=(standard_deviation/mean)*100
print(f'Standard Deviation is {standard_deviation}..\ncoefficient of variation is {coefficient_variation}..')