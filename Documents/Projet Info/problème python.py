import matplotlib.pyplot as pl
import matplotlib
import numpy as np
import math as mp
import csv
import time
from datetime import datetime
from matplotlib.dates import AutoDateLocator
from datetime import time

def fonction1():#fonction pour afficher le tableau où toutes les données sont séparées par des points virgules et sous le format str: id1;noise1;temp1;humidity1;lum1;co2 1;aaaa-mm-jj hh:mm:ss+0200;id2;noise2...
    Tableau=[]
    f= open('/Users/felixmaquin/Documents/Projet Info/post-32566-EIVP_KM modifié colonne.csv')
    csv_f=csv.reader(f,delimiter=';')
    for row in csv_f:
        Tableau.append(row)
    f.close
    S=[]
    for i in range (1,len(Tableau)):
        a=Tableau[i]
        c=";".join(a)#donne pour chaque ligne: id;noise;temp;humidity;lum;co2;sent_at
        S.append(c)#S de la forme: ['id1;noise1;temp1;humidity1;lum1;co2 1;sent_at1','id2;noise2;temp2;humidity2;lum2;co2 2;sent_at2',...]
    Z1=";".join(S)
    return(Z1)#renvoie id1;noise1;temp1;humidity1;lum1;co2 1;sent_at1;id2;noise2;temp2;humidity2;lum2;co2 2;sent_at2;...
#print(fonction1())

def separation():
    liste_id=[] #liste contenant les id sous la forme 'id'
    liste_noise=[] # liste contenant  le paramètre noise sous la forme 'noise'
    liste_temp=[] # liste contenant le paramètre temp sous la forme 'temp'
    liste_humidity=[] # liste contenant le paramètre humidity sous la forme 'humidity'
    liste_lum=[] # liste contenant le paramètre lum sous la forme 'lum'
    liste_co2=[] # liste contenant le paramètre co2 sous la forme 'co2'
    liste_dateheure=[] # liste contenant date et heure sous la forme 'aaaa-mm-jj hh:mm:ss +0200'
    liste_date=[] # liste contenant seulement la date sous la forme 'aaaa-mm-jj'
    J=[]
    liste_heure=[] # liste contenant seulement les heures sous la forme 'hh:mm:ss'
    Q=fonction1()
    A=Q.split(";")#dès qu'un point virgule est rencontré, la fonction split prend l'élément juste avant et juste après le point virgule et les met dans une liste séparés par des virgules
    for i in range (0,len(A)-6,7):#je ne sélectionne que les identifiants qui sont présents dans la liste aux positions multiples de 7: id1,noise1,temp1,humidity1,lum1,co2 1, sent_at1,id2,...
        liste_id.append(A[i])
    for j in range(1,len(A)-5,7):#on ne sélectionne que les éléments de noise qu'on met dans une liste
        liste_noise.append(A[j])
    for k in range(2,len(A)-4,7):#on ne sélectionne que les éléments de temp qu'on met dans une liste
        liste_temp.append(A[k])
    for g in range(3,len(A)-3,7):#on ne sélectonne que les éléments de humidity qu'on met dans une liste
        liste_humidity.append(A[g])
    for h in range(4,len(A)-2,7):#on ne sélectionne que les éléments de lum  qu'on met dans une liste
        liste_lum.append(A[h])
    for z in range(5,len(A)-1,7):#on ne sélectionne que les éléments de co2 qu'on met dans une liste
        liste_co2.append(A[z])
    for r in range (6,len(A),7):#on ne sélectionne que les éléments de sent_at sous la forme 'aaaa-mm-jj hh:mm:ss+0200' qu'on met dans une liste
        liste_dateheure.append(A[r])
    for b in range(len(liste_dateheure)):#dans la liste précédente, pour chaque sent_at, dès que l'espace séparant le jour et l'heure est rencontré, je place dans la liste liste_date que 'aaaa-mm-jj' et dans la liste liste_heure que 'hh:mm:ss+02:00'
        e=liste_dateheure[b].split(" ")
        liste_date.append(e[0])
        liste_heure.append(e[1])
    for u in range (len(liste_id)):
        J.append([liste_id[u],liste_noise[u],liste_temp[u],liste_humidity[u],liste_lum[u],liste_co2[u],liste_date[u],liste_dateheure[u],liste_heure[u]])#la liste J contient donc des sous listes contenant une date avec ses trois formes ('aaaa-mm-ss hh:mm:ss+0200'(liste_dateheure[u]), 'aaaa-mm-jj'(liste_date[u]), 'hh:mm:ss'(liste_heure[u])) et les éléments id, noise, temp, humidity, lum, co2 associés
    d=len(J)
    J[d-1][7].strip('"\n')
    return(liste_id,liste_noise,liste_temp,liste_humidity,liste_lum,liste_co2,liste_dateheure,liste_date,J,liste_heure)
