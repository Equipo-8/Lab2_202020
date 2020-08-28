import config as cf
import sys
import csv
from ADT import list as lt
from DataStructures import arraylistiterator as it
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

listamovies=(loadCSVFile("Data/AllMoviesCastingRaw.csv"))
listacasting=(loadCSVFile("Data/AllMoviesDetailsCleaned.csv"))
director="Quentin Tarantino"


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
print(encontrar_buenas_peliculas(listacasting,director,listamovies))
