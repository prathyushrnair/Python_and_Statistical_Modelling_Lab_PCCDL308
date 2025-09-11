"""
21. Suppose a sample of 16 light trucks is randomly selected off the assembly line. The trucks are driven 1000 miles and
the fuel mileage (MPG) of each truck is recorded. It is found that the mean MPG is 22 with a SD equal to 3. The previous
model of the light truck got 20 MPG. Conduct a t-test of the null hypothesis at p = 0.05
"""
from scipy import stats
import math
mean=20
number=16
sample_mean=22
sample_sd=3
t_statistics= (sample_mean-mean) / (sample_sd/ math.sqrt(number))
p_value=1-stats.t.cdf(t_statistics,math.sqrt(number)-1)
if p_value < 0.05:
    print(f'NULL Hypothesis prevails with p-value ={round(p_value,7)}...')
else:
    print(f'Alternate Hypothesis prevails with p-value ={round(p_value,7)}...')