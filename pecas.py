#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import math as m
import copy

# Modelo da estrutura de dados. Cada indice de 'formas' tera, na primeira posicao, a quantidade de vertices
# da sua forma, seguida (nas posicoes seguintes), das coordenadas
# formas = [[qt_vertices1, coordenada1_v_1, coordenada2_v_1, coordenada3_v_1,...],[qt_vertices2, coordenada1_v_2, coordenada2_v_2],...]

#	 construtor
#	 Cada peca tera:
#	 	- numero de vertices total
#	 	- numero de formas
#		- formas
	 
#	 Cada forma tera:
#		- numero de vertices
#		- coordenadas dos vertices
global tab 
tab = "					"

class Peca:

	# Construtor
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
		# Flag para indicar a primeira forma (Forma maior)
		primeira_forma = True
		area_sub_total = 0.0
		area_total = 0.0
		# Itera por todas as formas
		for f in self.formas:
			if primeira_forma:
				primeira_forma = False
				# Percorre todas as coordenadas da forma, aplicando a formula
				for coord in range(1, int(f[0])+1):
					# Tratamento para a ultima coordenada da lista
					if coord != int(f[0]):
						# Divide a coordenada em componentes x e y, convertendo para float
						c1 = f[coord].split()
						c1 = [float(i) for i in c1]
						c2 = f[coord+1].split()
						c2 = [float(i) for i in c2]
						area_sub_total += (c1[0]*c2[1]) - (c1[1]*c2[0]) 

					else:
						# Divide a coordenada em componentes x e y, convertendo para float
						c1 = f[coord].split()
						c1 = [float(i) for i in c1]
						c2 = f[1].split()
						c2 = [float(i) for i in c2]
						area_sub_total += (c1[0]*c2[1]) - (c1[1]*c2[0]) 
				area_total = area_sub_total

			else:
				area_sub_total = 0
				# Percorre todas as coordenadas da forma, aplicando a formula
				for coord in range(1, int(f[0])+1):
					# Tratamento para a ultima coordenada da lista
					if coord != int(f[0]):
						# Divide a coordenada em componentes x e y, convertendo para float
						c1 = f[coord].split()
						c1 = [float(i) for i in c1]
						c2 = f[coord+1].split()
						c2 = [float(i) for i in c2]
						area_sub_total += (c1[0]*c2[1]) - (c1[1]*c2[0]) 
					else:
						# Divide a coordenada em componentes x e y, convertendo para float
						c1 = f[coord].split()
						c1 = [float(i) for i in c1]
						c2 = f[1].split()
						c2 = [float(i) for i in c2]
						area_sub_total += (c1[0]*c2[1]) - (c1[1]*c2[0]) 
				area_total -= abs(area_sub_total)
		return area_total/2
	

	def calcula_centro_gravidade(self, area):
		x = 0
		y = 0
		x_sub = 0
		y_sub = 0
		x_maior = 0
		y_maior = 0
		primeira_forma = True
		# Itera por todas as formas
		for f in self.formas:
			if primeira_forma:
				primeira_forma = False
				# Percorre todas as coordenadas da forma, aplicando a formula
				for coord in range(1, int(f[0])+1):
					# Tratamento para a ultima coordenada da lista
					if coord != int(f[0]):
						# Divide a coordenada em componentes x e y, convertendo para float
						c1 = f[coord].split()
						c1 = [float(i) for i in c1]
						c2 = f[coord+1].split()
						c2 = [float(i) for i in c2]
						y = (c1[1]+c2[1])*((c1[0]*c2[1]) - (c2[0]*c1[1]))
						x = (c1[0]+c2[0])*((c1[0]*c2[1]) - (c2[0]*c1[1]))
						y_maior += y
						x_maior += x

					else:
						# Divide a coordenada em componentes x e y, convertendo para float
						c1 = f[coord].split()
						c1 = [float(i) for i in c1]
						c2 = f[1].split()
						c2 = [float(i) for i in c2]
						y = (c1[1]+c2[1])*((c1[0]*c2[1]) - (c2[0]*c1[1]))
						x = (c1[0]+c2[0])*((c1[0]*c2[1]) - (c2[0]*c1[1]))
						y_maior += y
						x_maior += x 
						#y_maior = abs(y_maior)		#	Usando o abs(), o resultado nunca terminaria negativo
						#x_maior = abs(x_maior)		#	como o esperado

			else:
				x_sub = 0.0
				y_sub = 0.0
				# Percorre todas as coordenadas da forma, aplicando a formula
				for coord in range(1, int(f[0])+1):
					# Tratamento para a ultima coordenada da lista
					if coord != int(f[0]):
						# Divide a coordenada em componentes x e y, convertendo para float
						c1 = f[coord].split()
						c1 = [float(i) for i in c1]
						c2 = f[coord+1].split()
						c2 = [float(i) for i in c2]
						y = (c1[1]+c2[1])*((c1[0]*c2[1]) - (c2[0]*c1[1]))
						x = (c1[0]+c2[0])*((c1[0]*c2[1]) - (c2[0]*c1[1]))
						y_sub += y
						x_sub += x

					else:
						# Divide a coordenada em componentes x e y, convertendo para float
						c1 = f[coord].split()
						c1 = [float(i) for i in c1]
						c2 = f[1].split()
						c2 = [float(i) for i in c2]
						y = (c1[1]+c2[1])*((c1[0]*c2[1]) - (c2[0]*c1[1]))
						x = (c1[0]+c2[0])*((c1[0]*c2[1]) - (c2[0]*c1[1]))
						y_sub += y
						x_sub += x 
						#y_sub = abs(y_sub)
						#x_sub = abs(x_sub)					
						y_maior += y_sub
						x_maior += x_sub
						
		return  x_maior/(6*area), y_maior/(6*area)	

	def calcula_momento_inercia(self, cgx, cgy):
		IX_sub = 0
		IY_sub = 0
		IX = 0
		IY = 0
		# Itera por todas as formas
		for f in self.formas:
			IX_sub = 0
			IY_sub = 0
			# Percorre todas as coordenadas da forma, aplicando a formula
			for coord in range(1, int(f[0])+1):
				# Tratamento para a ultima coordenada da lista
				if coord != int(f[0]):
					# Divide a coordenada em componentes x e y, convertendo para float e alterando o sistema de eixos de referencia para o c.g.
					c1 = f[coord].split()
					c1 = [float(i) for i in c1]
					c1[0] -= cgx 
					c1[1] -= cgy
					c2 = f[coord+1].split()
					c2 = [float(i) for i in c2]
					c2[0] -= cgx 
					c2[1] -= cgy

					IY_sub = ((c1[0] * c2[1]) - (c2[0] * c1[1])) * (c1[0] ** 2 + (c1[0] * c2[0]) + (c2[0]**2))
					IX_sub = ((c1[0] * c2[1]) - (c2[0] * c1[1])) * (c1[1] ** 2 + (c1[1] * c2[1]) + (c2[1]**2))
					IY += IY_sub 
					IX += IX_sub

				else:
					# Divide a coordenada em componentes x e y, convertendo para float e alterando o sistema de eixos de referencia para o c.g.
					c1 = f[coord].split()
					c1 = [float(i) for i in c1]
					c1[0] -= cgx 
					c1[1] -= cgy
					c2 = f[1].split()
					c2 = [float(i) for i in c2]
					c2[0] -= cgx 
					c2[1] -= cgy

					IY_sub = ((c1[0] * c2[1]) - (c2[0] * c1[1])) * (c1[0] ** 2 + (c1[0] * c2[0]) + (c2[0]**2))
					IX_sub = ((c1[0] * c2[1]) - (c2[0] * c1[1])) * (c1[1] ** 2 + (c1[1] * c2[1]) + (c2[1]**2))
					IY += IY_sub 
					IX += IX_sub
					
		return IX/12, IY/12
	
	def calcula_momento_inercia_maxmin(self, IX, IY, IXY):
		
		I_max = ((IX + IY) / 2) + m.sqrt((((IX - IY) / 2) ** 2) + IXY ** 2);
		I_min = ((IX + IY) / 2) - m.sqrt((((IX - IY) / 2) ** 2) + IXY ** 2);

		return I_max, I_min

	def calcula_momento_polar(self, IX, IY):
		Ip = IX + IY
		return  Ip

	def calcula_produto_inercia(self, cgx, cgy):
		IXY_sub = 0
		IXY = 0
		# Itera por todas as formas
		for f in self.formas:
			IX_sub = 0
			IY_sub = 0
			# Percorre todas as coordenadas da forma, aplicando a formula
			for coord in range(1, int(f[0])+1):
				# Tratamento para a ultima coordenada da lista
				if coord != int(f[0]):
					# Divide a coordenada em componentes x e y, convertendo para float e alterando o sistema de eixos de referencia para o c.g.
					c1 = f[coord].split()
					c1 = [float(i) for i in c1]
					c1[0] -= cgx 
					c1[1] -= cgy
					c2 = f[coord+1].split()
					c2 = [float(i) for i in c2]
					c2[0] -= cgx 
					c2[1] -= cgy

					IXY_sub = ((c1[0] * c2[1]) - (c2[0] * c1[1])) * ((c1[0] * c2[1]) + (2*c1[0]*c1[1]) + (2*c2[0]*c2[1]) + c2[0] * c1[1])
					IXY += IXY_sub 

				else:
					# Divide a coordenada em componentes x e y, convertendo para float e alterando o sistema de eixos de referencia para o c.g.
					c1 = f[coord].split()
					c1 = [float(i) for i in c1]
					c1[0] -= cgx 
					c1[1] -= cgy
					c2 = f[1].split()
					c2 = [float(i) for i in c2]
					c2[0] -= cgx 
					c2[1] -= cgy

					IXY_sub = ((c1[0] * c2[1]) - (c2[0] * c1[1])) * ((c1[0] * c2[1]) + (2*c1[0]*c1[1]) + (2*c2[0]*c2[1]) + c2[0] * c1[1])
					IXY += IXY_sub 					
		return IXY/24

	def calcula_angulo_inclinacao(self, IX, IY, IXY):	# ERRADO		
		if IX-IY != 0:
			teta_1 = m.atan((-2*IXY)/(IX-IY))/2
			teta_2 = teta_1+90
		
		else:
			teta_1 = 45
			teta_2 = 135

		return teta_1, teta_2

	def calcula_raio_giracao(self, area, IX, IY, I_max, I_min):
		Kx = m.sqrt(IX/area);
		Ky = m.sqrt(IY/area);
		K_max = m.sqrt(I_max/area);
		K_min = m.sqrt(I_min/area);

		return Kx, Ky, K_max, K_min

