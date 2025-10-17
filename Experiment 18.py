"""

If X is binomially distributed with 6 trials and a probability of success equal to 0.25 at each attempt, what is the probability of:
a) exactly 4 successes
b) at least one success

"""
from scipy.stats import binom
from sklearn.externals.array_api_extra import atleast_nd

exactly_least_4_success=binom.pmf( 4,6,.25)
print(exactly_least_4_success)
at_least_1_success=binom.cdf(0,6,0.25)
print(f'{exactly_least_4_success} and {1-at_least_1_success}')
