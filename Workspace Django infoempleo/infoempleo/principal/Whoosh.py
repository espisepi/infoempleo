import os
import urllib
from bs4 import BeautifulSoup
import sqlite3 
import Tkinter
from Tkinter import *
import tkMessageBox
from whoosh.index import create_in,open_dir
from whoosh.fields import Schema, TEXT, KEYWORD
from whoosh.qparser import QueryParser
from bs4 import BeautifulSoup


dirindex="Index"

def extraer():
    url = "https://www.infoempleo.com/trabajo/en_sevilla/area-de-empresa_ingenieria-y-produccion//"
    html = urllib.urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    print soup
     

def indexar():
    if not os.path.exists(dirindex):
            os.mkdir(dirindex)
    diccionario_prueba = {{'Titulo1','Funciones1','Requisitos1','Area1','Categoria1','Vacantes1','Jornada1','Contrato1', 'Retribucion1','Experiencia1'},{'Titulo2','Funciones2','Requisitos2','Area2','Categoria2','Vacantes2','Jornada2','Contrato2', 'Retribucion2', 'Experiencia2'}}
    lista_completa= diccionario_prueba
    ix = create_in(dirindex, schema=get_schema()) #crea el indice y el esquema, que se almacena con el indice (lo que se indexa se puede buscar)
    writer = ix.writer() #'escribe' el indice
    for elemento in lista_completa:
        writer.add_document(titulo=elemento[0],funciones = elemento[1],requisitos = elemento[2],area =elemento[3], categoria= elemento[4], vacantes = elemento[5], jornada = elemento[6], contrato = elemento[7], retribucion = elemento[8], experiencia=[9])
    tkMessageBox.showinfo("Fin de indexado", "Se han indexado "+str(len(lista_completa))+ " trabajos")
            
    writer.commit()
    
def get_schema():
    return Schema(title=TEXT(stored=True), funciones=TEXT(stored=True), requisitos=TEXT(stored=True), area=TEXT(stored=True), categoria=TEXT(stored=True), vacantes=TEXT(stored=True), jornada=TEXT(stored=True), contrato=TEXT(stored=True), retribucion=TEXT(stored=True), experiencia=TEXT(stored=True))

def ventana_principal():
    top = Tk()
    boton_indexar = Button(top, text="Indexar", command = indexar)
    boton_indexar.pack(side = TOP)
#     Buscar = Button(top, text="Buscar por Rtte", command = buscar_titulo)
#     Buscar.pack(side = TOP)
    top.mainloop()
ventana_principal()