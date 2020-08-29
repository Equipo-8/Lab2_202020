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
from Sorting import mergesort as me

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

def encontrar_buenas_peliculas(peliculas,casting,director):
    iteradorcasting=it.newIterator(casting)
    idmovies=[]
    goodmovies=[0,0]
    position=0
    while it.hasNext(iteradorcasting):
        movie=it.next(iteradorcasting)
        if director.lower() == movie["director_name"].lower():
            idmovies.append(position)
        position+=1
    for each in idmovies:
        movie=lt.getElement(peliculas,each)
        if float(movie["vote_average"])>=6.0:
            goodmovies[0]+=1
            goodmovies[1]+=float(movie["vote_average"])
    goodmovies[1]=round(goodmovies[1]/goodmovies[0],2)
    return goodmovies

def ordenarAverageAsc(mov1:dict,mov2:dict)->bool:
    if float(mov1['vote_average'])>float(mov2['vote_average']):
        return True
    return False
def ordenarAverageDesc(mov1:dict,mov2:dict)->bool:
    if float(mov1['vote_average'])<float(mov2['vote_average']):
        return True
    return False
def ordenarCountAsc(mov1:dict,mov2:dict)->bool:
    if float(mov1['vote_count'])>float(mov2['vote_count']):
        return True
    return False
def ordenarCountDesc(mov1:dict,mov2:dict)->bool:
    if float(mov1['vote_count'])<float(mov2['vote_count']):
        return True
    return False


def crear_ranking_peliculas(peliculas,n_peliculas,CoA,ascOdesc):
    lista_return=[]
    iterador=it.newIterator(peliculas)
    if CoA == True:
        if ascOdesc == True:
            me.mergesort(peliculas,ordenarCountAsc)
        elif ascOdesc == False:
             me.mergesort(peliculas,ordenarCountDesc)   
    elif CoA== False:
        if ascOdesc ==True:
            me.mergesort(peliculas,ordenarAverageAsc)
        elif ascOdesc == False:
             me.mergesort(peliculas, ordenarAverageDesc)
    while n_peliculas != -1 and it.hasNext(iterador):
            n_peliculas-= 1
            movie = it.next(iterador)
            lista_return.append(movie)
    return lista_return

def entender_genero(peliculas,genero):
    promedio_y_peliculas=[0,0,[]]
    iteradorpeliculas= it.newIterator(peliculas)

    while it.hasNext(iteradorpeliculas):
        pelicula=it.next(iteradorpeliculas)
        if genero.lower() in pelicula["genres"].lower():
            promedio_y_peliculas[2].append(pelicula)
            promedio_y_peliculas[0]+=1
            promedio_y_peliculas[1]+=float(pelicula["vote_average"])
    promedio_y_peliculas[1]=promedio_y_peliculas[1]/promedio_y_peliculas[0]
    return promedio_y_peliculas


