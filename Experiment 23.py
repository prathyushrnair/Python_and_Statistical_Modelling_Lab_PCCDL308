"""
23. Obtain the regression equation for predicting systolic blood pressure from job satisfaction with reference to the
given data using statistical analysis software. If one knows that a subject in the future has a score on job
satisfaction of 15, what is their systolic blood pressure predicted to be? What is the standard error of estimate?
    | Job Satisfaction | Systolic BP |
    |------------------|-------------|
    | 34               | 124         |
    | 23               | 128         |
    | 19               | 157         |
    | 43               | 133         |
    | 56               | 116         |
    | 47               | 125         |
    | 32               | 147         |
    | 16               | 167         |
    | 55               | 110         |
    | 25               | 156         |

"""
from scipy import stats
import numpy as np
job_satisfaction=np.array([34,23,19,43,56,47,32,16,55,25])
systolic_bp=np.array([124,128,157,133,116,125,147,167,110,156])
slope,intercept,r_value,p_value,std_err=stats.linregress(job_satisfaction,systolic_bp)
print(f'Slope \t\t={slope} \nIntercept\t={intercept} \nR-value \t={r_value} \nP-value \t={p_value} '
      f'\nStandard Error bw data points\t={std_err}')
y_prediction = slope * job_satisfaction + intercept
# Y          =                       MX + C
Sum_of_Squared_Errors=np.sum((systolic_bp-y_prediction)**2)
#degree of freedom eq = len( job satisfaction ) - 2
dof=len(job_satisfaction)-2
SSE=np.sqrt(Sum_of_Squared_Errors/dof)
print(f'Standard Error of Estimate is {round(SSE,4)}..')
