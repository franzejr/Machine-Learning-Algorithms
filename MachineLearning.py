#!/usr/bin/python 
#Filename: Machine Learning.py
# @victorfarias @franzejr

from numpy import *
from pylab import *
from importer import *
from linear_regression import *
import numpy as np
import matplotlib.pyplot as plt
	
'''
Main function

'''
def main():
	#print sys.argv

	f = importer("ru.csv")

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

	plt.xlabel("Hora de Chegada")
	plt.ylabel("Tempo de espera (minutos)")
	plt.plot(f[1],f[2],'o',color='white',markersize=7,linewidth=3)
	plt.plot(x1, x1.dot(theta1) + theta0,'k-')
	plt.show()
	print "Theta 0:"+ str(theta0)
	print "Theta 1:"+ str(theta1)
	print "Equation: "+ str(theta1)+"x + "+str(theta0)+"b" 
main()
