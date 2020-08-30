"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""

import config as cf
import sys
import csv
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt

from time import process_time 


def loadCSVFile (file, sep=";"):
    """
    Carga un archivo csv a una lista
    Args:
        file
            Archivo csv del cual se importaran los datos
        sep = ";"
            Separador utilizado para determinar cada objeto dentro del archivo
        Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None  
    """
    lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    #lst = lt.newList() #Usando implementacion linkedlist
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst,row)
    except:
        print("Hubo un error con la carga del archivo")
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return lst

def encontrar_buenas_peliculas(peliculas,casting,director,needoflist):
    iteradorcasting=it.newIterator(casting)
    idmovies=[]
    goodmovies=[0,0,[]]
    position=0
    while it.hasNext(iteradorcasting):
        movie=it.next(iteradorcasting)
        if director.lower() == movie["director_name"].lower():
            idmovies.append(position)
        position+=1
    for each in idmovies:
        movie=lt.getElement(peliculas,each)
        if not needoflist:
            if float(movie["vote_average"])>=6.0:
                goodmovies[0]+=1
                goodmovies[1]+=float(movie["vote_average"])
        elif needoflist:
            goodmovies[0]+=1
            goodmovies[1]+=float(movie["vote_average"])
            goodmovies[2].append(movie)
    goodmovies[1]=round(goodmovies[1]/goodmovies[0],2)
    return goodmovies

def conocer_autor(peliculas,casting,actor):
    iteradorcasting=it.newIterator(casting)
    idmovies=[]
    most=["DirectorName",0]
    moviesautor=[0,0,[],{}]
    position=0
    while it.hasNext(iteradorcasting):
        movie=it.next(iteradorcasting)
        if actor == movie["actor1_name"] or actor == movie["actor2_name"] or actor == movie["actor3_name"] or actor == movie["actor4_name"] or actor == movie["actor5_name"]:
            idmovies.append((position,movie["director_name"]))
        position+=1
    for each in idmovies:
        movie=lt.getElement(peliculas,each[0])
        moviesautor[0]+=1
        moviesautor[1]+=float(movie["vote_average"])
        moviesautor[2].append(movie)
        if each[1] in moviesautor[3]:
            moviesautor[3][each[1]]+=1
        else:
            moviesautor[3][each[1]]=1 
        if moviesautor[3][each[1]]>most[1]:
            most[0]=each[1]
            most[1]=moviesautor[3][each[1]]
    moviesautor[1]=round(moviesautor[1]/moviesautor[0],2)
    return [moviesautor[0],moviesautor[1],moviesautor[2],most[0]]

def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos Movies Casting")
    print("2- Cargar Datos Movies Details")
    print("3- Cargar buenas películas")
    print("4- Crear ranking de películas")
    print("5- Conocer a un director")
    print("5- conocer a un actor")
    print("6- Entender un género cinematográgico")
    print("7- Crear ranking del género")
    print("8- Contar los elementos de la Lista")
    print("9- Contar elementos filtrados por palabra clave")
    print("10- Consultar elementos a partir de dos listas")
    print("0- Salir")

def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    Args:
        criteria:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        list
            Lista en la cual se realizará el conteo, debe estar inicializada
    Return:
        counter :: int
            la cantidad de veces ue aparece un elemento con el criterio definido
    """
    if lst['size']==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0
        iterator = it.newIterator(lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            if criteria.lower() in element[column].lower(): #filtrar por palabra clave 
                counter+=1           
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

def countElementsByCriteria(criteria, column, lst):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    return 0

def orderElementsByCriteria(function, column, lst, elements):
    """
    Retorna una lista con cierta cantidad de elementos ordenados por el criterio
    """
    return 0
def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    listacasting = None   # se require usar lista definida
    listamovies = None
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                listacasting = loadCSVFile("Data/AllMoviesCastingRaw.csv") #llamar funcion cargar datos
                print("Datos cargados, ",listacasting['size']," elementos cargados")
            elif int(inputs[0])==2: #opcion2
                 listamovies = loadCSVFile("Data/AllMoviesDetailsCleaned.csv")
                 print("Datos cargados, ",listamovies['size']," elementos cargados")
            elif int(inputs[0])==3:#opcion3
                if listacasting == None or listamovies == None:
                    print("esta lista esta vacia:(" )
                else: 
                    director=input("Inserta el nombre del director a consultar: ")
                    goodmovies=encontrar_buenas_peliculas(listamovies,listacasting,director,False)
                    print("Las buenas películas de "+director+" son: "+str(goodmovies[0]))
                    print("El ranking promedio de las mismas es: "+str(goodmovies[1]))
            elif int(inputs[0]==4):#opcion4
                   if listacasting == None or listamovies == None:
                        print("esta lista esta vacia:(" )
                   else: 
                         print("El ranking de películas es: ", listacasting) 
            elif int(inputs[0]==5):#opcion5
                 if listacasting == None or listamovies == None:
                     print("esta lista esta vacia:(" )
                 else: 
                     print("Los datos del actor son: ", lista)
            elif int(inputs[0]==6):#opcion6
                 if listacasting == None or listamovies == None:
                     print("esta lista esta vacia:(" )
                 else: 
                     print("Las caracteristicas del geénero son: ", lista)
            elif int(inputs[0])==7:#opcion7
                 if listacasting == None or listamovies == None:
                     print("esta lista esta vacia:(" )
                 else: 
                     print("La lista con el ranking del género es: ", lista)
            elif int(inputs[0])==8:#opcion8
                if listacasting==None or listamovies==None or listacasting['size']==0 or listamovies['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")    
                else: print("La lista tiene ",lista['size']," elementos")
            elif int(inputs[0])==9: #opcion 9
                if listacasting==None or listamovies==None or listacasting['size']==0 or listamovies['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:   
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    counter=countElementsFilteredByColumn(criteria, "nombre", lista) #filtrar una columna por criterio  
                    print("Coinciden ",counter," elementos con el crtierio: ", criteria  )
            elif int(inputs[0])==10: #opcion 10
                if listacasting==None or listamovies==None or listacasting['size']==0 or listamovies['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    counter=countElementsByCriteria(criteria,0,lista)
                    print("Coinciden ",counter," elementos con el crtierio: '", criteria ,"' (en construcción ...)")
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()