#print((separation()))

def tridates(L,M):# on a crée cette fonction parce que dans le tableau des dates, il y a des données pour une date à différents endroits du tableau. Comme on va faire nos tracés avec la liste C de séparation qui prend les dates suivant l'ordre du tableau de données, lors des tracés, on avait sur l'axe des abscisses des données pas classées par ordre chronologique de gauche à droite sur l'axe. Cette fonction trie les dates par ordre croissant dans une liste et met à la même position de cette date la valeur de noise, temp, humidity, lum ou co2 dans la liste correspondante. 
    for i in range (1,len(L)):
        a=L[i]
        b=M[i]
        j=i
        while j>0 and L[j-1]>a:
            L[j]=L[j-1]
            M[j]=M[j-1]
            j=j-1
        L[j]=a
        M[j]=b
    return(L,M)



def anomalies():
    datechoisie=input('Pour quelle date souhaitez vous voir si des anomalies sont présentes?(aaaa-mm-jj)')
    noise=separation()[1]#liste des valeurs du paramètre noise
    temp=separation()[2]#liste des valeurs du paramètre temp
    humidity=separation()[3]#liste des valeurs de humidity
    lum=separation()[4]#liste des valeurs du paramètre lum
    co2=separation()[5]#liste des valeurs du paramètre co2
    datesheures=separation()[6]#liste des dates sous la forme aaaa-mm-jj hh:mm:ss+02:00
    dates=separation()[7]#liste des valeurs des dates sous la forme aaaa-mm-jj
    heures=separation()[9]#liste des valeurs des heures sous la forme hh:mm:ss
    noise_datechoisie=[]#liste qui recevra les valeurs du paramètre noise pour la date choisie
    temp_datechoisie=[]#liste qui recevra les valeurs du paramètre temp pour la date choisie
    humidity_datechoisie=[]#liste qui recevra les valeurs du paramètre humidity pour la date choisie
    lum_datechoisie=[]#liste qui recevra les valeurs du paramètre lum pour la date choisie
    co2_datechoisie=[]#liste qui recevra les valeurs du paramètre co2 pour la date choisie
    datesheures_datechoisie=[]#liste qui recevra les valeurs du paramètre dates+heures pour la date choisie
    heures_datechoisie=[]#liste qui recevra les valeurs du paramètre heures pour la date choisie
    W1=[]#liste qui renvoie les anomalies sous la forme[[dateheure,'lum','co2'],[dateheure,'noise'],...] par exemple
    for p1 in range (len(dates)):#on parcourt la liste des dates classées selon l'ordre du fichier csv et renvoyée par la fonction séparation
        if dates[p1]==datechoisie:
            datesheures_datechoisie.append(datesheures[p1])#on ajoute dans cette liste que les dates=heures correspondant à la date choisie
            noise_datechoisie.append(float(noise[p1]))#on ajoute dans cette liste que les valeurs de noise correspondant à la date choisie
            temp_datechoisie.append(float(temp[p1]))#on ajoute dans cette liste que les valeurs de temp correspondant à la date choisie
            humidity_datechoisie.append(float(humidity[p1]))#on ajoute dans cette liste que les valeurs de humidity correspondant à la date choisie
            lum_datechoisie.append(float(lum[p1]))#on ajoute dans cette liste que les valeurs de lum correspondant à la date choisie
            co2_datechoisie.append(float(co2[p1]))#on ajoute dans cette liste que les valeurs de co2 correspondant à la date choisie
            heures_datechoisie.append(heures[p1])#on ajoute dans cette liste les valeurs des heures correspondant à la date choisie
    noise_datechoisietriees=tridates([d1 for d1 in datesheures_datechoisie],[d2 for d2 in noise_datechoisie])[1]#on trie la liste des valeurs de noise obtenue pour la date choisie selon le même ordre que l'ordre chronologique des dates
    temp_datechoisietriees=tridates([d3 for d3 in datesheures_datechoisie],[d4 for d4 in temp_datechoisie])[1]#on trie la liste des valeurs de temp obtenue pour la date choisie selon le même ordre que l'ordre chronologique des dates
    humidity_datechoisietriees=tridates([d5 for d5 in datesheures_datechoisie],[d6 for d6 in humidity_datechoisie])[1]#on trie la liste des valeurs de humidity obtenue pour la date choisie selon le même ordre que l'ordre chronologique des dates
    lum_datechoisietriees=tridates([d7 for d7 in datesheures_datechoisie],[d8 for d8 in lum_datechoisie])[1]#on trie la liste des valeurs de lum obtenue pour la date choisie selon le même ordre que l'ordre chronologique des dates
    co2_datechoisietriees=tridates([d9 for d9 in datesheures_datechoisie],[d10 for d10 in co2_datechoisie])[1]#on trie la liste des valeurs de co2 obtenue pour la date choisie selon le même ordre que l'ordre chronologique des dates
    datesheures_datechoisietriees=tridates([d11 for d11 in datesheures_datechoisie],[d12 for d12 in noise_datechoisie])[0]#cette liste correspond à la liste des dates+heures triée par ordre chronologique
    heures_datechoisietriees=tridates([d13 for d13 in heures_datechoisie],[d14 for d14 in noise_datechoisie])[0]#cette liste correspond à la liste des heures triée par ordre chronologique
    for j in range (1,len(noise_datechoisietriees)):
        if (float(noise_datechoisietriees[j])>float(noise_datechoisietriees[j-1])+((10/100)*float(noise_datechoisietriees[j-1]))) or float(noise_datechoisietriees[j])<float(noise_datechoisietriees[j-1])-((10/100)*float(noise_datechoisietriees[j-1])) and ('00:00:00'<heures_datechoisietriees[j]<'08:00:00' or '20:00:00'<heures_datechoisietriees[j]<'23:59:00'):#si on a une augmentation ou une diminution de 10% sur une valeur de noise_datechoisietriees par rapport à la précédente et que l'heure correspondant à cette valeur est entre minuit et 8h ou entre 20h et 23h59, on ajoute la valeur date+heure correspondante et le nom du paramètre(ici noise) sur lequel porte l'anomalie dans W1
            W1.append([datesheures_datechoisietriees[j],'noise'])
        elif (float(noise_datechoisietriees[j])>float(noise_datechoisietriees[j-1])+((40/100)*float(noise_datechoisietriees[j-1])) or float(noise_datechoisietriees[j])<float(noise_datechoisietriees[j-1])-((40/100)*float(noise_datechoisietriees[j-1]))) and ('08:00:00'<=heures_datechoisietriees[j]<='20:00:00'):#si on a une augmentation ou une diminution de 40% sur une valeur de noise_datechoisietriees par rapport à la précédente et que l'heure correspondant à cette valeur est entre 8h et 20h, on ajoute la valeur date+heure correspondante et le nom du paramètre(ici noise) sur lequel porte l'anomalie dans W1
            W1.append([datesheures_datechoisietriees[j],'noise'])
    for a1 in range (1,len(temp_datechoisietriees)):
        if (float(temp_datechoisietriees[a1])>float(temp_datechoisietriees[a1-1])+((10/100)*float(temp_datechoisietriees[a1-1])) or float(temp_datechoisietriees[a1])<float(temp_datechoisietriees[a1-1])-((10/100)*float(temp_datechoisietriees[a1-1]))) and ('00:00:00'<heures_datechoisietriees[a1]<'08:00:00' or '20:00:00'<heures_datechoisietriees[a1]<'23:59:00') :#si on a une augmentation ou une diminution de 10% sur une valeur de temp_datechoisietriees par rapport à la précédente et que l'heure correspondant à cette valeur est entre minuit et 8h ou entre 20h et 23h59
            b1=False
            if len(W1)!=0:#il faut que la liste W1 contienne des anomalies liées aux paramètres précédents
                for a2 in range (len(W1)):
                    if W1[a2][0]==datesheures_datechoisietriees[a1]:#si la date d'une anomalie (contenue dans une liste dans W1) correspondant à un paramètre précédent et la même que celle de l'anomalie décelée par le dernier if, on ajoute à cette liste de W1 'temp' pour indiquer que l'anomalie vient aussi du paramètre temp. On change alors la valeur de b1 en true
                        W1[a2].append('temp')
                        b1=True
            if b1==False:#si b1==False, cela signifie qu'il n'y avait pas de liste de W1 contenant la même date que celle sur laquelle porte l'anomalie décelée par le dernier if. On ajoute alors la date+heure de cette anomalie et le paramètre (ici temp)dans W1
                W1.append([datesheures_datechoisietriees[a1],'temp'])
        elif (float(temp_datechoisietriees[a1])>float(temp_datechoisietriees[a1-1])+((40/100)*float(temp_datechoisietriees[a1-1])) or float(temp_datechoisietriees[a1])<float(temp_datechoisietriees[a1-1])-((40/100)*float(temp_datechoisietriees[a1-1]))) and ('08:00:00'<=heures_datechoisietriees[a1]<='20:00:00'):#si on a une augmentation ou une diminution de 40% sur une valeur de temp_datechoisietriees par rapport à la précédente et que l'heure correspondant à cette valeur est entre minuit et 8h et 20h 
            b1=False
            if len(W1)!=0:
                for a2 in range (len(W1)):
                    if W1[a2][0]==datesheures_datechoisietriees[a1]:#si la date d'une anomalie (contenue dans une liste dans W1) correspondant à un paramètre précédent et la même que celle de l'anomalie décelée par le dernier if, on ajoute à cette liste de W1 'temp' pour indiquer que l'anomalie vient aussi du paramètre temp. On change alors la valeur de b1 en true
                        W1[a2].append('temp')
                        b1=True
            if b1==False:#si b1==False, cela signifie qu'il n'y avait pas de liste de W1 contenant la même date que celle sur laquelle porte l'anomalie décelée par le dernier if. On ajoute alors la date+heure de cette anomalie et le paramètre (ici temp) dans W1
                W1.append([datesheures_datechoisietriees[a1],'temp'])
    for v1 in range (1,len(humidity_datechoisietriees)):
        if (float(humidity_datechoisietriees[v1])>float(humidity_datechoisietriees[v1-1])+((10/100)*float(humidity_datechoisietriees[v1-1])) or float(humidity_datechoisietriees[v1])<float(humidity_datechoisietriees[v1-1])-((10/100)*float(humidity_datechoisietriees[v1-1]))) and ('00:00:00'<heures_datechoisietriees[v1]<'08:00:00' or '20:00:00'<heures_datechoisietriees[v1]<'23:59:00'):#on reproduit le même schéma pour les autres paramètres
            n1=False
            if len(W1)!=0:
                for v2 in range (len(W1)):
                    if W1[v2][0]==datesheures_datechoisietriees[v1]:
                        W1[v2].append('humidity')
                        n1=True
            if n1==False:
                W1.append([datesheures_datechoisietriees[v1],'humidity'])
        elif (float(humidity_datechoisietriees[v1])>float(humidity_datechoisietriees[v1-1])+((40/100)*float(humidity_datechoisietriees[v1-1])) or float(humidity_datechoisietriees[v1])<float(humidity_datechoisietriees[v1-1])-((40/100)*float(humidity_datechoisietriees[v1-1]))) and ('08:00:00'<=heures_datechoisietriees[v1]<='20:00:00'):
            n1=False
            if len(W1)!=0:
                for v2 in range (len(W1)):
                    if W1[v2][0]==datesheures_datechoisietriees[v1]:
                        W1[v2].append('humidity')
                        n1=True
            if n1==False:
                W1.append([datesheures_datechoisietriees[v1],'humidity'])
    for a3 in range (1,len(lum_datechoisietriees)):
        if (float(lum_datechoisietriees[a3])>float(lum_datechoisietriees[a3-1])+((10/100)*float(lum_datechoisietriees[a3-1])) or float(lum_datechoisietriees[a3])<float(lum_datechoisietriees[a3-1])-((10/100)*float(lum_datechoisietriees[a3-1]))) and ('00:00:00'<heures_datechoisietriees[a3]<'08:00:00' or '20:00:00'<heures_datechoisietriees[a3]<'23:59:00'):
            b2=False
            if len(W1)!=0:
                for a4 in range (len(W1)):
                    if W1[a4][0]==datesheures_datechoisietriees[a3]:
                        W1[a4].append('lum')
                        b2=True
            if b2==False:
                W1.append([datesheures_datechoisietriees[a3],'lum'])
        elif (float(lum_datechoisietriees[a3])>float(lum_datechoisietriees[a3-1])+((40/100)*float(lum_datechoisietriees[a3-1])) or float(lum_datechoisietriees[a3])<float(lum_datechoisietriees[a3-1])-((40/100)*float(lum_datechoisietriees[a3-1]))) and ('08:00:00'<=heures_datechoisietriees[a3]<='20:00:00'):
            b2=False
            if len(W1)!=0:
                for a4 in range (len(W1)):
                    if W1[a4][0]==datesheures_datechoisietriees[a3]:
                        W1[a4].append('lum')
                        b2=True
            if b2==False:
                W1.append([datesheures_datechoisietriees[a3],'lum'])
    for a5 in range (1,len(co2_datechoisietriees)):
        if (float(co2_datechoisietriees[a5])>float(co2_datechoisietriees[a5-1])+((10/100)*float(co2_datechoisietriees[a5-1])) or float(co2_datechoisietriees[a5])<float(co2_datechoisietriees[a5-1])-((10/100)*float(co2_datechoisietriees[a5-1]))) and ('00:00:00'<heures_datechoisietriees[a5]<'08:00:00' or '20:00:00'<heures_datechoisietriees[a5]<'23:59:00'):
            b3=False
            if len(W1)!=0:
                for a6 in range (len(W1)):
                    if W1[a6][0]==datesheures_datechoisietriees[a5]:
                        W1[a6].append('co2')
                        b3=True
            if b3==False:
                W1.append([datesheures_datechoisietriees[a5],'co2'])
        elif (float(co2_datechoisietriees[a5])>float(co2_datechoisietriees[a5-1])+((40/100)*float(co2_datechoisietriees[a5-1])) or float(co2_datechoisietriees[a5])<float(co2_datechoisietriees[a5-1])-((40/100)*float(co2_datechoisietriees[a5-1]))) and ('08:00:00'<=heures_datechoisietriees[a5]<='20:00:00'):
            b3=False
            if len(W1)!=0:
                for a6 in range (len(W1)):
                    if W1[a6][0]==datesheures_datechoisietriees[a5]:
                        W1[a6].append('co2')
                        b3=True
            if b3==False:
                W1.append([datesheures_datechoisietriees[a5],'co2'])
    return(W1)
    
    
print(anomalies())

