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

listamovies=(loadCSVFile("Data/AllMoviesDetailsCleaned.csv"))
listacasting=(loadCSVFile("Data/AllMoviesCastingRaw.csv"))
director="Quentin Tarantino"


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
print(conocer_autor(listamovies,listacasting,"Marisa Tomei"))