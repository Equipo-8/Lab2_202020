"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
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


import pytest
import config
from Sorting import insertionsort as sort
from DataStructures import listiterator as it
from ADT import list as slt

#list_type = 'ARRAY_LIST'
list_type = 'SINGLE_LINKED'

def cmpfunction (element1, element2):
    if element1 == element2:
        return 0

def peliculas():
    peliculas=[]
    archivo=open("Data/SmallMoviesDetailsCleaned.csv","r",encoding="utf-8")
    linea_1=archivo.readline()
    titles=linea_1.split(";")
    linea=archivo.readline()
    while len(linea)>0:
        datos=linea.split(";")
        dicto={}
        dicto["id"]=datos[0]
        for i in range(1,20):
            dicto[titles[i]]=datos[i]
        dicto[titles[21]]= datos[21].replace("\n","")
        peliculas.append(dicto)
        linea=archivo.readline()
    archivo.close()
    return peliculas

def lstpeliculas(peliculas):
    lst = slt.newList()
    for each in peliculas:
        slt.addLast(lst,each)  
    return lst

movies=peliculas()
lstmovies=lstpeliculas(movies)



def less(element1, element2):
    if int(element1['id']) < int(element2['id']):
        return True
    return False

def greater(element1, element2):
    if int(element1['id']) > int(element2['id']):
        return True
    return False


def test_less():
    lst=lstmovies
    print("Ordenando lista de manera ascendente:----------------------------------------------------")
    iterator = it.newIterator(lst)
    while it.hasNext(iterator):
        element = it.next(iterator)
        result = "".join(str(key) + ": " + str(value) +
                         ",  " for key, value in element.items())
        print(result)
    print("sorting ....")
    sort.insertionSort(lst, less)

    
def test_greater():
    lst=lstmovies
    print("Ordenando lista por de manera descendente:----------------------------------------------------")
    iterator = it.newIterator(lst)
    while it.hasNext(iterator):
        element = it.next(iterator)
        result = "".join(str(key) + ": " + str(value) +
                         ",  " for key, value in element.items())
        print(result)
    print("sorting ....")
    sort.insertionSort(lst, greater)