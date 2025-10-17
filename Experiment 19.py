"""
19. A random sample of 395 people were surveyed and each person was asked to report the highest education level they
obtained. The data that resulted from the survey is summarized in the following table. Are gender and education level
dependent at 5% level of significance?
    |         | High School | Bachelors | Masters | Ph.D. | Total |
    |---------|-------------|-----------|---------|-------|-------|
    | Female  | 60          | 54        | 46      | 41    | 201   |
    | Male    | 40          | 44        | 53      | 57    | 194   |
    | Total   | 100         | 98        | 99      | 98    | 395   |
"""
from scipy.stats import chi2_contingency

data = [[60, 54, 46, 41], [40, 44, 53, 57]]
chi_sq_statistics, p_Value, dof, expected = chi2_contingency(data)
print(f'Chi2_statistics value is {round(chi_sq_statistics,4)}\nP-value is {round(p_Value,4)}\n'
      f'Degree of Freedom ={round(dof,4)}\nExpected Frequency(array)={expected}')
