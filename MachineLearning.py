#!/usr/bin/python 
#Filename: Machine Learning.py
# @victorfarias @franzejr

from numpy import *
from pylab import *
import matplotlib.pyplot as plt
import sys
import csv

#Function to get the time and return number which can represent this number
def convertToNumber(hora):
	hora_vetor = hora.split(":")
	return (int(hora_vetor[0])*3600 + int(hora_vetor[1])*60 + int(hora_vetor[2]))

#LinearRegression
def linearRegression(xi,y):
	A = array([ xi,ones(140)])
	w = linalg.lstsq(A.T,y)[0]
	
	# plotting the line
	line = w[0]*xi+w[1] # regression line
	plt.plot(xi,line,'r-',xi,y,'o')
	
	
def main():
	#print sys.argv

	f = csv.reader(open('ru.csv'), delimiter=',')
	plt.xlabel("Hora de Chegada")
	plt.ylabel("Tempo de espera (minutos)")
	chegadasAtrasos = []
	horasChegadas = []
	atrasos = []
	for [DataHora,DiaSemana,atraso,HoraChegada,Curso,FurouFila] in f:
		chegadasAtrasos.append([convertToNumber(HoraChegada),atraso])
		horasChegadas.append(convertToNumber(HoraChegada))
		atrasos.append(atraso)
		plt.scatter(convertToNumber(HoraChegada),int(atraso))
	linearRegression(horasChegadas,atrasos)
	#print atrasos
	#print horasChegadas
	#plt.show()

main()
