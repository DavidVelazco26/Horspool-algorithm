import math
from cProfile import label
from scipy.stats import multivariate_normal
from scipy.special import expit
import random
import seaborn as sn
import cv2 as cv
import numpy as np
import pandas as pd
import numpy.linalg as npl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D
from numpy.linalg import eig
import math as ma

#funcion de fracaso
def fracaso(b): # calcula y retorna función de fracaso para patrón b
  d={}
  for i in range (0,len(b)-1):
    d[b[i]]=i
  return d
def horspool(a,b): #Algoritmo de Horspool
    g=fracaso(b)
    n=len(a)
    m=len(b)
    r=[]
    k=m-1
    j=m-1
    while k<n:
        if j<0:
            r+=[k-m+1]
            j=m-1
            k+=1
            if k>=n:
                break
        if a[k-(m-1-j)]==b[j]:
            j=j-1
        else:
            k=k+(m-1-g.get(a[k],-1))
            j=m-1
    return r
#Lectura de los archivos txt
with open('./Ama y no sufras - Walter Riso (7 files merged).txt', encoding="utf8") as archivo1:
  leer1=archivo1.read()
with open('./Amar o depender - Walter Riso.txt', encoding="utf8") as archivo2:
  leer2=archivo2.read()
with open('./Amar o depender cómo superar el apego afectivo - Walter Riso.txt',encoding="utf8") as archivo3:
  leer3=archivo3.read()
with open('./Amor divina locura - Walter Riso.txt',encoding="utf8") as archivo4:
  leer4=archivo4.read()
with open('./Amores altamente peligrosos - Walter Riso.txt',encoding="utf8") as archivo5:
  leer5=archivo5.read()
with open('./Cuestión de dignidad_ El derecho a decir NO - Walter Riso.txt',encoding="utf8") as archivo6:
  leer6=archivo6.read()
with open('./Deshojando margaritas.txt',encoding="utf8") as archivo7:
  leer7=archivo7.read()
with open('./El camino de los sabios_ Filosofía para la vida cotidiana - Walter Riso.txt',encoding="utf8") as archivo8:
  leer8=archivo8.read()
with open('./Enamorados-o-esclavizados.txt',encoding="utf8") as archivo9:
  leer9=archivo9.read()
with open('./Enamorate-de-ti.txt',encoding="utf8") as archivo10:
  leer10=archivo10.read()
with open('./Guía práctica para descubrir el poder sanador de las emociones - Walter Riso',encoding="utf8") as archivo11:
  leer11=archivo11.read()
with open('./Guía práctica para mejorar la autoestima - Walter Riso.txt',encoding="utf8") as archivo12:
  leer12=archivo12.read()
with open('./La fidelidad es mucho más que amor.txt',encoding="utf8") as archivo13:
  leer13=archivo13.read()
with open('./Las mayores estupideces que hacemos por amor.txt',encoding="utf8") as archivo14:
  leer14=archivo14.read()
with open('./Los-caminos-del-perdón.txt',encoding="utf8") as archivo15:
  leer15=archivo15.read()
with open('./Los-límites-del-amor.txt',encoding="utf8") as archivo16:
  leer16=archivo16.read()
with open('./Manifiesto-para-la-liberación-afectiva.txt',encoding="utf8") as archivo17:
  leer17=archivo17.read()
with open('./Maravillosamente-imperfecto.txt',encoding="utf8") as archivo18:
  leer18=archivo18.read()
with open('./Pensar bien, sentirse bien.txt',encoding="utf8") as archivo19:
  leer19=archivo19.read()
librostxt=[leer1,leer2,leer3,leer4,leer5,leer6,leer7,leer8,leer9,leer10,leer11,leer12,leer13,leer14,leer15,leer16,leer17,leer18,leer19]





