import numpy as np
import matplotlib.pyplot as plt

class Table():

    def __init__(self, xmin, xmax, xfreq, ylist):
        self.xlist=list(np.linspace(xmin, xmax, xfreq))
        self.ylist=ylist
        self.table={}
        for i in range(len(self.xlist)):
            self.table[self.xlist[i]]=self.ylist[i]

    def m(self, x1,x2):
        return (self.table[x2]-self.table[x1])/(x2-x1)

    def x2(self, x):
        for i in range(len(self.xlist)):
            if x< self.xlist[i]:
                return i

    def y(self, x):
        if self.x2(x)==0:
            return self.ylist[0]
        elif self.x2(x)==None:
            return self.ylist[-1]
        else:
            x2= self.xlist[self.x2(x)]
            x1=self.xlist[self.x2(x)-1]
            x-=x1

            y=self.table[x1]+self.m(x1,x2)*x
            return y

    def graph(self):
            plt.plot(self.xlist, self.ylist)
            plt.show()





tabelle= Table(0, 9, 10, [0,1,-1,3,3,5,6,7,8,7])
print(tabelle.table)
#m=tabelle.m(1,2)
print(tabelle.y(4.123))
tabelle.graph()
