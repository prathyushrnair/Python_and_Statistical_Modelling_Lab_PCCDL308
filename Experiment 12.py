"""
Plot a graph 𝑦=𝑓(𝑥)  [1, 2]
"""
import matplotlib.pyplot as plt
import numpy as np
import math
choice=0
print("""
[[ MENU ]]
1.X^2
2.Sin X
3.Cos X
4.Tan x
5.Break
""")
choice=int(input('Enter the choice from above.'))
while choice!=5:
    if choice==1:
        x=np.linspace(-10,10,100)
        y=x**2
        plt.plot(x,y,label='X^2=F(X)')
        plt.xlabel('X Values  --->')
        plt.ylabel('Y Values  --->')
        plt.show()
    elif choice==2:
        x=np.linspace(-10,10,100)
        y=math.sin(x)
        plt.plot(x,y,label='Sin(X) = F(X)')
        plt.xlabel('X Values  --->')
        plt.ylabel('Y Values  --->')
        plt.show()
    elif choice==3:
        x=np.linspace(-10,10,100)
        y=math.cos(x)
        plt.plot(x,y,label='Cos(X) = F(X)')
        plt.xlabel('X Values  --->')
        plt.ylabel('Y Values  --->')
        plt.show()
    elif choice==4:
            x=np.linspace(-10,10,100)
            y=math.tan(x)
            plt.plot(x,y,label='Tan(X) = F(X)')
            plt.xlabel('X Values  --->')
            plt.ylabel('Y Values  --->')
            plt.show()
    else:
        break


