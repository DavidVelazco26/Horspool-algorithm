import math
import operator
import random
import numpy as np
import pandas as pd
import math as ma
#Definimos el nombre de los libros que serán ocupados
librostxt=['./Ama y no sufras - Walter Riso (7 files merged).txt','./Amar o depender - Walter Riso.txt','./Amar o depender cómo superar el apego afectivo - Walter Riso.txt',
'./Amor divina locura - Walter Riso.txt','./Amores altamente peligrosos - Walter Riso.txt','./Cuestión de dignidad_ El derecho a decir NO - Walter Riso.txt','./Deshojando margaritas.txt',
'./El camino de los sabios_ Filosofía para la vida cotidiana - Walter Riso.txt','./Enamorados-o-esclavizados.txt','./Enamorate-de-ti.txt','./Guía práctica para descubrir el poder sanador de las emociones - Walter Riso.txt',
'./Guía práctica para mejorar la autoestima - Walter Riso.txt','./La fidelidad es mucho más que amor.txt',
'./Las mayores estupideces que hacemos por amor.txt','./Los-caminos-del-perdón.txt','./Los-límites-del-amor.txt','./Manifiesto-para-la-liberación-afectiva.txt','./Maravillosamente-imperfecto.txt',
'./Pensar bien, sentirse bien.txt']
libros=['AMA Y NO SUFRAS - Walter Riso','AMAR O DEPENDER - Walter Riso','AMAR O DEPENDER COMO SUPERAR EL APEGO - Walter Riso',
'AMOR DIVINA LOCULA - Walter Riso','AMORES ALTAMENTE PELIGROSOS - Walter Riso','CUESTIÓN DE DIGNIDAD - Walter Riso.txt','DESHOJANDO MARGARITAS',
'EL CAMINO DE LOS SABIOS - Walter Riso','ENAMORADOS O ESCLAVIZADOS - Walter Riso','ENAMORATE DE TI - Walter Riso','GUIA DE LAS EMOCIONES - Walter Riso',
'GUÍA PARA EL AUTOESTIMA - Walter Riso','LA FIDELIDAD - Walter Riso',
'ESTUPIDECES DEL AMOR - Walter Riso','LOS CAMINOS DEL PERDÓN - Walter Riso','LOS LIMITES DEL AMOR - Walter Riso','LIBERACIÓN AFECTIVA - Walter Riso','MARAVILLOSAMENTE IMPERFECTO - Walter Riso',
'PENSAR BIEN SENTIRSE BIEN - Walter Riso']

#funcion de fracaso
def fracaso(b): # calcula y retorna función de fracaso para patrón b
  d={} #Diccionario vacío que representará a la funcion de fracaso
  for i in range (0,len(b)-1): #Iretamos en todas las letras excepto la última
    d[b[i]]=i #En cada letra guardamos el índice
  return d # Se retorna al diccionario


def horspool(a,b):#Algoritmo de Horspool
    g=fracaso(b) #Generamos la función de fracaso a la palabra ingresada
    n=len(a) #Determinamos la longitud del texto
    m=len(b) #Dtemerminamos la longitud de la palabra
    r=[] # Declaramos una lista donde se guardaran todas la posiciones que generó la palabra
    k=m-1 #Indice del texto
    j=m-1#Indice de la palabra
    while k<n:
        if j<0: #Si coinciden las letras, guardamos la posicion
            r+=[k-m+1]
            j=m-1
            k+=1
            if k>=n:
                break
        if a[k-(m-1-j)]==b[j]:
            j=j-1 #Si las letras son iguales, restamos 1 al indice de la palabra
        else:
            k=k+(m-1-g.get(a[k],-1)) #Si no son iguales buscamos la letra en el diccionario
            j=m-1
    return r
