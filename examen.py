import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.set_printoptions(suppress=True)

class YieldConverter():
	def __init__(self, CN):
		self.CN = CN
		self.T = np.array(273.15/(self.CN['T gas']+273.15))
		self.metano = np.array(np.round(((self.CN['ml biogas']*self.T)/self.CN.loc[0,'SV'])*(self.CN['CH4%']/100),2))
		self.biogas = np.array(np.round(((self.CN['ml biogas']*self.T)/self.CN.loc[0,'SV']),2))
		self.metano_cum = np.add.accumulate(self.biogas)
		self.biogas_cum = np.add.accumulate(self.metano)
		self.x = np.array(self.CN['DIA'])


class Compare():
	def __init__(self, ensayo):
		self.ensayo = ensayo
		self.valores = {}
		i = 1
		while i<=len(self.ensayo):
			self.valores[i] = self.ensayo[i-1]
			i+=1


	def max_daily(self):
		resultado = []
		for i in self.valores.keys():
			dia = np.where(self.valores[i]==np.amax(self.valores[i]))
			a,b,c = np.round(np.amax(self.valores[i]), 2), i, dia[0][0]
			tupla = (a,b,c)
			resultado.append(tupla)
		return resultado


	def max_cum(self):
		resultado = []
		for i in self.valores.keys():
			suma = np.round(np.sum(self.valores[i]), 2)
			a,b = suma,i
			tupla = (a,b)
			resultado.append(tupla)
		return resultado


	def stopday(self):
		resultado=[]
		for i in self.valores.keys():
			days = 0
			inicio = []
			batch = self.valores[i]
			while np.sum(inicio)*0.01 <= batch[days]:
				inicio.append(batch[days])
				days += 1
			a,b=i,days
			tupla = (a,b)
			resultado.append(tupla)
		return resultado
