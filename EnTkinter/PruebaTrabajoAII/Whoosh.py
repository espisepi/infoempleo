#utf-8

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
import BeautifulSoup 
from BeautifulSoup import inicio


dirindex="Index"

def extraer():
    url = "https://www.infoempleo.com/trabajo/en_sevilla/area-de-empresa_ingenieria-y-produccion//"
    html = urllib.urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    print soup
     

def indexar():
    if not os.path.exists(dirindex):
            os.mkdir(dirindex)
    #diccionario_prueba = #{{'Titulo1','Funciones1','Requisitos1','Area1','Categoria1','Vacantes1','Jornada1','Contrato1', 'Retribucion1','Experiencia1'},{'Titulo2','Funciones2','Requisitos2','Area2','Categoria2','Vacantes2','Jornada2','Contrato2', 'Retribucion2', 'Experiencia2'}}
    #lista_completa= scraping("https://www.infoempleo.com/trabajo/en_sevilla/area-de-empresa_ingenieria-y-produccion/")
    lista_completa= inicio()
    ix = create_in(dirindex, schema=get_schema()) #crea el indice y el esquema, que se almacena con el indice (lo que se indexa se puede buscar)
    writer = ix.writer() #'escribe' el indice
    for elemento in lista_completa:
        writer.add_document(titulo=unicode(elemento[0]),funciones = unicode(elemento[1]),requisitos = unicode(elemento[2]),area =unicode(elemento[3]), categoria= unicode(elemento[4]), nvacantes = unicode(elemento[5]), jornada = unicode(elemento[6]), contrato = unicode(elemento[7]), retribucion = unicode(elemento[8]), experiencia=unicode(elemento[9]))
    tkMessageBox.showinfo("Fin de indexado", "Se han indexado "+str(len(lista_completa))+ " trabajos")
            
    writer.commit()
    
def get_schema():
    return Schema(titulo=TEXT(stored=True), funciones=TEXT(stored=True), requisitos=TEXT(stored=True), area=TEXT(stored=True), categoria=TEXT(stored=True), nvacantes=TEXT(stored=True), jornada=TEXT(stored=True), contrato=TEXT(stored=True), retribucion=TEXT(stored=True), experiencia=TEXT(stored=True))



def buscar_titulo():
    def mostrar_lista(event):
        lb.delete(0,END)   #borra toda la lista
        ix=open_dir(dirindex)#Abre el indice  
        with ix.searcher() as searcher:
            '''busca en el campo title del esquema ix.schema lo que introduzcamos por pantalla en el entry 'en' '''
            query = QueryParser("titulo", ix.schema).parse(unicode(en.get())) 
            results = searcher.search(query)
            for r in results:
                lb.insert(END,r['titulo'])
                lb.insert(END,r['funciones'])
                lb.insert(END,r['requisitos'])
                lb.insert(END,r['area'])
                lb.insert(END,r['categoria'])
                lb.insert(END,r['nvacantes'])
                #lb.insert(END,r['jornada'])
                #lb.insert(END,r['contrato'])
                #lb.insert(END,r['retribucion'])
                #lb.insert(END,r['experiencia'])
                lb.insert(END,'')
    v = Toplevel()
    v.title("Busqueda por titulos")
    f =Frame(v)
    f.pack(side=TOP)
    l = Label(f, text="Introduzca el titulo:")
    l.pack(side=LEFT)
    en = Entry(f)
    en.bind("<Return>", mostrar_lista) #cuando haga return se muestre la lista
    en.pack(side=LEFT)
    sc = Scrollbar(v)
    sc.pack(side=RIGHT, fill=Y)
    lb = Listbox(v, yscrollcommand=sc.set)
    lb.pack(side=BOTTOM, fill = BOTH)
    sc.config(command = lb.yview) 
    
def buscar_categoria():
    def mostrar_lista(event):
        lb.delete(0,END)   #borra toda la lista
        ix=open_dir(dirindex)#Abre el indice  
        with ix.searcher() as searcher:
            query = QueryParser("categoria", ix.schema).parse(unicode(en.get())) 
            results = searcher.search(query)
            for r in results:
                lb.insert(END,r['titulo'])
                lb.insert(END,r['funciones'])
                lb.insert(END,r['requisitos'])
                lb.insert(END,r['area'])
                lb.insert(END,r['categoria'])
                lb.insert(END,r['nvacantes'])
                #lb.insert(END,r['jornada'])
                #lb.insert(END,r['contrato'])
                #lb.insert(END,r['retribucion'])
                #lb.insert(END,r['experiencia'])
                lb.insert(END,'')
    v = Toplevel()
    v.title("Busqueda por categorias")
    f =Frame(v)
    f.pack(side=TOP)
    l = Label(f, text="Introduzca una categoria:")
    l.pack(side=LEFT)
    en = Entry(f)
    en.bind("<Return>", mostrar_lista) #cuando haga return se muestre la lista
    en.pack(side=LEFT)
    sc = Scrollbar(v)
    sc.pack(side=RIGHT, fill=Y)
    lb = Listbox(v, yscrollcommand=sc.set)
    lb.pack(side=BOTTOM, fill = BOTH)
    sc.config(command = lb.yview) 
    
def buscar_area():
    def mostrar_lista(event):
        lb.delete(0,END)   #borra toda la lista
        ix=open_dir(dirindex)#Abre el indice  
        with ix.searcher() as searcher:
            query = QueryParser("area", ix.schema).parse(unicode(en.get())) 
            results = searcher.search(query)
            for r in results:
                lb.insert(END,r['titulo'])
                lb.insert(END,r['funciones'])
                lb.insert(END,r['requisitos'])
                lb.insert(END,r['area'])
                lb.insert(END,r['categoria'])
                lb.insert(END,r['nvacantes'])
                #lb.insert(END,r['jornada'])
                #lb.insert(END,r['contrato'])
                #lb.insert(END,r['retribucion'])
                #lb.insert(END,r['experiencia'])
                lb.insert(END,'')
    v = Toplevel()
    v.title("Busqueda por area")
    f =Frame(v)
    f.pack(side=TOP)
    l = Label(f, text="Introduzca un area:")
    l.pack(side=LEFT)
    en = Entry(f)
    en.bind("<Return>", mostrar_lista) #cuando haga return se muestre la lista
    en.pack(side=LEFT)
    sc = Scrollbar(v)
    sc.pack(side=RIGHT, fill=Y)
    lb = Listbox(v, yscrollcommand=sc.set)
    lb.pack(side=BOTTOM, fill = BOTH)
    sc.config(command = lb.yview) 

def ventana_principal():
    top = Tk()
    boton_indexar = Button(top, text="Indexar", command = indexar)
    boton_indexar.pack(side = TOP)
    Buscar = Button(top, text="Buscar por titulo", command = buscar_titulo)
    Buscar.pack(side = TOP)
    Buscar2 = Button(top, text="Buscar por categorias", command = buscar_categoria)
    Buscar2.pack(side = TOP)
    Buscar3 = Button(top, text="Buscar por area", command = buscar_area)
    Buscar3.pack(side = TOP)
    top.mainloop()
ventana_principal()