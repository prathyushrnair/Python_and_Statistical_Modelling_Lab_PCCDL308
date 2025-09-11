"""
22. The mean productivity rating for all employees at a company was 3.8 on a five-point scale last year.
This year you get ratings from a representative sample of fifteen employees from the Human Research Management.
Do the data from this sample provide evidence that employee productivity in the department of Human Resource Management
is significantly higher than in the company as a whole? Write the null and alternative hypotheses for this problem. Use
statistical analysis software to test the null hypothesis stated above.
"""
from scipy import stats
import numpy as np
arr=np.array([4.1,3.9,3.5,4.0,4.4,4.3,4.2,4.5,3.9,3.6,4.2,4.4,4.1,4.3,4.1])
mean=3.8
t_test_value,t_p_value=stats.ttest_1samp(arr,mean)
if t_test_value > 0:
    t_p_value=t_p_value/2
    print(f'Value is greater than 0..\n P Value ={round(t_p_value/2,4)}..')
else:
    t_p_value=1-(t_p_value/2)
    print(f'Value is less than 0..\n P Value ={1-(round(t_p_value,4))}...')
print(f'T statistics value ={round(t_test_value,4)}..')
if t_p_value > 0.05:
    print(f'NULL HYPOTHESIS PREVAILS with p value={t_p_value}..')
else:
    print(f'Alternate Hypothesis Prevails with p-value ={round(t_p_value,7)}..')