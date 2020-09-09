import config
import pytest 
from DataStructures import arraylist as slt





def cmpfunction (element1, element2):
    if element1 ["\ufeffid"]== element2["\ufeffid"]:
        return 0
    elif element1["\ufeffid"] < element2["\ufeffid"]:
        return -1
    else:
        return 1


@pytest.fixture
def lst ():
    lst = slt.newList(cmpfunction)
    return lst


@pytest.fixture
def peliculas():
    peliculas=[]
    archivo=open("Data/AllMoviesDetailsCleaned.csv","r",encoding="utf-8")
    linea_1=archivo.readline()
    titles=linea_1.split(";")
    linea=archivo.readline()
    while len(linea)>0:
        datos=linea.split(";")
        dicto={}
        for i in range(0,20):
            dicto[titles[i]]=datos[i]
        dicto[titles[21]]= datos[21].replace("\n","")
        peliculas.append(dicto)
        linea=archivo.readline()
    archivo.close()
    return peliculas


@pytest.fixture
def lstpeliculas(peliculas):
    lst = slt.newList(cmpfunction)
    for each in peliculas:    
        slt.addLast(lst,each)    
    return lst



def test_empty (lst):
    assert slt.isEmpty(lst) == True
    assert slt.size(lst) == 0



def test_addFirst (lst, peliculas):
    assert slt.isEmpty(lst) == True
    assert slt.size(lst) == 0
    slt.addFirst (lst, peliculas[1])
    assert slt.size(lst) == 1
    slt.addFirst (lst, peliculas[2])
    assert slt.size(lst) == 2
    pelicula = slt.firstElement(lst)
    assert pelicula == peliculas[2]




def test_addLast (lst, peliculas):
    assert slt.isEmpty(lst) == True
    assert slt.size(lst) == 0
    slt.addLast (lst, peliculas[1])
    assert slt.size(lst) == 1
    slt.addLast (lst, peliculas[2])
    assert slt.size(lst) == 2
    pelicula = slt.firstElement(lst)
    assert pelicula == peliculas[1]
    pelicula = slt.lastElement(lst)
    assert pelicula == peliculas[2]




def test_getElement(lstpeliculas, peliculas):
    pelicula = slt.getElement(lstpeliculas, 1)
    assert pelicula == peliculas[0]
    pelicula = slt.getElement(lstpeliculas, 5)
    assert pelicula == peliculas[4]





def test_removeFirst (lstpeliculas, peliculas):
    assert slt.size(lstpeliculas) == len(peliculas)
    slt.removeFirst(lstpeliculas)
    assert slt.size(lstpeliculas) == len(peliculas)-1
    pelicula = slt.getElement(lstpeliculas, 1)
    assert pelicula == peliculas[1]



def test_removeLast (lstpeliculas, peliculas):
    assert slt.size(lstpeliculas) == len(peliculas)
    slt.removeLast(lstpeliculas)
    assert slt.size(lstpeliculas) == len(peliculas)-1
    pelicula = slt.getElement(lstpeliculas, 4)
    assert pelicula  == peliculas[3]



def test_insertElement (lst, peliculas):
    assert slt.isEmpty(lst) is True
    assert slt.size(lst) == 0
    slt.insertElement (lst, peliculas[0], 1)
    assert slt.size(lst) == 1
    slt.insertElement (lst, peliculas[1], 2)
    assert slt.size(lst) == 2
    slt.insertElement (lst, peliculas[2], 1)
    assert slt.size(lst) == 3
    pelicula = slt.getElement(lst, 1)
    assert pelicula == peliculas[2]
    pelicula = slt.getElement(lst, 2)
    assert pelicula == peliculas[0]



def test_isPresent (lstpeliculas, peliculas):
    pelicula = {'\ufeffid': '12391238712897', 'budget': '2', 'genres': 'Bachata|Salsa|Romance|Trap Fiction', 'imdb_id': 'tt012938123', 'original_language': 'es', 'original_title': 'El loco', 'overview': "LOCURA.", 'popularity': '10', 'production_companies': 'Bachata INC', 'production_countries': 'Colombia', 'release_date': '26/06/2020', 'revenue': '1239813', 'runtime': '195', 'spoken_languages': 'Locura', 'status': 'Released', 'tagline': 'AAAAAAAAAAAY.', 'title': 'XD', 'vote_average': '10', 'vote_count': '1', 'production_companies_number': '2', 'spoken_languages_number\n': '7'}
    print(slt.isPresent (lstpeliculas, peliculas[2]))
    assert slt.isPresent (lstpeliculas, peliculas[2]) > 0
    assert slt.isPresent (lstpeliculas, pelicula) == 0
    


def test_deleteElement (lstpeliculas, peliculas):
    pos = slt.isPresent (lstpeliculas, peliculas[2])
    assert pos > 0
    pelicula = slt.getElement(lstpeliculas, pos)
    assert pelicula == peliculas[2]
    slt.deleteElement (lstpeliculas, pos)
    assert slt.size(lstpeliculas) == len(peliculas)-1
    pelicula = slt.getElement(lstpeliculas, pos)
    assert pelicula == peliculas[3]


def test_changeInfo (lstpeliculas):
    pelicula10 = {'book_id':'10', 'book_title':'Title 10', 'author':'author 10'}
    slt.changeInfo (lstpeliculas, 1, pelicula10)
    pelicula = slt.getElement(lstpeliculas, 1)
    assert pelicula10 == pelicula


def test_exchange (lstpeliculas, peliculas):
    pelicula1 = slt.getElement(lstpeliculas, 1)
    pelicula5 = slt.getElement(lstpeliculas, 5)
    slt.exchange (lstpeliculas, 1, 5)
    assert slt.getElement(lstpeliculas, 1) == pelicula5
    assert slt.getElement(lstpeliculas, 5) == pelicula1