# Funcao que calcula a distancia entre dois pontos
def calcula_dist(v1,v2):
	aux = v1.split()
	x1 = float(aux[0])
	y1 = float(aux[1])
	aux = v2.split()
	x2 = float(aux[0])
	y2 = float(aux[1])
	return m.sqrt((x2-x1)**2+(y2-y1)**2)

# Funcao que todo o arquivo e armazena em uma estrutura
def ler_arquivo():
	nome_arquivo = sys.argv[1] 	
	arquivo = open(nome_arquivo, 'r')
	lista_linhas = arquivo.readlines()
	arquivo.close()
	return lista_linhas 

def escrever_ativo(Perimetro, Area, Cgx, Cgy, IX, IY, IXY, Imax, Imin, Ip, Teta1, Teta2, Kx, Ky, Kmax, Kmin):
	arquivo = open("saida.out", 'w')
	arquivo.write("ALUNO:" + str(tab) + "PEDRO HENRIQUE MORI \n")
	arquivo.write("MATRÍCULA:" + str(tab) + "2015110643 \n \n \n")
	arquivo.write("Área da figura: " +  str(tab) + str(Area) + " cm2 \n")
	arquivo.write("Perímetro da figura: " + str(tab) + str(Perimetro) + " cm \n")
	arquivo.write("Coord. X do C.G.: " + str(tab) + str(Cgx) + " cm \n")
	arquivo.write("Coord. Y do C.G.: " + str(tab) + str(Cgy) + " cm \n")
	arquivo.write("Momento de inercia, Ix: " + str(tab) + str(IX) + " cm4 \n")
	arquivo.write("Momento de inercia, Iy: " + str(tab) + str(IY) + " cm4 \n")
	arquivo.write("Produto de inercia, Ixy: " + str(tab) + str(IXY) + " cm4 \n")
	arquivo.write("Momento polar de inercia, Ip: " + str(tab) + str(Ip) + " cm4 \n")
	arquivo.write("Momento de inercia mínimo, Imin: " + str(tab) + str(Imin) + " cm4 \n")
	arquivo.write("Momento de inercia máximo, Imax: " + str(tab) + str(Imax) + " cm4 \n")
	arquivo.write("Ângulo incl. eixo princ. - Teta1: " + str(tab) + str(Teta1) + " cm \n")
	arquivo.write("Ângulo incl. eixo princ. - Teta2: " + str(tab) + str(Teta2) + " cm \n")
	arquivo.write("Raio de giração, Rmin: " + str(tab) + str(Kmin) + " cm \n") 	
	arquivo.write("Raio de giração, Rmax: " + str(tab) + str(Kmax) + " cm \n")
	arquivo.write("Raio de giração, Rx: " + str(tab) + str(Kx) + " cm \n")
	arquivo.write("Raio de giração, Ry: " + str(tab) + str(Ky) + " cm \n")

