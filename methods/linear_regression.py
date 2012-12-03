#!/usr/bin/python 
#Filename: linear_regression.py
# @victorfarias @franzejr


from numpy import *
import sys
sys.path.append("../")
from importer import *
import numpy as np


#LinearRegression
def linearRegression(xi,y):
	pass


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
	Gradient Descent Process
'''
def gradient_descent(X, y, theta0, theta1, alpha, num_iters):
	m = y.size
	history = []
	
	for i in range(num_iters):

		predictions = X.dot(theta1) + theta0
		
	        errors_x0 = (predictions - y) 
	        errors_x1 = (predictions - y) * X[:]

		theta0 = theta0 - alpha * (1.0 / m) * errors_x0.sum()
		theta1 = theta1 - alpha * (1.0 / m) * errors_x1.sum()

		print cost_function(X,y,theta0,theta1)

		#J_history.append(compute_cost(X, y, theta))

	return theta0,theta1

def main(data_path):
	#print sys.argv

	f = importer(data_path)

	x = np.array(f[1],dtype=float)
	y = np.array(f[2],dtype=float)
	print x


	#Initialize theta parameters
	theta0 = 0.
	theta1 = 0.

	#Some gradient descent settings
	iterations = 50
	alpha = 0.000000001


	theta0, theta1 =gradient_descent(x, y, theta0, theta1, alpha, iterations)

	x1 = linspace(38000,50000,5)

	# plt.xlabel("Hora de Chegada")
	# plt.ylabel("Tempo de espera (minutos)")
	# plt.plot(f[1],f[2],'o',color='white',markersize=7,linewidth=3)
	# plt.plot(x1, x1.dot(theta1) + theta0,'k-')
	# plt.show()
	print "Theta 0:"+ str(theta0)
	print "Theta 1:"+ str(theta1)
	print "Equation: "+ str(theta1)+"x + "+str(theta0)+"b" 
main()