#Lectura de los archivos txt
posicion_palabra=[]
num_palabras_libros=[]
leer_libro=[]
i=0
#Ingresamos la palabra que será evaluada por el algorimo
palabra=input("Ingrese una frase o palabra: ")
separador=" "
#Separamos la frase por palabras y guardamos el resultado en una lista
palabra_separada=palabra.split(separador)
#Identificamos si es una palabra o es una frase
#verificamos la longitud de la variable para poder cumplir la condición
if len(palabra_separada) == 1:  
  #Generamos un ciclo para extraer los textos de cada uno de los libros
 for l in librostxt:
  #Extraemos los libros y los guardamos en una variable
  with open(l,encoding='utf-8',errors='ignore') as archivo1:
    #Leemos la variable y guardamos el texto en una variable como una string
    leer_libro=archivo1.read()
    #Guardamos el numero de palabras de cada libro en una lista
    num_palabras_libros.append(len(horspool(leer_libro,palabra)))
 #juntamos en una sola sola variable el libro y el numero de palabras busadas
 dic=dict(zip(libros,num_palabras_libros))
 #Ordenamos la lista
 orden=(sorted(dic.items(),key=operator.itemgetter(1),reverse=True))
 #Imprimos la lista donde se encientra el resultado final
 for ñ in orden:
   print("---------------------")
   print (ñ)
#Búsqueda de posicion de cada palabra en todos los libros
 posicion=[]
 for xc in range(len(librostxt)):
  #Hacemos de nuevo una busqueda en los libros 
    with open(librostxt[xc],encoding='utf-8',errors='ignore') as archivo2:
      #Leemos cada uno de los lirbos
      leer_posicion=archivo2.read()
      #Agregamos a una lista las posiciones que hay en cada uno de los libros
      posicion.append(horspool(leer_posicion,palabra))
 lista_libros=[]
 #Hacemos un ciclo para poder sacar listas dentro deuna lista
 for o in range(len(posicion)):
      lista_libros=posicion[o]
      #Desigmamos una condicion en en donde si hay valores en la lista s imprimiran los valores
      if len(lista_libros)!=0:
       #Imprimimos el libro en el que se encientra el ciclo para identificar de donde son las posiciones
       print("En el libro: {0}".format(libros[o]))
       #Hacemos un ciclo en el cual se imprimen las posiciones de la palabra en cada uno de los libros
       for u in range(len(lista_libros)):
        #Imprimimos la palabra
          print("La palabra está en la pocisión: {0}".format(lista_libros[u]))
        #Imprimos un anuncio si no existe esa palabra
      else: 
          print("NO EXISTE ESTA PALABRA EN EL LIBRO: {0}".format(libros[o]))
      #Reseteamos la lista para que no se acumulen las posiciones de las palabras en una misma lista
      lista_libros.clear()
#Hacemos un menu para el usuario para que pueda identificar las operaciones a realizar
else:
  menu=""" 
                 OPCIONES DE BÚSQUEDAS.
  [1] Frase. 
  [2] Palabras.  
  [3] Ambas. 
        PRESIONE EL NÚMERO QUE DESEA REALIZAR.
  """
  print(menu)
  #Guaramos la opcion en un variable oara evaluarla
  opcion=int(input("¿Qué busqueda desea realizar?: "))
  #Evaliamos la opcion dependiendo el caso
  if opcion==1:
  #Realizamos las mismas operaciones que anteriormente se realizaron para una sola palabra
    posicion=[]
    for l in range(len(librostxt)):
     with open(librostxt[l],encoding='utf-8',errors='ignore') as archivo1:
      leer_libro=archivo1.read()
      num_palabras_libros.append(len(horspool(leer_libro,palabra)))
    dic=dict(zip(libros,num_palabras_libros))
    orden=(sorted(dic.items(),key=operator.itemgetter(1),reverse=True))
    for ñ in orden:
       print("---------------------")
       print (ñ)
