#include <iostream>
#include <cmath>
#include <fstream>

using namespace std;

int main()
{
		
	
	int Num_cont,Num_vert;
	ifstream arq_entrada("secao.dat");
	if (arq_entrada){
		cout << "Foi gerado o arquivo com o nome " << endl; 
		
		arq_entrada >> Num_cont; //Numero de contornos
		cout << "Num_cont: " << Num_cont << endl;
		arq_entrada >> Num_vert; //Numero de Vértices
		cout << "Num_vert: " << Num_vert << endl;
		int vet[Num_cont];
		if (Num_cont == 1) {
			vet[0] = Num_vert;
			cout << "MEUPAU";
		}
		else {
		for (int i=0; i<Num_cont; i++){
			arq_entrada >> vet[i];
			cout << vet[i] << ", ";	
		}
		}
		cout << endl;
		float vetx[Num_vert],vety[Num_vert];
		for (int i=0; i<Num_vert; i++){
			arq_entrada>>vetx[i]>>vety[i];
			cout << vet[i] << ", ";	
		}
		cout << endl;
	
	arq_entrada.close();
	
	//calculando o perimetro
	float PMT=0;
	int k=0;// o k ira guardar a posicao inicial de cada contorno
	for (int i = 0; i < Num_cont; i++){
	
		for (int j=0;j<vet[i];j++){
			if(j==vet[i]-1){
				PMT += sqrt((pow(vetx[k+j]-vetx[k],2))+(pow(vety[k+j]-vety[k],2)));				
				k += j+1;
			}else{
				PMT += sqrt((pow(vetx[k+j]-vetx[k+j+1],2))+(pow(vety[k+j]-vety[k+j+1],2)));
			}
		}
	}
	
	k=0;
	
	
	//calculando a area da figura
	float areaTotal= 0, areaFuros=0;
		for (int i = 0; i < Num_cont; i++){
			if (!i){
				for (int j=0;j<vet[i];j++){
					if(j==vet[i]-1){
						areaTotal += ((vetx[j] * vety[k]) - (vetx[k]*vety[j]));
						k += j+1;
					}else{
						areaTotal += ((vetx[j] * vety[j+1])- (vetx[j+1]*vety[j]));
					}
				}
			}else{
				areaFuros = 0;
				for (int j=0;j<vet[i];j++){
					if(j==vet[i]-1){
						areaFuros += ((vetx[k+j]*vety[k])-vetx[k]*vety[k+j]);
						k += j+1;
					}else{
						areaFuros += ((vetx[k+j]*vety[k+j+1])-vetx[k+j+1]*vety[k+j]);
					}
					
				}
				areaTotal -= abs(areaFuros);
			}
		}
		k=0;
		
		areaTotal= areaTotal/2;
		
	//		CALCULANDO O CG DA FIGURA
	float CGx=0,aux_x=0,aux_y=0,CGy=0;
		for (int i = 0; i < Num_cont; i++){
			if (!i){
				for (int j=0;j<vet[i];j++){
					
					if(j==vet[i]-1){
						CGy+= ((vety[j]+vety[k])*(vetx[j]*vety[k]-vetx[k]*vety[j]));
						CGx+= ((vetx[j]+vetx[k])*(vetx[j]*vety[k]-vetx[k]*vety[j]));
						k += j+1;
					}else{
						CGy+= ((vety[j]+vety[j+1])*(vetx[j]*vety[j+1]-vetx[j+1]*vety[j]));
						CGx+= ((vetx[j]+vetx[j+1])*(vetx[j]*vety[j+1]-vetx[j+1]*vety[j]));
					}
					
				}
			}else{
				aux_x = 0;
				aux_y = 0;
				for (int j=0;j<vet[i];j++){
					
					if(j==vet[i]-1){
						aux_y+= ((vety[j+k]+vety[k])*(vetx[j+k]*vety[k]-vetx[k]*vety[j+k]));
						aux_x+= ((vetx[j+k]+vetx[k])*(vetx[j+k]*vety[k]-vetx[k]*vety[j+k]));
						k += j+1;
					}else{
						aux_y+= ((vety[j+k]+vety[j+1+k])*(vetx[j+k]*vety[j+1+k]-vetx[j+1+k]*vety[j+k]));
						aux_x+= ((vetx[j+k]+vetx[j+1+k])*(vetx[j+k]*vety[j+1+k]-vetx[j+1+k]*vety[j+k]));
					}
					
					
				}
				CGx+=aux_x;
				CGy+=aux_y;
			}
		}
		
		
		CGy=CGy/(6*areaTotal);
		CGx=CGx/(6*areaTotal);
		
		
		
		k=0;
		// PASSANDO O VETOR DE CORDENADAS PARA A REFERENCIA NO CENTRO DE GRAVIDADE
		float Ix=0,Iy=0;
		for (int i = 0; i < Num_vert; i++){
			vetx[i] -= CGx;
			vety[i] -= CGy;
		}
		// CALCULANDO O MOMENTO DE INERCIA
		for (int i = 0; i < Num_cont; i++){
			aux_y=0;
			aux_x=0;
			for (int j=0;j<vet[i];j++){	
				if(j==vet[i]-1){
					Iy+= ((vetx[k+j] * vety[k]) - (vetx[k] * vety[k+j])) * (pow(vetx[k+j],2) + (vetx[k+j] * vetx[k]) + (pow(vetx[k],2)));
					Ix+=((vetx[k+j] * vety[k]) - (vetx[k] * vety[k+j])) * (pow(vety[k+j],2) + (vety[k+j]*vety[k]) + (pow(vety[k],2)));		
					k += j+1;
				}else{
					Iy+= (vetx[k+j] * vety[k+j+1] - vetx[k+j+1] * vety[k+j]) * (pow(vetx[k+j],2) + (vetx[k+j]*vetx[k+j+1]) + (pow(vetx[k+j+1],2)));
					Ix+= (vetx[k+j] * vety[k+j+1] - vetx[k+j+1] * vety[k+j]) * (pow(vety[k+j],2) + (vety[k+j]*vety[k+j+1]) + (pow(vety[k+j+1],2)));
				}		
			}
		}
		Ix=Ix/12;
		Iy=Iy/12;
		// CALCULO DO PRODUTO DE INERCIA
		
		k=0;
		float Ixy = 0;
		
		for (int i = 0; i < Num_cont; i++){
			
			for (int j=0;j<vet[i];j++){	
				if(j==vet[i]-1){
					Ixy+= ((vetx[k+j] * vety[k]) - (vetx[k] * vety[k+j])) * ((vetx[k+j]*vety[k]) + (2*vetx[k+j] * vety[k+j]) + (2 * vety[k] * vetx[k]) + (vetx[k]*vety[k+j]));
					
					k += j+1;
				}else{
					Ixy+= ((vetx[k+j] * vety[k+j+1]) - (vetx[k+j+1] * vety[k+j])) * ((vetx[k+j]*vety[k+j+1]) + (2*vetx[k+j] * vety[k+j]) + (2 * vety[k+j+1] * vetx[k+j+1]) + (vetx[k+j+1]*vety[k+j]));
					
				}		
			}
		}
		Ixy=Ixy/24;
		
		//MOMENTO POLAR DE INERCIA 
		
		float Ip=Ix+Iy;
		
		//CALCULO DO MOMENTO MAXIMO E MINIMO
		
		float I_max, I_min;
		I_max=((Ix+Iy)/2)+ sqrt(pow(((Ix-Iy)/2),2)+ pow(Ixy,2));
		I_min=((Ix+Iy)/2)- sqrt(pow(((Ix-Iy)/2),2)+ pow(Ixy,2));
		
		//CALCULO DO RAIO DE GIRAÇÃO
		
		float  K_max, K_min;
		
		
		K_max = sqrt(I_max/areaTotal);
		K_min = sqrt(I_min/areaTotal);
		
		//ÂNGULOS DE INCLINAÇÃO
		float teta1, teta2;
		if ((Ix-Iy)!=0){
			teta1 = 0.5*atan((-2*Ixy)/(Ix-Iy));
			teta2 = teta1+90;
		}
		else{
			teta1 = 45;
			teta2 = 135;
		}
		ofstream arq_saida("INFORMACOES DA PECA.txt");
		arq_saida<<"Perimetro: " << PMT<<" cm"<<endl;
		arq_saida<< "Area Total: " << areaTotal <<" cm^2"<<endl<<endl;
		arq_saida<<"Cordenada x do CG " <<CGx<<" cm"<<endl;
		arq_saida<<"Cordenada y do CG: " <<CGy<<" cm"<<endl<<endl;
		arq_saida<<"Momento de inercia de x: " <<Ix<<" cm4"<<endl;
		arq_saida<<"Momento de inercia de y: " <<Iy<<" cm4"<<endl;
		arq_saida<<"Produto de inercia: " <<Ixy<<" cm4"<<endl;
		arq_saida<<"Momento polar de inercia: "<<Ip<<" cm4"<<endl;
		arq_saida<<"Momento de inercia minimo: " <<I_min<<" cm4"<<endl;
		arq_saida<<"Momento de inercia maximo: " <<I_max<<" cm4"<<endl<<endl;
		arq_saida<<"Teta1: " <<teta1<<" º"<<endl;
		arq_saida<<"Teta2 " <<teta2<<" °"<<endl<<endl;
		arq_saida<<"Raio de giração maximo " <<K_max<< endl;
		arq_saida<<"Raio de giração minimo " << K_min << endl;
		arq_saida.close();
	
	
	
	}else{
		cout<<"ARQUIVO NAO ABERTO"<<endl;
	}
	
}

	
	


