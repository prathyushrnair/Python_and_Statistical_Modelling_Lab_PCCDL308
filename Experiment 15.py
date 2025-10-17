"""
Table contains population and murder rates (in units of murders per 100,000
people per year) for different states. Compute the mean, median and variance for
the population.
"""
population=[4779736,710231,6392017,2915918,37253956,5029196,3574097,897934]
State=['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware']
Murder_Rate=[5.7,5.6,4.7,5.6,4.4,2.8,2.4,5.8]
population_sum=sum(population)
population_mean=population_sum/len(population)
population.sort()
median_value=0
if len(population)%2==0:
    index=len(population)//2
    median_value=(population[index-1]+population[index])/2
else:
    index = len(population)//2
    median_value=population[index]
variance=0
for i in range(len(population)):
    variance+=(population[i]-population_mean)**2
variance=variance/len(population)
standard_deviation=variance**0.5
print(f'Mean of the population is {population_mean}\nMedian of the population is {median_value}'
      f'\nVariance of the population is {variance}\nCoefficent of Variation is {(standard_deviation/population_mean)*100}')