# Auxiliar para criacao do objeto 'peca'
def gera_peca(lista_linhas):
	num_formas = int(lista_linhas[0].replace('\n', ''));
	num_vertices = int(lista_linhas[1].replace('\n', ''));
	formas = []
	
	if num_formas != 1:
		for i in range(2, num_formas+2):
			formas.append([lista_linhas[i].replace('\n', '')])
	else:
		i = 1
		formas.append([num_vertices])
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
	# Le o arquivo e armazena em 'lista_linhas'
	lista_linhas = ler_arquivo()
	# Extrai de 'lista_linhas' os valores necessarios para criar a peca
	num_vertices, num_formas, formas = gera_peca(lista_linhas)
	# Cria a peca
	p = Peca(num_vertices, num_formas, formas)

	#		   #
	# Calculos #
	#		   #
	
	Perimetro =  p.calcula_perimetro()
	print '\n' + "Perímetro: " + str(Perimetro) + '\n'
	Area =  p.calcula_area()
	print "Área: " + str(Area) + '\n'
	Cgx,Cgy = p.calcula_centro_gravidade(Area)
	print "C.G. em x: " + str(Cgx) + '\n'
	print "C.G. em y: " + str(Cgy) + '\n'
	IX,IY = p.calcula_momento_inercia(Cgx,Cgy)
	print "Momento de inercia em x: " + str(IX) + '\n'
	print "Momento de inercia em y: " + str(IY) + '\n'
	IXY = p.calcula_produto_inercia(Cgx, Cgy)
	print "Produto de inercia: " + str(IXY) + '\n'
	Imax, Imin = p.calcula_momento_inercia_maxmin(IX, IY, IXY)
	print "Momento de inercias mínimo: " + str(Imin) + '\n'
	print "Momento de inercias máximo: " + str(Imax) + '\n'
	Ip = p.calcula_momento_polar(IX, IY)
	print "Momento polar de inercia: " + str(Ip) + '\n'
	Teta1, Teta2 = p.calcula_angulo_inclinacao(IX, IY, IXY)
	print "Ângulo de inclinação eixo principal - Teta1: " + str(Teta1) + '\n'
	print "Ângulo de inclinação eixo principal - Teta2: " + str(Teta2) + '\n'
	Kx, Ky, Kmax, Kmin = p.calcula_raio_giracao(Area, IX, IY, Imax, Imin)
	print "Raio de giração, Kx: " + str(Kx) + '\n'
	print "Raio de giração, Ky: " + str(Ky) + '\n'
	print "Raio minimo de giração: " + str(Kmin) + '\n'
	print "Raio máximo de giração: " + str(Kmax) + '\n'
	escrever_ativo(Perimetro, Area, Cgx, Cgy, IX, IY, IXY, Imax, Imin, Ip, Teta1, Teta2, Kx, Ky, Kmax, Kmin)