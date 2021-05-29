##PARTE DE CORRER AL FINAL DEL CODIGO
#JOSE MARTINEZ HERNANDEZ 19/05/2021
import matplotlib
import matplotlib.pyplot as plt
from bresenham import bresenham
matriz = []
fig = plt.figure()
ax = fig.add_subplot(111)

def llenadoMatrizCuadrado():
    iniciox = int(input("Ingresa coordenadas de inicio x: "))
    inicioy = int(input("Ingresa coordenadas de inicio y: "))
    aumento = int(input("Ingresa tamaño de lado: "))
    aumento = aumento -1
    matriz.append([])
    matriz[0].append(iniciox)
    matriz[0].append(inicioy)
    matriz.append([])
    matriz[1].append(iniciox)
    matriz[1].append(inicioy + aumento)
    matriz.append([])
    matriz[2].append(iniciox + aumento)
    matriz[2].append(inicioy+ aumento)
    matriz.append([])
    matriz[3].append(iniciox+aumento)
    matriz[3].append(inicioy)
    
    plt.xlim([iniciox-2, (iniciox+aumento)+2])
    plt.ylim([inicioy-2, (inicioy+aumento)+2])
    
def llenadoMatrizRectangulo():
    iniciox = int(input("Ingresa coordenadas de inicio x: "))
    inicioy = int(input("Ingresa coordenadas de inicio y: "))
    base = int(input("Ingresa tamaño de la base: "))
    altura = int(input("Ingresa tamaño de la altura: "))
    base = base-1
    altura = altura -1
    matriz.append([])
    matriz[0].append(iniciox)
    matriz[0].append(inicioy)
    matriz.append([])
    matriz[1].append(iniciox)
    matriz[1].append(inicioy + altura)
    matriz.append([])
    matriz[2].append(iniciox + base)
    matriz[2].append(inicioy+ altura)
    matriz.append([])
    matriz[3].append(iniciox + base)
    matriz[3].append(inicioy)
    
    plt.xlim([iniciox-2, (iniciox+base)+2])
    plt.ylim([inicioy-2, (inicioy+altura)+2])

def llenadoMatrizTrianguloRectangulo():
    iniciox = int(input("Ingresa coordenadas de inicio x: "))
    inicioy = int(input("Ingresa coordenadas de inicio y: "))
    base = int(input("Ingresa tamaño de la base: "))
    altura = int(input("Ingresa tamaño de la altura: "))
    base = base-1
    altura = altura -1
    matriz.append([])
    matriz[0].append(iniciox)
    matriz[0].append(inicioy)
    matriz.append([])
    matriz[1].append(iniciox + base)
    matriz[1].append(inicioy + altura)
    matriz.append([])
    matriz[2].append(iniciox + base)
    matriz[2].append(inicioy)
    
    plt.xlim([iniciox-2, (iniciox+base)+2])
    plt.ylim([inicioy-2, (inicioy+altura)+2])

def llenadoMatrizTrianguloIsoceles():
    iniciox = int(input("Ingresa coordenadas de inicio x: "))
    inicioy = int(input("Ingresa coordenadas de inicio y: "))
    altura = int(input("Ingresa tamaño de altura: "))
    altura = altura -1
    matriz.append([])
    matriz[0].append(iniciox)
    matriz[0].append(inicioy)
    matriz.append([])
    matriz[1].append(iniciox + altura)
    matriz[1].append(inicioy + altura)
    matriz.append([])
    matriz[2].append(iniciox + (altura*2))
    matriz[2].append(inicioy)
    
    plt.xlim([iniciox-2, (iniciox+(altura*2))+2])
    plt.ylim([inicioy-2, (inicioy+altura)+2])
    
def DDAs(x1, y1, x2, y2):
    x=x2-x1
	y=y2-y1
	m=x1
	n=y1
	if x>y:
		pp=1/x
	else: 
        pp=1/y
	while m<=x2 & n<=y2:
		m=m+pp*x
		n=n+pp*y
        print(m, "   ", n)
		x1=m
		y1=n


def DDA(x1, y1, x2, y2):   
    dx = abs(x2-x1)
    dy = abs(y2-y1)

    if dx > dy:
        steps = dx
    else: 
        steps = dy

    xInc = round((dx/steps), 2)
    yInc = round((dy/steps), 2)
    
    for i in range(0, steps+1):
        rect1 = matplotlib.patches.Rectangle((round(x1), round(y1)),1, 1,linewidth=1, edgecolor='b', facecolor='none')
        ax.add_patch(rect1)
        x1 += xInc 
        y1 += yInc   
        print (round(x1), '  ', round(y1)) 

def graficacion(aristas, metodo):
    resultado=[]
    for f in range(aristas):
        if f == aristas-1:
            if metodo == 1:
                DDA(matriz[f][0], matriz[f][1], matriz[0][0], matriz[0][1])
            else:
                valores = list(bresenham(matriz[f][0], matriz[f][1], matriz[0][0], matriz[0][1]))
                resultado+=valores

        else:
            if metodo == 1:
                DDA(matriz[f][0], matriz[f][1], matriz[f+1][0], matriz[f+1][1])
            else:
                valores = list(bresenham(matriz[f][0], matriz[f][1], matriz[f+1][0], matriz[f+1][1]))
                resultado+=valores
            
    for i in resultado:
        rect1 = matplotlib.patches.Rectangle((i),1, 1,linewidth=1, edgecolor='b', facecolor='none')
        ax.add_patch(rect1)
  
if __name__ == "__main__": 
    figura = int(input("Ingrese el numero de figura a trazar:\n1._ Cuadrado \n2._ Rectangulo\n3._ Triangulo Isoceles \n4._ Triangulo Rectangulo:\n"))
    metodo = int(input("Ingrese el medoto a utilizar\n1.DDA\n2.Bresenham:\n"))
    if metodo == 1:
        plt.title('METODO DDA')
    else: 
        plt.title('METODO BRESENHAMS') 
    if figura == 1:
        llenadoMatrizCuadrado()
        graficacion(4, metodo)
    elif figura == 2:
        llenadoMatrizRectangulo()
        graficacion(4, metodo)
    elif figura == 3:
        llenadoMatrizTrianguloIsoceles()
        graficacion(3, metodo)
    elif figura == 4:
        llenadoMatrizTrianguloRectangulo()
        graficacion(3, metodo)
    plt.show()