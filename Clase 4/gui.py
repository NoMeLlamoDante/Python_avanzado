from unittest import TextTestResult


class Ventana: 
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.puede_cerrarse = False
        self.puede_minimizarse = False
        self.puede_maximizarse = False
        self.elementos = []

    def obtener_tamanio(self):
        return [self.ancho, self.alto]

    def agregar_elemento(self, elemento, x, y):
        self.elementos.append([elemento, x, y])

    def pintar_ventana(self):
        texto_ventana = []
        #Creamos la ventana
        for i in range(self.alto):
            #Marco Sup e Inferior
            if i == 0 or i == (self.alto -1):
                texto_ventana.append("*" * self.ancho)
            #Resto de la ventana
            else:
                texto_ventana.append("*"+str(i%10)*(self.ancho-2)+"*")
        #Recorre Lista de elementos
        for j in range(len(self.elementos)):
            #Obtiene elemento
            elemento = self.elementos[j][0]
                #ancho
                #alto
                #texto
            #posición del elemento
            posX = self.elementos[j][1]
            posY = self.elementos[j][2]
            #Reemplaza prints por el elemento
            for k in range(elemento.alto):
                #obtiene linea en acorde al indice:
                linea_original = texto_ventana[posY+k]
                #Marco Superior e inferior
                if k == 0 or k == (elemento.alto -1):
                    #Substring Antes de reemplazar
                    linea_de_reemplazo = linea_original[:posX]
                    #reemplazo de texto
                    linea_de_reemplazo+= "*"*elemento.ancho
                    #Substring Posterior
                    linea_de_reemplazo+= linea_original[posX+elemento.ancho:]
                #Resto del elemento
                else:
                    #Substring Antes de reemplazar
                    linea_de_reemplazo = linea_original[:posX]
                    #reemplazo de texto
                    linea_de_reemplazo+= "*"+" "*(elemento.ancho-2)+"*"
                    #Substring Posterior
                    linea_de_reemplazo+= linea_original[posX+elemento.ancho:]
                
                #Borrar la anterior
                del texto_ventana[posY+k]
                #Insertar la linea nueva
                texto_ventana.insert(posY+k,linea_de_reemplazo)
                    
                    #texto_ventana.append("*"+" "*(elemento.ancho-2)+"*")
                #print(linea_nueva);
                #Marco Sup e Inferior
                #if k == 0 or k == (elemento.alto -1):
                #    texto_ventana.append("*" * elemento.ancho)
                #Resto del elemento
                #else:
                #    texto_ventana.append("*"+" "*(elemento.ancho-2)+"*")


        

        #Imprimimos la ventana
        for i in range(len(texto_ventana)):
            print(texto_ventana[i]);
               
            
        #for i in range(self.texto_ventana):
        #    print(texto_ventana[i])



class Boton: 
    def __init__(self, ancho, alto, texto):
        self.ancho = ancho
        self.alto = alto
        self.texto = texto

    def obtener_tamanio(self):
        return [self.ancho, self.alto]


    
ventana = Ventana(20,12)
boton_cerrar = Boton(5, 4, 'cerrar')
boton_abrir = Boton(6, 3, 'abrir')
ventana.agregar_elemento(boton_cerrar,3,4)
ventana.agregar_elemento(boton_abrir,10,7)
ventana.pintar_ventana()

#print(boton_cerrar.obtener_tamanio())
#print(ventana.obtener_tamanio())

