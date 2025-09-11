"""
20. Calculate the correlation coefficient of the two variables shown in the table below.
    | Person | Hand | Height |
    |--------|------|--------|
    | A      | 17   | 150    |
    | B      | 15   | 154    |
    | C      | 19   | 169    |
    | D      | 17   | 172    |
    | E      | 21   | 175    |
"""
import numpy as np
hand=np.array([17,15,19,17,21])
height=np.array([150,154,169,172,175])
print(f'Correleation coefficent ={round(np.corrcoef(hand,height)[1][0],4)}..')