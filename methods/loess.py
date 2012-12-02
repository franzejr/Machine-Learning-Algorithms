#!/usr/bin/python 
#Filename: linear_regression.py
# @victorfarias @franzejr

from pylab import *
from importer import *
import numpy as np

'''
LOESS and LOWESS (locally weighted scatterplot smoothing) are two strongly 
related regression modeling methods that combine multiple regression models in a 
k-nearest-neighbor-based meta-model. "LOESS" is a later generalization of LOWESS; 
although it is not a true initialism, it may be understood as standing for "LOcal regrESSion"
'''
def loess(x,h,xp,yp):
	w=exp(-0.5*(((x-xp)/h)**2)/sqrt(2*pi*h**2))
	b=sum(w*xp)*sum(w*yp) - sum(w)*sum(w*xp*yp)
	b /= sum(w*xp)**2 - sum(w)*sum(x*xp**2)
	a=(sum(w*yp)-b*sum(w*xp))/sum(w)
	return a+b*x

#d=loadtxt("ex.csv",delimiter=',')
ru=importer("ru.csv")
d=np.array(ru[1],dtype=float)
e=np.array(ru[2],dtype=float)

s1,s2 = [],[]

for k in d:
	s2.append(loess(int(k),50,d,e))
	s1.append(loess(int(k),5,d,e))

xlabel("Day in Year")
ylabel("Draft Number")


plot(d,e,'o',color='white',markersize=7,linewidth=3)
plot(d,array(s1),'k-',d,array(s2),'k--')

#q=4
#axis([1-q,366+q,1-q,366+q])

show()

savefig("ex.eps")
