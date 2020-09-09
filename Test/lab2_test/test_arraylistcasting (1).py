import config
import pytest
from DataStructures import arraylist as slt



def cmpfunction (element1, element2):
    if element1["id"] == element2["id"]:
        return 0
    elif element1["id"] < element2["id"]:
        return -1
    else:
        return 1


@pytest.fixture
def lst ():
    lst = slt.newList(cmpfunction)
    return lst


@pytest.fixture
def casting():
    casting=[]
    archivo=open("Data/AllMoviesCastingRaw.csv","r",encoding="utf-8")
    linea_1=archivo.readline()
    titles=linea_1.split(";")
    linea=archivo.readline()
    while len(linea)>0:
        datos=linea.split(";")
        dicto={}
        dicto
        for i in range(0,19):
            dicto[titles[i]]=datos[i]
        casting.append(dicto)
        linea=archivo.readline()
    archivo.close()
    return casting


@pytest.fixture
def lstcasting(casting):
    lst = slt.newList(cmpfunction)
    for each in casting:    
        slt.addLast(lst,each)    
    return lst



def test_empty (lst):
    assert slt.isEmpty(lst) == True
    assert slt.size(lst) == 0



def test_addFirst (lst, casting):
    assert slt.isEmpty(lst) == True
    assert slt.size(lst) == 0
    slt.addFirst (lst, casting[1])
    assert slt.size(lst) == 1
    slt.addFirst (lst, casting[2])
    assert slt.size(lst) == 2
    cast = slt.firstElement(lst)
    assert cast == casting[2]




def test_addLast (lst, casting):
    assert slt.isEmpty(lst) == True
    assert slt.size(lst) == 0
    slt.addLast (lst, casting[1])
    assert slt.size(lst) == 1
    slt.addLast (lst, casting[2])
    assert slt.size(lst) == 2
    cast = slt.firstElement(lst)
    assert cast == casting[1]
    cast = slt.lastElement(lst)
    assert cast == casting[2]




def test_getElement(lstcasting, casting):
    cast = slt.getElement(lstcasting, 1)
    assert cast == casting[0]
    cast = slt.getElement(lstcasting, 5)
    assert cast == casting[4]





def test_removeFirst (lstcasting, casting):
    assert slt.size(lstcasting) == len(casting)
    slt.removeFirst(lstcasting)
    assert slt.size(lstcasting) == len(casting)-1
    cast = slt.getElement(lstcasting, 1)
    assert cast  == casting[1]



def test_removeLast (lstcasting, casting):
    assert slt.size(lstcasting) == len(casting)
    slt.removeLast(lstcasting)
    assert slt.size(lstcasting) == len(casting)-1
    cast = slt.getElement(lstcasting, len(casting)-1)
    assert cast  == casting[len(casting)-2]



def test_insertElement (lst, casting):
    assert slt.isEmpty(lst) is True
    assert slt.size(lst) == 0
    slt.insertElement (lst, casting[0], 1)
    assert slt.size(lst) == 1
    slt.insertElement (lst, casting[1], 2)
    assert slt.size(lst) == 2
    slt.insertElement (lst, casting[2], 1)
    assert slt.size(lst) == 3
    cast = slt.getElement(lst, 1)
    assert cast == casting[2]
    cast = slt.getElement(lst, 2)
    assert cast == casting[0]



def test_isPresent (lstcasting, casting):
    cast = {'id': '31212432412431412132', 'budget': '0', 'genres': 'Drama|Crime', 'imdb_id': 'tt0094675', 'original_language': 'fi', 'original_title': 'Ariel', 'overview': "Taisto Kasurinen is a Finnish coal miner whose father has just committed suicide and who is framed for a crime he did not commit. In jail, he starts to dream about leaving the country and starting a new life. He escapes from prison but things don't go as planned...", 'popularity': '0.823904', 'production_companies': 'Villealfa Filmproduction Oy', 'production_countries': 'Finland', 'release_date': '21/10/1988', 'revenue': '0', 'runtime': '69', 'spoken_languages': 'suomi', 'status': 'Released', 'tagline': '', 'title': 'Ariel', 'vote_average': '7.1', 'vote_count': '40', 'production_companies_number': '2', 'spoken_languages_number': '2'}
    print(slt.isPresent (lstcasting, casting[2]))
    assert slt.isPresent (lstcasting, casting[2]) > 0
    assert slt.isPresent (lstcasting, cast) == 0
    


def test_deleteElement (lstcasting, casting):
    pos = slt.isPresent (lstcasting, casting[2])
    assert pos > 0
    cast = slt.getElement(lstcasting, pos)
    assert cast == casting[2]
    slt.deleteElement (lstcasting, pos)
    assert slt.size(lstcasting) == len(casting)-1
    cast = slt.getElement(lstcasting, pos)
    assert cast == casting[3]


def test_changeInfo (lstcasting):
    cast10 = {'id': '31212432412431412132', 'budget': '0', 'genres': 'Drama|Crime', 'imdb_id': 'tt0094675', 'original_language': 'fi', 'original_title': 'Ariel', 'overview': "Taisto Kasurinen is a Finnish coal miner whose father has just committed suicide and who is framed for a crime he did not commit. In jail, he starts to dream about leaving the country and starting a new life. He escapes from prison but things don't go as planned...", 'popularity': '0.823904', 'production_companies': 'Villealfa Filmproduction Oy', 'production_countries': 'Finland', 'release_date': '21/10/1988', 'revenue': '0', 'runtime': '69', 'spoken_languages': 'suomi', 'status': 'Released', 'tagline': '', 'title': 'Ariel', 'vote_average': '7.1', 'vote_count': '40', 'production_companies_number': '2', 'spoken_languages_number': '2'}
    slt.changeInfo (lstcasting, 1, cast10)
    cast = slt.getElement(lstcasting, 1)
    assert cast10 == cast


def test_exchange (lstcasting, casting):
    cast1 = slt.getElement(lstcasting, 1)
    cast5 = slt.getElement(lstcasting, 5)
    slt.exchange (lstcasting, 1, 5)
    assert slt.getElement(lstcasting, 1) == cast5
    assert slt.getElement(lstcasting, 5) == cast1