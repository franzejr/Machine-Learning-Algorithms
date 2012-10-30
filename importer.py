#!/usr/bin/python 
#Filename: importer.py
# @victorfarias @franzejr

import csv

#Function to get the time and return number which can represent this number
def convertToNumber(hora):
	hora_vetor = hora.split(":")
	return (int(hora_vetor[0])*3600 + int(hora_vetor[1])*60 + int(hora_vetor[2]))

'''
	Import from a file and can return the dict with all the informations you want
'''
def importer(filename):
	f = csv.reader(open(filename), delimiter=',')
	chegadasAtrasos = []
	horasChegadas = []
	atrasos = []
	for [DataHora,DiaSemana,atraso,HoraChegada,Curso,FurouFila] in f:
		chegadasAtrasos.append([convertToNumber(HoraChegada),atraso])
		horasChegadas.append(convertToNumber(HoraChegada))
		atrasos.append(atraso)
	return chegadasAtrasos,horasChegadas,atrasos
