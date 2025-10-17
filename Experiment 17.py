"""
If X is binomially distributed with 6 trials and a probability of success equal to
0.25 at each attempt, what is the probability of:
a) exactly 4 successes
b) at least one success
"""
from math import comb
from scipy.stats import binom
p=0.25
q=0.75
n=6
"""
exactly 4 ->>> 6C4 * p^n * q^n-r
ie """
probability_4=comb(6,4)*(0.25**4)*(0.75**2)
probability_1=comb(6,0)*(0.25**0)*(0.75**6)
print(f'Probability that x=4 is {round(probability_4,4)}\nProbability that x>1 is {round(1-probability_1,4)}')
print(type(binom.pmf(4,6,0.25)))