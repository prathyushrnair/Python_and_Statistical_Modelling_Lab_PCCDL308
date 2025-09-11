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