def crear_ranking_genero(peliculas,n_peliculas,genero,CoA,ascOdesc):
    lista_ranking=[0,0,[]]
    iterador=it.newIterator(peliculas)
    if CoA == True:
        if ascOdesc == True:
            me.mergesort(peliculas,ordenarCountAsc)
        elif ascOdesc == False:
             me.mergesort(peliculas,ordenarCountDesc)   
    elif CoA== False:
        if ascOdesc ==True:
            me.mergesort(peliculas,ordenarAverageAsc)
        elif ascOdesc == False:
             me.mergesort(peliculas, ordenarAverageDesc)
    while n_peliculas != -1 and it.hasNext(iterador):
            pelicula=it.next(iterador)
            if genero.lower() in pelicula["genres"].lower():
                n_peliculas-= 1
                lista_ranking[2].append(pelicula)
                lista_ranking[0]+=1
                lista_ranking[1]+=float(pelicula["vote_average"])
    lista_ranking[1]=lista_ranking[1]/lista_ranking[0]
    return lista_ranking
                
        
           
        



         

    
        
            


    


    




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
                listacasting = loadCSVFile("Data/MoviesCastingRaw-small.csv") #llamar funcion cargar datos
                print("Datos cargados, ",listacasting['size']," elementos cargados")
            elif int(inputs[0])==2: #opcion2
                 listamovies = loadCSVFile("Data/SmallMoviesDetailsCleaned.csv")
                 print("Datos cargados, ",listamovies['size']," elementos cargados")
            elif int(inputs[0])==3:#opcion3
                if listacasting == None or listamovies == None:
                    print("esta lista esta vacia:(" )
                else: 
                    director=input("Inserta el nombre del director a consultar: ")
                    goodmovies=encontrar_buenas_peliculas(listamovies,listacasting,director)
                    print("Las buenas películas de "+director+" son: "+str(goodmovies[0]))
                    print("El ranking promedio de las mismas es: "+str(goodmovies[1]))
            elif int(inputs[0])==4:#opcion4
                   if listacasting == None or listamovies == None:
                        print("esta lista esta vacia:(" )
                   else:
                        cantidad = int(input("escriba la cantidad de películas que quiere en el ranking, debe ser mayor o igual a 10: "))                        
                        while 10>cantidad:
                            print("la cantidad debe ser mayor a 10.")
                            cantidad=int(input("Escriba la cantidad de peliculas que quiere en el ranking: "))
                        AoC=input("Escriba Averague, de lo contrario escriba Count: ").title()
                        ascOdesc= input("Segun el orden que quiera escriba ascendente o descendente: ").title()
                        if AoC == "Averague":
                            if ascOdesc == "Ascendente":
                                lista_final=crear_ranking_peliculas(listamovies,cantidad,False,False)
                            elif ascOdesc == "Descendente":
                                lista_final=crear_ranking_peliculas(listamovies,cantidad,False,True)                           
                        elif AoC == "Count":
                            if ascOdesc == "Ascendente":
                                lista_final=crear_ranking_peliculas(listamovies,cantidad,True,False)
                            elif ascOdesc == "Descendente":
                                lista_final=crear_ranking_peliculas(listamovies,cantidad,True,True)
                        if len(lista_final)>0:
                            print("El ranking de películas es: ",lista_final)
                          
            elif int(inputs[0])==5:#opcion5
                 if listacasting == None or listamovies == None:
                     print("esta lista esta vacia:(" )
                 else: 
                      print(None)
                        
                                        


                     
            elif int(inputs[0])==6:#opcion6
                if listacasting == None or listamovies == None:
                     print("esta lista esta vacia:(" )
                else: 
                     genero=input("Digite el genero de la película: ").title()                
                     entender_genero1=entender_genero(listamovies,genero)
                     print("El numero de peliculas encontradas es de: ",entender_genero1[0])
                     print("El promedio de la votacion de las películas es de: ",entender_genero1[1])
                     listasn=input("Si quiere que se muestre en pantalla l lista de películas, presione S, de lo contratio presione n: ").lower()
                     if listasn == "s":
                         print("La lista de las películas es la siguiente: ",entender_genero1[2])

                     elif listasn== "n":
                         print(None)
            elif int(inputs[0])==7:#opcion7
                 if listacasting == None or listamovies == None:
                     print("esta lista esta vacia:(" )
                 else: 
                      cantidad = int(input("escriba la cantidad de películas que quiere en el ranking, debe ser mayor o igual a 10: "))                        
                      genero=input("Escriba el genero con el quiera crear el ranking: ")
                      while 10>cantidad:
                          print("la cantidad debe ser mayor a 10.")
                          cantidad=int(input("Escriba la cantidad de peliculas que quiere en el ranking: "))
                      AoC=input("Escriba Averague, de lo contrario escriba Count: ").title()
                      ascOdesc= input("Segun el orden que quiera escriba ascendente o descendente: ").title()
                      if AoC == "Averague":
                          if ascOdesc == "Ascendente":
                              lista_final=crear_ranking_genero(listamovies,cantidad,genero,False,False)
                          elif ascOdesc == "Descendente":
                              lista_final=crear_ranking_genero(listamovies,cantidad,genero,False,True)                           
                      elif AoC == "Count":
                          if ascOdesc == "Ascendente":
                              lista_final=crear_ranking_genero(listamovies,cantidad,genero,True,False)
                          elif ascOdesc == "Descendente":
                              lista_final=crear_ranking_genero(listamovies,cantidad,genero,True,True)
                      if len(lista_final) >0:
                          print("El número de las películas encontradas del genero, ",genero,"fue de: ",lista_final[0])
                          print("El promedio de la votación de las mismas fue de: ",lista_final[1])
                          print("Y el ranking es este: ",lista_final[2])
                      
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