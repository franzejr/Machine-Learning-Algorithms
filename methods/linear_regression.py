#!/usr/bin/python 
#Filename: linear_regression.py
# @victorfarias @franzejr


from numpy import *
import sys
sys.path.append("../")
from importer import *
import numpy as np
import matplotlib.pyplot as plt
'''

	Cost Function for linear Regression
'''
def cost_function(X, y, theta0,theta1):
    m = y.size

    predictions = X.dot(theta1) + theta0

    sqErrors = (predictions - y) ** 2

    J = (1.0 / (2 * m)) * sqErrors.sum()

    return J

'''
	Linear Regression using Gradient Descent Process
'''
def linearRegression(X, y, theta0, theta1, alpha, num_iters):
	X = np.array(X,dtype=float)
	y = np.array(y,dtype=float)
	m = y.size
	
	for i in range(num_iters):

		predictions = X.dot(theta1) + theta0
		
	        errors_x0 = (predictions - y) 
	        errors_x1 = (predictions - y) * X[:]

		theta0 = theta0 - alpha * (1.0 / m) * errors_x0.sum()
		theta1 = theta1 - alpha * (1.0 / m) * errors_x1.sum()
		x1 = linspace(38000,50000,5)
		y1 = x1.dot(theta1) + theta0

	return x1,y1

def main():
	#print sys.argv

	f = importer("ru.csv")

	x, y =linearRegression(f[1], f[2], 0., 0., 0.000000001, 50)
	plt.xlabel("Hora de Chegada")
	plt.ylabel("Tempo de espera (minutos)")
	plt.plot(f[1],f[2],'o',color='white',markersize=7,linewidth=3)
	plt.plot(x, y,'k-')
	plt.show()
#	print "Theta 0:"+ str(theta0)
#	print "Theta 1:"+ str(theta1)
#	print "Equation: "+ str(theta1)+"x + "+str(theta0)+"b" 
main()
