#utf-8
'''
Created on 12 ene. 2018

@author: espisepi
'''
import urllib
from bs4 import BeautifulSoup

def extraer(url):
    html = urllib.urlopen(url)
    soup=BeautifulSoup(html,'html.parser')
    return soup

def extraer_trabajo(soup):
    lista_trabajos=[]
    bloques_trabajos=soup.find('ul', {'class' : 'mt15 positions '})
    for trabajo_portada_html in bloques_trabajos.findAll('li'):
        trabajo_portada_html=trabajo_portada_html.find('a')['href']
        if(trabajo_portada_html.startswith('/')):
            #Con este filtro eliminamos los links publicitarios
            url_base='https://www.infoempleo.com'
            trabajo_portada_html=url_base+trabajo_portada_html
            trabajo_soup=extraer(trabajo_portada_html)
            try:
                titulo=trabajo_soup.find('h1').string
            except ValueError:
                break
            try:
                funciones=(trabajo_soup.find('div', {'class' : 'offer'}).findAll('pre')[0]).string
            except:
                funciones='no disponible'
            try:
                requisitos=(trabajo_soup.find('div', {'class' : 'offer'}).findAll('pre')[0]).string
            except:
                requisitos='no disponible'
            try:
                area=trabajo_soup.find('ul', {'class' : 'inline boxes mt30'}).findAll('li')[0].find('p').string
            except:
                area='no disponible'
            try:
                categoria=trabajo_soup.find('ul', {'class' : 'inline boxes mt30'}).findAll('li')[1].find('p').string
            except:
                categoria='no disponible'
            try:
                nvacantes=(trabajo_soup.find('ul', {'class' : 'inline boxes mt30'}).findAll('li')[2].find('p').string).string
            except:
                nvacantes='no disponible'
            try:
                jornada=trabajo_soup.find('p', {'class' : 'small mt10'}).string.split('-')[0].strip().string
            except:
                jornada='no disponible'
            try:
                contrato=trabajo_soup.find('p', {'class' : 'small mt10'}).string.split('-')[1].strip().string
            except:
                contrato='no disponible'
            try:
                retribucion=trabajo_soup.find('p', {'class' : 'small mt10'}).string.split('-')[2].strip().string
            except:
                retribucion='no disponible'
            try:
                experiencia=trabajo_soup.find('p', {'class' : 'small mt10'}).string.split('-')[3].strip().string
            except:
                experiencia='no disponible'
            trabajo=[titulo,funciones,requisitos,area,categoria,nvacantes,jornada,contrato,retribucion,experiencia]   
            lista_trabajos.append(trabajo)
    return lista_trabajos

def scraping(url):
    lista_trabajos_totales=[]
    soup = extraer(url)
    lista_trabajos_totales.extend(extraer_trabajo(soup))
    next=soup.find('li', {'class' : 'next'}).find('a')['href']
    if(not(next==u'javascript:void(0);')):
        scraping(next)
    return lista_trabajos_totales
def inicio():
    url='https://www.infoempleo.com/trabajo/en_sevilla/area-de-empresa_ingenieria-y-produccion/'
    lista_trabajos_totales=scraping(url)
    return lista_trabajos_totales