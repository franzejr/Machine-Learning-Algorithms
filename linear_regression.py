#!/usr/bin/python 
#Filename: linear_regression.py
# @victorfarias @franzejr

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