#Búsqueda de posicion de cada palabra en todos los libros
    for xc in range(len(librostxt)):
     with open(librostxt[xc],encoding='utf-8',errors='ignore') as archivo2:
       leer_posicion=archivo2.read()
       posicion.append(horspool(leer_posicion,palabra))
    lista_libros=[]
    for o in range(len(posicion)):
      lista_libros=posicion[o]
      if len(lista_libros)!=0:
       print("En el libro: {0}".format(libros[o]))
       for u in range(len(lista_libros)):
          print("La palabra está en la pocisión: {0}".format(lista_libros[u]))
      else: 
          print("NO EXISTE ESTA PALABRA EN EL LIBRO: {0}".format(libros[o]))
      lista_libros.clear()
  elif opcion==2:
    for b in range(len(palabra_separada)):
     print("****************************************  Palabra: {0}  *********************************************************************".format(palabra_separada[b]))
     for l in librostxt:
      with open(l,encoding='utf-8',errors='ignore') as archivo1:
       leer_libro=archivo1.read()
       num_palabras_libros.append(len(horspool(leer_libro,palabra_separada[b])))
     dic=dict(zip(libros,num_palabras_libros))
     orden=(sorted(dic.items(),key=operator.itemgetter(1),reverse=True))
     for ñ in orden:
       print("---------------------")
       print (ñ)
#Búsqueda de posicion de cada palabra en todos los libros       
    posicion=[]   
    for xc in range(len(librostxt)):
     with open(librostxt[xc],encoding='utf-8',errors='ignore') as archivo2:
       leer_posicion=archivo2.read()
       posicion.append(horspool(leer_posicion,palabra))
    lista_libros=[]
    for o in range(len(posicion)):
      lista_libros=posicion[o]
      if len(lista_libros)!=0:
       print("En el libro: {0}".format(libros[o]))
       for u in range(len(lista_libros)):
          print("La palabra está en la pocisión: {0}".format(lista_libros[u]))
      else: 
          print("NO EXISTE ESTA PALABRA EN EL LIBRO: {0}".format(libros[o]))
      lista_libros.clear()     
  elif opcion==3:
    print("*********************************************************  La frase buscada es: {0} *************************************".format(palabra))
    for l in librostxt: 
     with open(l,encoding='utf-8',errors='ignore') as archivo1:
      leer_libro=archivo1.read()
      num_palabras_libros.append(len(horspool(leer_libro,palabra)))
    dic=dict(zip(libros,num_palabras_libros))
    orden=(sorted(dic.items(),key=operator.itemgetter(1),reverse=True))
    for ñ in orden:
      print("------------------------------------------------")
      print (ñ)
#Búsqueda de posicion de cada palabra en todos los libros       
    posicion=[]   
    for xc in range(len(librostxt)):
     with open(librostxt[xc],encoding='utf-8',errors='ignore') as archivo2:
       leer_posicion=archivo2.read()
       posicion.append(horspool(leer_posicion,palabra))
    lista_libros=[]
    for o in range(len(posicion)):
      lista_libros=posicion[o]
      if len(lista_libros)!=0:
       print("En el libro: {0}".format(libros[o]))
       for u in range(len(lista_libros)):
          print("La palabra está en la pocisión: {0}".format(lista_libros[u]))
      else: 
          print("NO EXISTE ESTA PALABRA EN EL LIBRO: {0}".format(libros[o]))
      lista_libros.clear()  
    for b in range(len(palabra_separada)):
     print("****************************************  Palabra: {0}  *********************************************************************".format(palabra_separada[b]))
     for m in librostxt:
      with open(m,encoding='utf-8',errors='ignore') as archivo1:
       leer_libro=archivo1.read()
       num_palabras_libros.append(len(horspool(leer_libro,palabra_separada[b])))
     dic=dict(zip(libros,num_palabras_libros))
     orden=(sorted(dic.items(),key=operator.itemgetter(1),reverse=True))
     for ñ in orden:
      print("------------------------------------------------")
      print (ñ)
      #Búsqueda de posicion de cada palabra en todos los libros       
    posicion=[]   
    for xc in range(len(librostxt)):
     with open(librostxt[xc],encoding='utf-8',errors='ignore') as archivo2:
       leer_posicion=archivo2.read()
       posicion.append(horspool(leer_posicion,palabra))
    lista_libros=[]
    for o in range(len(posicion)):
      lista_libros=posicion[o]
      if len(lista_libros)!=0:
       print("En el libro: {0}".format(libros[o]))
       for u in range(len(lista_libros)):
          print("La palabra está en la pocisión: {0}".format(lista_libros[u]))
      else: 
          print("NO EXISTE ESTA PALABRA EN EL LIBRO: {0}".format(libros[o]))
      lista_libros.clear()  
