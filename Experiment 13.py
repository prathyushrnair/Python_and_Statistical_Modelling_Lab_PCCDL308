"""
11.7 for Africa; 10.4 for Asia; 1.9 for Europe; 9.4 for North America; 3.3
Oceania; 6.9 South America; 7.9 Soviet Union.
"""
import matplotlib.pyplot as plt
from scipy.ndimage import rotate

continents=['Africa','ASIA','Europe','NA','Ocenia','SA','SU']
values=[ 11.7 , 10.4 , 1.9 , 9.4 , 3.3 , 6.9 , 7.9 ]
plt.bar(continents,values,label='Areas of Various continents around the world')
plt.xlabel('CONTINENTS -->')
plt.ylabel('Area in millions of sq miles --->')
plt.xticks(rotation=30)
plt.show()