#!/usr/bin/env python2

import sys
import math
import copy

class Peca:

# Modelo da estrutura de dados. Cada indice de 'formas' tera, na primeira posicao, a quantidade de vertices
# da sua forma, seguida (nas posicoes seguintes), das coordenadas
# formas = [[qt_vertices1, coordenada1_v_1, coordenada1_v_2, coordenada1_v_3,...],[qt_vertices2, coordenada2_v_1, coordenada2_v_2],...]

#	 construtor
#	 Cada peca tera:
#	 	- numero de vertices total
#	 	- numero de formas
	 
#	 Cada forma tera:
#		- numero de vertices
#		- coordenadas dos vertices

	def __init__(self, num_vertices, num_formas, formas): 
		self.formas = formas
		self.num_vertices = num_vertices
		self.num_formas = num_formas 

	def calcula_perimetro(self):
		soma = 0
		for f in formas:
			for i in range(1,int(f[0])+1):
				if i == int(f[0]):
					soma += calcula_dist(f[i],f[1])
				else:
					soma += calcula_dist(f[i],f[i+1])
		return soma

	def calcula_area(self):
		primeira_forma = True
		area_sub_total = 0.0
		area_total = 0.0
		for f in self.formas:
			if primeira_forma:
				primeira_forma = False
				for coord in range(1, int(f[0])+1):
					if coord != int(f[0]):
						c1 = f[coord].split()
						c2 = f[coord+1].split()
						area_sub_total += (float(c1[0])*float(c2[1])) - (float(c1[1])*float(c2[0])) 

					else:
						c1 = f[coord].split()
						c2 = f[1].split()
						area_sub_total += (float(c1[0])*float(c2[1])) - (float(c1[1])*float(c2[0])) 
				area_total = area_sub_total

			else:
				area_sub_total = 0
				for coord in range(1, int(f[0])+1):
					if coord != int(f[0]):
						c1 = f[coord].split()
						c2 = f[coord+1].split()
						area_sub_total += (float(c1[0])*float(c2[1])) - (float(c1[1])*float(c2[0])) 
					else:
						c1 = f[coord].split()
						c2 = f[1].split()
						area_sub_total += (float(c1[0])*float(c2[1])) - (float(c1[1])*float(c2[0])) 
				area_total -= abs(area_sub_total)
		return float(area_total/2)
	
	def calcula_centro_gravidade(self):
		x = 0
		y = 0
		x_sub = 0
		y_sub = 0
		x_maior = 0
		y_maior = 0
		primeira_forma = True

		for f in self.formas:
			if primeira_forma:
				primeira_forma = False
				for coord in range(1, int(f[0])+1):
					if coord != int(f[0]):
						c1 = f[coord].split()
						c2 = f[coord+1].split()
						y = (float(c1[1])+float(c2[1]))*((float(c1[0])*float(c2[1]) ) - (float(c2[0])*float(c1[1])))
						x = (float(c1[0])+float(c2[0]))*((float(c1[0])*float(c2[1]) ) - (float(c2[0])*float(c1[1])))
						y_maior += y
						x_maior += x

					else:
						c1 = f[coord].split()
						c2 = f[1].split()
						y = (float(c1[1])+float(c2[1]))*((float(c1[0])*float(c2[1]) ) - (float(c2[0])*float(c1[1])))
						x = (float(c1[0])+float(c2[0]))*((float(c1[0])*float(c2[1]) ) - (float(c2[0])*float(c1[1])))
						y_maior += y
						x_maior += x 
						y_maior = abs(y_maior)
						x_maior = abs(x_maior)

			else:
				x_sub = 0
				y_sub = 0
				for coord in range(1, int(f[0])+1):
					if coord != int(f[0]):
						c1 = f[coord].split()
						c2 = f[coord+1].split()
						y = (float(c1[1])+float(c2[1]))*((float(c1[0])*float(c2[1]) ) - (float(c2[0])*float(c1[1])))
						x = (float(c1[0])+float(c2[0]))*((float(c1[0])*float(c2[1]) ) - (float(c2[0])*float(c1[1])))
						y_sub += y
						x_sub += x

					else:
						c1 = f[coord].split()
						c2 = f[1].split()
						y = (float(c1[1])+float(c2[1]))*((float(c1[0])*float(c2[1]) ) - (float(c2[0])*float(c1[1])))
						x = (float(c1[0])+float(c2[0]))*((float(c1[0])*float(c2[1]) ) - (float(c2[0])*float(c1[1])))
						y_sub += y
						x_sub += x 
						y_sub = abs(y_sub)
						x_sub = abs(x_sub)
						y_maior -= y_sub
						x_maior -= x_sub
		return y_maior, x_maior
	
		

def calcula_dist(v1,v2):
	aux = v1.split()
	x1 = float(aux[0])
	y1 = float(aux[1])
	aux = v2.split()
	x2 = float(aux[0])
	y2 = float(aux[1])
	return math.sqrt((x2-x1)**2+(y2-y1)**2)

# le todo o arquivo e armazena em uma estrutura
def ler_arquivo():
	nome_arquivo = sys.argv[1] 	
	arquivo = open(nome_arquivo, 'r')
	lista_linhas = arquivo.readlines()
	arquivo.close()
	return lista_linhas 

# Auxiliar para criacao do objeto 'peca'
def gera_caso(lista_linhas):
	num_vertices = int(lista_linhas[0].replace('\n', ''));
	num_formas = int(lista_linhas[1].replace('\n', ''));
	formas = []
	for i in range(2, num_formas+2):
		formas.append([lista_linhas[i].replace('\n', '')])
	coordenadas = []
	for linha in lista_linhas[i+1:]:
		coordenadas.append(linha.replace('\n',''))

	count = 0
	for f in formas:
		for i in range(0,int(f[0])):
			f.append(coordenadas[count])
			count +=1

	return num_vertices, num_formas, formas



if __name__ == "__main__":
	lista_linhas = ler_arquivo()
	num_vertices, num_formas, formas = gera_caso(lista_linhas)
	p = Peca(num_vertices, num_formas, formas)
	print p.calcula_perimetro()
	print p.calcula_area()
	print p.calcula_centro_gravidade()