#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 11:50:20 2020

@author: nathanjacotot
"""
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
    f= open('EIVP_KM_ColonnesModifiees.csv')
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
    liste_heure=[] # liste contenant seulement les heures sous la forme 'hh:mm:ss+02:00'
    Q=fonction1()
    A=Q.split(";")#dès qu'un point virgule est rencontré, la fonction split prend l'élément juste avant et juste après le point virgule et les met dans une liste séparés par des virgules
    for i in range (0,len(A)-6,7):#on ne sélectionne que les identifiants qui sont présents dans la liste aux positions multiples de 7: id1,noise1,temp1,humidity1,lum1,co2 1, sent_at1,id2,...
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
    for b in range(len(liste_dateheure)):#dans la liste précédente, pour chaque sent_at, dès que l'espace séparant le jour et l'heure est rencontré, on place dans la liste liste_date que 'aaaa-mm-jj' et dans la liste liste_heure que 'hh:mm:ss+02:00'
        e=liste_dateheure[b].split(" ")
        liste_date.append(e[0])
        liste_heure.append(e[1])
    for u in range (len(liste_id)):
        J.append([liste_id[u],liste_noise[u],liste_temp[u],liste_humidity[u],liste_lum[u],liste_co2[u],liste_date[u],liste_dateheure[u],liste_heure[u]])#la liste J contient donc des sous listes contenant une date avec ses trois formes ('aaaa-mm-ss hh:mm:ss+02:00'(liste_dateheure[u]), 'aaaa-mm-jj'(liste_date[u]), 'hh:mm:ss'(liste_heure[u])) et les éléments id, noise, temp, humidity, lum, co2 associés
    d=len(J)
    J[d-1][7].strip('"\n')
    return(liste_id,liste_noise,liste_temp,liste_humidity,liste_lum,liste_co2,liste_dateheure,liste_date,J,liste_heure)
#print((separation()))


def calcmin(L):
    c=0
    for i in range (len(L)):
        if float(L[i])<=float(L[c]):#on met des float car dans les listes qcréees avec la fonction separation, les éléments sont sous la forme '134' par exemple
            c=i
    return(float(L[c]))
    
def calcmax(L):
    m=0
    for i in range(len(L)):
        if float(L[i])>=float(L[m]):
            m=i
    return(float(L[m]))
 

def calcmoy(L):
    k=0
    e=len(L)
    for i in range(e):
        k=k+float(L[i])
    return(round(k/e,2))#la fonction round( ,2) permet d'avoir un nombre qu'avec deux chiffres après la virgule

def variance(L):
    r=calcmoy(L)
    m=0
    j=len(L)
    for i in range (j):
        m=m+(float(L[i])-r)**2
    return(round(m/j,2))
    
def mediane(L):
    L.sort()
    j=len(L)
    if j%2==1:
        return(L[int(j/2)])
    else:
        return((L[(j//2)-1]+L[j//2])/2)
 
 
def ecarttype(L):
    r=calcmoy(L)
    m=0
    j=len(L)
    for i in range (j):
        m=m+(float(L[i])-r)**2
    return(round(mp.sqrt(m/j),2))
    
  
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


def trace1():
    P=[]
    K=[]#liste qui recevra les valeurs à tracer en ordonnée non classées par la fonction tridates
    S=[]#liste qui recevra les dates+heures à placer en abscisse non classées par la fonction tridates
    g=separation()[8]#la liste J de la fonction separation
    a1=separation()[1]#liste des éléments de noise
    a2=separation()[2]#liste des éléments de temp
    a3=separation()[3]#liste des éléments de humidity
    a4=separation()[4]#liste des éléments de lum
    a5=separation()[5]#liste des éléments de co2
    r=input('Quelle variable souhaitez vous utiliser?(noise,temp, humidity, lum ou co2)')
    o=input('Souhaitez-vous spécifier un intervalle de temps?(oui/non)')
    if o=='non':
        if r=='noise':
            for b1 in range(len(a1)):
                K.append(float(a1[b1]))#on rajoute chaque élément de a1 dans K sous la forme d'un float
            pl.plot(tridates(separation()[6],K)[0],tridates(separation()[6],K)[1])#on trace avec un ordre chronologique sur l'axe des abscisses avec la fonction tridates
            pl.ylabel('noise(dBA)')
            pl.xticks(rotation='vertical')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))#on fait apparaitre que 8 dates clés sur l'axe des ordonnées
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))#on fait apparaître que 8 dates clés sur l'axe des abscisses
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.show()
        elif r=='temp':
            for b2 in range (len(a2)):
                K.append(float(a2[b2]))
            pl.plot(tridates(separation()[6],K)[0],tridates(separation()[6],K)[1])
            pl.ylabel('temp(°C)')
            pl.xticks(rotation='vertical')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.show()
        elif r=='humidity':
            for b3 in range (len(a3)):
                K.append(float(a3[b3]))
            pl.plot(tridates(separation()[6],K)[0],tridates(separation()[6],K)[1])
            pl.ylabel('humidity(%)')
            pl.xticks(rotation='vertical')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.show()
        elif r=='lum':
            for b4 in range (len(a4)):
                K.append(float(a4[b4]))
            pl.plot(tridates(separation()[6],K)[0],tridates(separation()[6],K)[1])
            pl.ylabel('lum(lux)')
            pl.xticks(rotation='vertical')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.show()
        elif r=='co2':
            for b5 in range (len(a5)):
                K.append(a5[b5])
            pl.plot(tridates(separation()[6],K)[0],tridates(separation()[6],K)[1])
            pl.ylabel('co2(ppm)')
            pl.xticks(rotation='vertical')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.show()
    else:
        t=input('Quelle date initiale souhaitez-vous pour évolution de cette variable?(aaaa-mm-jj)')
        f=input('Quelle date finale souhaitez-vous pour évolution de cette variable?(aaaa-mm-jj)')
        for i in range (len(g)):
            if g[i][6]<=f and g[i][6]>=t:#grâce au module datetime importé au début, on peut comparer deux dates sous la forme str et au format 'aaaa-mm-jj'. On parcourt la liste J[['id1', 'noise1','temp1','humidity1','lum1','co2 1','aaaa-mm-jj','aaaa-mm-jj hh:mm:ss+0200','hh:mm:ss'],...] et on compare les 6°éléments de ces sous listes au dates rentrées par l'utilisateur. Si cette date est comprise entre la date de départ et la date finale rentrées par l'utilisateur, on ajoute à la liste K les éléments que on va mettre en ordonnée( soit noise, soit temp, soit humidity, soit lum, soit co2) et à S la date sous la forme 'aaaa-mm-jj hh:mm:ss+0200'
                P.append(g[i])#on ajoute dans P si la valeur de liste_date est comprise dans l'intervalle de temps mentionné ou correspond à l'unique date rentrée dans t et dans f: liste_id,liste_noise,liste_temp,liste_humidity,liste_lum,liste_co2,liste_date,liste_dateheure,liste_heure 
        if r=='noise':
            for j in range (len(P)):
                K.append(P[j][1])
                S.append(P[j][7])
        elif r=='temp':
            for h in range(len(P)):
                K.append(P[h][2])
                S.append(P[h][7])
        elif r=='humidity':
            for k in range(len(P)):
                K.append(P[k][3])
                S.append(P[k][7])
        elif r=='lum':
            for l in range (len(P)):
                K.append(P[l][4])
                S.append(P[l][7])
        elif r=='co2':
            for m in range (len(P)):
                K.append(P[m][5])
                S.append(P[m][7])
    for a in range(len(K)):
        K[a]=float(K[a])#conversion de tous les éléments de K de str en float
    pl.xticks(rotation='vertical')
    pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
    pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
    pl.tick_params(axis = 'x', labelsize = 3)
    if r=='noise':
        pl.ylabel('noise(dBA)')
    elif r=='temp':
        pl.ylabel('temp(°C)')
    elif r=='humidity':
        pl.ylabel('humidity(%)')
    elif r=='lum':
        pl.ylabel('lum(lux)')
    elif r=='co2':
        pl.ylabel('co2(ppm)')
    pl.plot(tridates(S,K)[0],tridates(S,K)[1])#on trie les dates pour qu'elles apparaissent par ordre chronologique sur l'axe des abscisses et on leur associe la valeur en ordonnée correspondante
    pl.show()
    return()
            
#print(trace1())

def inter():# exactement la même fonction que trace1 sauf qu'au lieu de faire un tracé, on renvoie les listes qui nous servent à faire les tracés de la fonction ajouttrace
    P=[]
    K=[]
    S=[]
    g=separation()[8]
    a1=separation()[1]
    a2=separation()[2]
    a3=separation()[3]
    a4=separation()[4]
    a5=separation()[5]
    r=input('Quelle variable souhaitez vous utiliser?((noise,temp, humidity, lum ou co2)')
    o=input('Souhaitez-vous spécifier un intervalle de temps?(oui/non)')
    if o=='non':
        if r=='noise':
            for b1 in range (len(a1)):
                K.append(float(a1[b1]))
            return(tridates(separation()[6],K)[1],tridates(separation()[6],K)[0],r)
        elif r=='temp':
            for b2 in range (len(a2)):
                K.append(float(a2[b2]))
            return(tridates(separation()[6],K)[1],tridates(separation()[6],K)[0],r)
        elif r=='humidity':
            for b3 in range (len(a3)):
                K.append(float(a3[b3]))
            return(tridates(separation()[6],K)[1],tridates(separation()[6],K)[0],r)
        elif r=='lum':
            for b4 in range (len(a4)):
                K.append(float(a4[b4]))
            return(tridates(separation()[6],K)[1],tridates(separation()[6],K)[0],r)
        elif r=='co2':
            for b5 in range (len(a5)):
                K.append(float(a5[b5]))
            return(tridates(separation()[6],K)[1],tridates(separation()[6],K)[0],r)
    else:
        t=input('Quelle date initiale souhaitez-vous pour évolution de cette variable?(aaaa-mm-jj)')
        f=input('Quelle date finale souhaitez-vous pour évolution de cette variable?(aaaa-mm-jj)')
        for i in range (len(g)):
            if g[i][6]<=f and g[i][6]>=t:
                P.append(g[i])
        if r=='noise':
            for j in range (len(P)):
                K.append(P[j][1])
                S.append(P[j][7])
        elif r=='temp':
            for h in range(len(P)):
                K.append(P[h][2])
                S.append(P[h][7])
        elif r=='humidity':
            for k in range(len(P)):
                K.append(P[k][3])
                S.append(P[k][7])
        elif r=='lum':
            for l in range (len(P)):
                K.append(P[l][4])
                S.append(P[l][7])
        elif r=='co2':
            for m in range (len(P)):
                K.append(P[m][5])
                S.append(P[m][7])
    for q in range(len(K)):
        K[q]=float(K[q])
    return(tridates(S,K)[1],tridates(S,K)[0],r)    
    
#print(inter())



def ajouttrace():# dans cette fonction, on fait apparaitre le min, le max, la moyenne, l'écart type, la médiane et la variance si l'utilisateur le souhaite
    u=input('Voulez vous faire apparaître min, max, moyenne, ecart type, mediane, variance?(oui/non)')
    if u=='non':
        return(trace1())
    else:
        v=inter()
        a,b=calcmin(v[0]), calcmax(v[0])
        pl.gca().set_ylim(a,b)#c'est pour que l'axe des ordonnées commence au minimum des valeurs de la liste que l'utilisateur veut mettre en ordonnée( noise, temp, humidity, lum ou co2) et s'arrête au maximum
        pl.plot(v[1],v[0])
        pl.gca().annotate('min=',(0.45,0.95),xycoords='axes fraction')
        pl.gca().annotate(a,(0.53,0.95),xycoords='axes fraction')#avec la fonction annotate, on peut écrire des formules sur la fenêtre des tracés alors qu'avec plot.text, plot.text(calcmin(v[0])) écrit calcmin(v[0]) et pas la valeur de ce minimum. Axes fraction, c'est pour graduer les axes des abscisses et ordonnées de 0 à 1 sans que ça apparaisse sur la fenêtre de tracé pour pouvoir placer le texte que l'on veut faire apparaître sur la fenêtre plus simplement à partir de ses coordonnées.
        pl.gca().annotate('max=',(0.6,0.95),xycoords='axes fraction')
        pl.gca().annotate(b,(0.68,0.95),xycoords='axes fraction')
        pl.gca().annotate('moyenne=',(0.78,0.95),xycoords='axes fraction')
        pl.gca().annotate(calcmoy(v[0]),(0.93,0.95),xycoords='axes fraction')
        pl.gca().annotate('variance=',(0.25,0.9),xycoords='axes fraction')
        pl.gca().annotate(variance(v[0]),(0.4,0.9),xycoords='axes fraction')
        pl.gca().annotate('ecart type=',(0.55,0.9),xycoords='axes fraction')
        pl.gca().annotate(ecarttype(v[0]),(0.71,0.9),xycoords='axes fraction')
        pl.gca().annotate('mediane=',(0.83,0.9),xycoords='axes fraction')
        pl.gca().annotate(mediane(v[0]),(0.97,0.9),xycoords='axes fraction')
        if v[2]=='noise':
            pl.ylabel('noise(dBA)')
        elif v[2]=='temp':
            pl.ylabel('temp(°C)')
        elif v[2]=='humidity':
            pl.ylabel('humidity(%)')
        elif v[2]=='lum':
            pl.ylabel('lum(lux)')
        elif v[2]=='co2':
            pl.ylabel('co2(ppm)')
        pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
        pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
        pl.xticks(rotation='vertical')#on écrit les dates sur l'axe des abscisses verticalement
        pl.tick_params(axis = 'x', labelsize = 3)#on réduit la taille de la police sur l'axe des abscisses.
        pl.show()
    return()
#print(ajouttrace())  


    
def temprosee(T,h):#la formule vient d'internet
    a=17.27
    b=237.7
    return((b*(((a*T)/b+T)+np.log(h/100)))/(a-(((a*T)/(b+T))+np.log(h/100))))
    
def humidex(T,h):#on a trouvé la formule sur internet. T est la température et h l'humidité
    return(T+0.5555*(6.11*np.exp(5417.7530*((1/273.16)-(1/(273.15+temprosee(T,h))))-10)))
    
def tracehumidex():#cette fonction permet de tracer l'indice humidex en fonction des dates
    I=[]
    M=[]
    P=[]
    g=separation()[8]
    f=input('Souhaitez vous spécifier un intervalle de temps?')
    if f=='non':
        for i in range (len(g)):
            I.append(humidex(float(g[i][2]),float(g[i][3])))#la liste I contient les indices humidex associée à chaque date et calculés à partir de la température et de l'humidité de chaque date
            P.append(g[i][7])
        pl.plot(tridates(P,I)[0],tridates(P,I)[1])
        pl.ylabel('humidex')
        pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
        pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
        pl.xticks(rotation='vertical')
        pl.tick_params(axis = 'x', labelsize = 3)
        pl.show()
    else:
        t=input('Quelle date initiale souhaitez-vous pour évolution de cette variable?(aaaa-mm-jj)')
        k=input('Quelle date finale souhaitez-vous pour évolution de cette variable?(aaaa-mm-jj)')
        for j in range (len(g)):
            if g[j][6]<=k and g[j][6]>=t:
                P.append(g[j][7])
                I.append(humidex(float(g[j][2]),float(g[j][3])))
        pl.plot(tridates(P,I)[0],tridates(P,I)[1])#le tracé de l'indice humidex en fonction des dates n'est effectué que pour les dates dans l'intervalle de temps renseigné par l'utilisateur
        pl.ylabel('humidex')
        pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
        pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
        pl.xticks(rotation='vertical')
        pl.tick_params(axis = 'x', labelsize = 3)
        pl.show()
    return()
        
#print(tracehumidex())
           
       
    
def humidexdate():#cette fonction renvoie une liste de listes de la forme [[date,indice umidex]] si l'utilisateur ne veut calculer l'indice humidex que pour une seule date ou [[date1,indice humidex1],[date2, indice humidex2],...]si il mentionne un intervalle de dates pour lequel il veut avoir l'indice humidex
    S=[['date','indice humidex']]
    g=separation()[8]
    f=input('Souhaitez vous spécifier un intervalle de temps(1) ou proposer une seule date(2)?')
    if f=='1':
        t=input('Quelle date initiale souhaitez-vous pour calcul humidex?(aaaa-mm-jj)')
        k=input('Quelle date finale souhaitez-vous pour calcul humidex?(aaaa-mm-jj)')
        for j in range (len(g)):
            if g[j][6]<=k and g[j][6]>=t:
                S.append([g[j][7],humidex(float(g[j][2]),float(g[j][3]))])
    else:
        r=input('Pour quelle date souhaitez vous avoir indice humidex?(aaaa-mm-jj)')
        h=input('Quelle heure présente dans le tableau souhaitez vous pour cette date?(hh:mm:ss)')
        for i in range (len(g)):
            if datetime.fromisoformat(r)==datetime.fromisoformat(g[i][6]) and time.fromisoformat(h)==time.fromisoformat(g[i][8]):
                S.append([g[i][7],humidex(float(g[i][2]),float(g[i][3]))])
    return(S)

#print(humidexdate())

def valeurcorrelation(D,L,M):#pour deux variables L et M et leur produit D, cette fonction renvoie l'indice de correlation de ces deux variables.
    nm=calcmoy(D)-calcmoy(L)*calcmoy(M)  #numérateur: formule covariance
    dn=ecarttype(L)*ecarttype(M)         #dénominateur: multiplication des écarts type
    return round(nm/dn, 4)               #arrondis au millième



def indicecorrelation():
    A=[]
    B=[]
    C=[]
    D=[]
    g=separation()[8]
    a=input('Quel couple de variables choisissez vous?(noise-temp:1, noise-humidity:2, noise-lum:3, noise-co2:4, temp-humidity:5, temp-lum:6, temp-co2:7, humidity-lum:8, humidity-co2:9, lum-co2:10)')
    b=input('Souhaitez vous spécifier un intervalle de temps?(oui/non)')
    c=input('Voulez vous tracer les deux variables en fonction du temps et afficher indice correlation(1) ou seulement afficher indice de correlation(2)?')
    if b=='non' and a=='1':
        for a1 in range(len(g)):
            A.append(float(g[a1][1]))#A contient toutes les valeurs du paramètre noise
            B.append(float(g[a1][2]))#B contient toutes les valeurs du paramètre temp 
            C.append(float(g[a1][1])*float(g[a1][2]))#C contient le produit des valeurs des paramètres noise et temp date par date
            D.append(g[a1][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label='temp(°C)')
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label='noise(dBA)')
            pl.legend()
            pl.show()
        else:#on retourne seulement la liste de l'indice de corrélation et celle des dates si l'utilisateur ne choisit pas de tracer
            return(valeurcorrelation(C,D))
    elif b=='non' and a=='2':
        for a2 in range (len(g)):
            A.append(float(g[a2][1]))#A contient toutes les valeurs du paramètre noise
            B.append(float(g[a2][3]))#B contient toutes les valeurs du paramètre humidity
            C.append(float(g[a2][1])*float(g[a2][3]))#C contient le produit des valeurs des paramètres noise et humidity date par date
            D.append(g[a2][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label="humidity(%)")
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label="noise(dBA)")
            pl.legend()
            pl.show()
        else:#on retourne seulement la liste de l'indice de corrélation et celle des dates si l'utilisateur ne choisit pas de tracer
            return(valeurcorrelation(C,D))
    elif b=='non' and a=='3':
        for a3 in range (len(g)):
            A.append(float(g[a3][1]))#A contient toutes les valeurs du paramètre noise
            B.append(float(g[a3][4]))#B contient toutes les valeurs du paramètre lum
            C.append(float(g[a3][1])*float(g[a3][4]))#C contient le produit des valeurs des paramètres noise et lum date par date
            D.append(g[a2][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label="lum(lux)")
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label="noise(dBA)")
            pl.legend()
            pl.show()
        else:#on retourne seulement la liste de l'indice de corrélation et celle des dates si l'utilisateur ne choisit pas de tracer
            return(valeurcorrelation(C,D))
    elif b=='non' and a=='4':
        for a4 in range (len(g)):
            A.append(float(g[a4][1]))#A contient toutes les valeurs du paramètre noise
            B.append(float(g[a4][5]))#B contient toutes les valeurs du paramètre co2
            C.append(float(g[a4][1])*float(g[a4][5]))#C contient le produit des valeurs des paramètres noise et co2 date par date
            D.append(g[a4][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label="co2(ppm)")
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label="noise(lux)")
            pl.legend()
            pl.show()
        else:#on retourne seulement la liste de l'indice de corrélation et celle des dates si l'utilisateur ne choisit pas de tracer
            return(valeurcorrelation(C,D))
    elif b=='non' and a=='5':
        for a5 in range (len(g)):
            A.append(float(g[a5][2]))#A contient toutes les valeurs du paramètre temp
            B.append(float(g[a5][3]))#B contient toutes les valeurs du paramètre humidity
            C.append(float(g[a5][2])*float(g[a5][3]))#C contient le produit des valeurs des paramètres temp et humidity date par date
            D.append(g[a5][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label="humidity(%)")
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label="temp(°C)")
            pl.legend()
            pl.show()
        else:#on retourne seulement la liste de l'indice de corrélation et celle des dates si l'utilisateur ne choisit pas de tracer
            return(valeurcorrelation(C,D))
    elif b=='non' and a=='6':
        for a6 in range (len(g)):
            A.append(float(g[a6][2]))#A contient toutes les valeurs du paramètre temp
            B.append(float(g[a6][4]))#B contient toutes les valeurs du paramètre lum
            C.append(float(g[a6][2])*float(g[a6][4]))#C contient le produit des valeurs des paramètres temp et lum date par date
            D.append(g[a6][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label="lum(lux)")
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label="temp(°C)")
            pl.legend()
            pl.show()
        else:#on retourne seulement la liste de l'indice de corrélation et celle des dates si l'utilisateur ne choisit pas de tracer
            return(valeurcorrelation(C,D))
    elif b=='non' and a=='7':
        for a7 in range (len(g)):
            A.append(float(g[a7][2]))#A contient toutes les valeurs du paramètre temp
            B.append(float(g[a7][5]))#B contient toutes les valeurs du paramètre co2
            C.append(float(g[a7][2])*float(g[a7][5]))#C contient le produit des valeurs des paramètres temp et co2 date par date
            D.append(g[a7][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label="co2(ppm)")
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label="temp(°C)")
            pl.legend()
            pl.show()
        else:#on retourne seulement la liste de l'indice de corrélation et celle des dates si l'utilisateur ne choisit pas de tracer
            return(valeurcorrelation(C,D))
    elif b=='non' and a=='8':
        for a8 in range (len(g)):
            A.append(float(g[a8][3]))#A contient toutes les valeurs du paramètre humidity
            B.append(float(g[a8][4]))#B contient toutes les valeurs du paramètre lum
            C.append(float(g[a8][3])*float(g[a8][4]))#C contient le produit des valeurs des paramètres humidity et lum date par date
            D.append(g[a8][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label="lum(lux)")
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label="humidity(%)")
            pl.legend()
            pl.show()
        else:#on retourne seulement la liste de l'indice de corrélation et celle des dates si l'utilisateur ne choisit pas de tracer
            return(valeurcorrelation(C,D))
    elif b=='non' and a=='9':
        for a9 in range (len(g)):
            A.append(float(g[a9][3]))#A contient toutes les valeurs du paramètre humidity
            B.append(float(g[a9][5]))#B contient toutes les valeurs du paramètre co2
            C.append(float(g[a9][3])*float(g[a9][5]))#C contient le produit des valeurs des paramètres humidity et co2 date par date
            D.append(g[a9][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label="co2(ppm)")
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label="humidity(%)")
            pl.legend()
            pl.show()
        else:#on retourne seulement la liste de l'indice de corrélation et celle des dates si l'utilisateur ne choisit pas de tracer
            return(valeurcorrelation(C,D))
    elif b=='non' and a=='10':
        for a10 in range(len(g)):
            A.append(float(g[a10][4]))#A contient toutes les valeurs du paramètre lum
            B.append(float(g[a10][5]))#B contient toutes les valeurs du paramètre co2
            C.append(float(g[a10][4])*float(g[a10][5]))#C contient le produit des valeurs des paramètres lum eet co2 date par date
            D.append(g[a10][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label="co2(ppm)")
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label="lum(lux)")
            pl.legend()
            pl.show()
        else:#on retourne seulement la liste de l'indice de corrélation et celle des dates si l'utilisateur ne choisit pas de tracer
            return(valeurcorrelation(C,A,B))
    elif b=='oui' and a=='1':
        t=input('Quelle date initiale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        k=input('Quelle date finale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        for a1 in range (len(g)):
            if g[a1][6]<=k and g[a1][6]>=t:
                A.append(float(g[a1][1]))#A contient toutes les valeurs du paramètre noise comprises entre les dates renseignées
                B.append(float(g[a1][2]))#B contient toutes les valeurs du paramètre temp comprises entre les dates renseignées
                C.append(float(g[a1][1])*float(g[a1][2]))#C contient le produit des valeurs des paramètres noise et temp pour les dates comprises entre les dates renseignées
                D.append(g[a1][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label="temp(°C)")
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label="noise(dBA)")
            pl.legend()
            pl.show()
        else:#on retourne seulement la liste de l'indice de corrélation et celle des dates si l'utilisateur ne choisit pas de tracer
            return(valeurcorrelation(C,D))
    elif b=='oui' and a=='2':
        t=input('Quelle date initiale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        k=input('Quelle date finale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        for a2 in range (len(g)):
            if g[a2][6]<=k and g[a2][6]>=t:
                A.append(float(g[a2][1]))#A contient toutes les valeurs du paramètre noise comprises entre les dates renseignées
                B.append(float(g[a2][3]))#B contient toutes les valeurs du paramètre humidity comprises entre les dates renseignées
                C.append(float(g[a2][1])*float(g[a2][3]))#C contient le produit des valeurs des paramètres noise et humidity pour les dates comprises entre les dates renseignées
                D.append(g[a2][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label="humidity(%)")
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label="noise(dBA)")
            pl.legend()
            pl.show()
        else:
            return(valeurcorrelation(C,D))
    elif b=='oui' and a=='3':
        t=input('Quelle date initiale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        k=input('Quelle date finale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        for a3 in range (len(g)):
            if g[a3][6]<=k and g[a3][6]>=t:
                A.append(float(g[a3][1]))#A contient toutes les valeurs du paramètre noise comprises entre les dates renseignées
                B.append(float(g[a3][4]))#B contient toutes les valeurs du paramètre lum comprises entre les dates renseignées
                C.append(float(g[a3][1])*float(g[a3][4]))#C contient le produit des valeurs des paramètres noise et lum pour les dates comprises entre les dates renseignées
                D.append(g[a2][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label="lum(lux)")
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label="noise(dBA)")
            pl.legend()
            pl.show()
        else:#on retourne seulement la liste de l'indice de corrélation et celle des dates si l'utilisateur ne choisit pas de tracer
            return(valeurcorrelation(C,D))
    elif b=='oui' and a=='4':
        t=input('Quelle date initiale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        k=input('Quelle date finale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        for a4 in range (len(g)):
            if g[a4][6]<=k and g[a4][6]>=t:
                A.append(float(g[a4][1]))#A contient les valeurs du paramètre noise comprises entre les dates renseignées
                B.append(float(g[a4][5]))#B contient les valeurs du paramètre co2 comprises entre les dates renseignées
                C.append(float(g[a4][1])*float(g[a4][5]))#C contient le produit des valeurs des paramètres noise et co2 pour les dates comprises entre les dates renseignées
                D.append(g[a4][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label="co2(ppm)")
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label="noise(dBA)")
            pl.legend()
            pl.show()
        else:#on retourne seulement la liste de l'indice de corrélation et celle des dates si l'utilisateur ne choisit pas de tracer
            return(valeurcorrelation(C,D))
    elif b=='oui' and a=='5':
        t=input('Quelle date initiale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        k=input('Quelle date finale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        for a5 in range (len(g)):
            if g[a5][6]<=k and g[a5][6]>=t:
                A.append(float(g[a5][2]))#A contient les valeurs du paramètre temp comprises entre les dates renseignées
                B.append(float(g[a5][3]))#B contient les valeurs du paramètre humidity comprises entre les dates renseignées
                C.append(float(g[a5][2])*float(g[a5][3]))#C contient le produit des valeurs des paramètres temp et humidity pour les dates comprises entre les dates renseignées
                D.append(g[a5][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label="humidity(%)")
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label="temp(°C)")
            pl.legend()
            pl.show()
        else:#on retourne seulement la liste de l'indice de corrélation et celle des dates si l'utilisateur ne choisit pas de tracer
            return(valeurcorrelation(C,D))
    elif b=='oui' and a=='6':
        t=input('Quelle date initiale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        k=input('Quelle date finale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        for a6 in range (len(g)):
            if g[a6][6]<=k and g[a6][6]>=t:
                A.append(float(g[a6][2]))#A contient les valeurs du paramètre temp comprises entre les dates renseignées
                B.append(float(g[a6][4]))#B contient les valeurs du paramètre lum comprises entre les dates renseignées
                C.append(float(g[a6][2])*float(g[a6][4]))#C contient le produit des valeurs des paramètres temp et lum pour les dates comprises entre les dates renseignées
                D.append(g[a6][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label="lum(lux)")
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label="temp(°C)")
            pl.legend()
            pl.show()
        else:#on retourne seulement la liste de l'indice de corrélation et celle des dates si l'utilisateur ne choisit pas de tracer
            return(valeurcorrelation(C,D))
    elif b=='oui' and a=='7':
        t=input('Quelle date initiale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        k=input('Quelle date finale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        for a7 in range (len(g)):
            if g[a7][6]<=k and g[a7][6]>=t:
                A.append(float(g[a7][2]))#A contient les valeurs du paramètre temp comprises entre les dates renseignées
                B.append(float(g[a7][5]))#B contient les valeurs du paramètre co2 comprises entre les dates renseignées
                C.append(float(g[a7][2])*float(g[a7][5]))#C contient le produit des valeurs des paramètres temp et co2 pour les dates comprises entre les dates renseignées
                D.append(g[a7][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label="co2(ppm)")
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label="temp(°C)")
            pl.legend()
            pl.show()
        else:#on retourne seulement la liste de l'indice de corrélation et celle des dates si l'utilisateur ne choisit pas de tracer
            return(valeurcorrelation(C,D))
    elif b=='oui' and a=='8':
        t=input('Quelle date initiale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        k=input('Quelle date finale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        for a8 in range (len(g)):
            if g[a8][6]<=k and g[a8][6]>=t:
                A.append(float(g[a8][3]))#A contient les valeurs du paramètre humidity comprises entre les dates renseignées
                B.append(float(g[a8][4]))#B contient les valeurs du paramètre lum comprises entre les dates renseignées
                C.append(float(g[a8][3])*float(g[a8][4]))#C contient le produit des valeurs des paramètres humidity et lum pour les dates comprises entre les dates renseignées
                D.append(g[a8][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label="lum(lux)")
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label="humidity(%)")
            pl.legend()
            pl.show()
        else:#on retourne seulement la liste de l'indice de corrélation et celle des dates si l'utilisateur ne choisit pas de tracer
            return(valeurcorrelation(C,D))
    elif b=='oui' and a=='9':
        t=input('Quelle date initiale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        k=input('Quelle date finale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        for a9 in range (len(g)):
            if g[a9][6]<=k and g[a9][6]>=t:
                A.append(float(g[a9][3]))#A contient les valeurs du paramètre humidity comprises entre les dates renseignées
                B.append(float(g[a9][5]))#B contient les valeurs du paramètre co2 comprises entre les dates renseignées
                C.append(float(g[a9][3])*float(g[a9][5]))#C contient le produit des valeurs des paramètres humidity et co2 pour les dates comprises entre les dates renseignées
                D.append(g[a9][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label="co2(ppm)")
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label="humidity(%)")
            pl.legend()
            pl.show()
        else:#on retourne seulement la liste de l'indice de corrélation et celle des dates si l'utilisateur ne choisit pas de tracer
            return(valeurcorrelation(C,D))
    elif b=='oui' and a=='10':
        t=input('Quelle date initiale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        k=input('Quelle date finale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        for a10 in range (len(g)):
            if g[a10][6]<=k and g[a10][6]>=t:
                A.append(float(g[a10][4]))#A contient les valeurs du paramètre lum comprises entre les dates renseignées
                B.append(float(g[a10][5]))#B contient les valeurs du paramètre co2 comprises entre les dates renseignées
                C.append(float(g[a10][4])*float(g[a10][5]))#C contient le produit des valeurs des paramètres lum et co2 pour les dates comprises entre les dates renseignées
                D.append(g[a10][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label="co2(ppm)")
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label="lum(lux)")
            pl.legend()
            pl.show()
        else:#on retourne seulement la liste de l'indice de corrélation et celle des dates si l'utilisateur ne choisit pas de tracer
            return(valeurcorrelation(C,D))
    return()
                
#print(indicecorrelation())



def anomalies():
    datechoisie1=input('Quelle date initiale souhaitez vous pour voir si des anomalies sont présentes?(aaaa-mm-jj)')
    datechoisie2=input('Quelle date finale souhaitez vous pour voir si des anomalies sont présentes?(aaaa-mm-jj)(Celle-ci peut-être iidentique à la précédente si vous souhaitez voir les anomalies que pour un seul jour)')
    r=input('Quel paramètre souhaitez vous utiliser?(noise, temp, humidity, lum, co2)')
    noise=separation()[1]#liste des valeurs du paramètre noise
    temp=separation()[2]#liste des valeurs du paramètre temp
    humidity=separation()[3]#liste des valeurs de humidity
    lum=separation()[4]#liste des valeurs du paramètre lum
    co2=separation()[5]#liste des valeurs du paramètre co2
    datesheures=separation()[6]#liste des dates sous la forme aaaa-mm-jj hh:mm:ss+02:00
    dates=separation()[7]#liste des valeurs des dates sous la forme aaaa-mm-jj
    heures=separation()[9]#liste des valeurs des heures sous la forme hh:mm:ss
    noise_datechoisie=[]#liste qui recevra les valeurs du paramètre noise pour la ou les date(s) choisie(s)
    temp_datechoisie=[]#liste qui recevra les valeurs du paramètre temp pour la ou les date(s) choisie
    humidity_datechoisie=[]#liste qui recevra les valeurs du paramètre humidity pour la ou les date choisie(s)
    lum_datechoisie=[]#liste qui recevra les valeurs du paramètre lum pour la ou les date(s) choisie(s)
    co2_datechoisie=[]#liste qui recevra les valeurs du paramètre co2 pour la ou les date(s) choisie(s)
    datesheures_datechoisie=[]#liste qui recevra les valeurs du paramètre dates+heures pour la ou les date(s) choisie(s)
    heures_datechoisie=[]#liste qui recevra les valeurs du paramètre heures pour la ou des  date(s) choisie(s)
    heures_datechoisietriees=[]#liste qui recevra les heures de la ou des date(s) choisie(s) classées par ordre chronologique
    liste_ordonneestrace=[]#liste qui recevra les valeurs en ordonnées des points anomalies à tracer
    liste_abscissestrace=[]#liste qui recevra les dates des valeurs des anomalies à tracer
    g=separation()[8]
    K=[]#liste qui recevra les valeurs à tracer en ordonnée non classées par la fonction tridates
    P=[]
    S=[]#liste qui recevra les dates+heures à placer en abscisse non classées par la fonction tridates
    W1=[]#liste qui renvoie les anomalies sous la forme[[dateheure,'lum',valeurlum,'co2',valeurco2],[dateheure,'noise',valeurnoise],...] par exemple où les noms des(du) paramètre(s) correspond(ent) au(x) paramètre(s) de l'anomalie pour la date qui les/la précède(nt) dans une liste de W1
    for p1 in range (len(dates)):#on parcourt la liste des dates classées selon l'ordre du fichier csv et renvoyée par la fonction séparation
        if datechoisie1<=dates[p1]<=datechoisie2:
            datesheures_datechoisie.append(datesheures[p1])#on ajoute dans cette liste que les dates+heures correspondant à la ou aux date(s) choisie(s)
            noise_datechoisie.append(float(noise[p1]))#on ajoute dans cette liste que les valeurs de noise correspondant à la ou aux date(s) choisie(s)
            temp_datechoisie.append(float(temp[p1]))#on ajoute dans cette liste que les valeurs de temp correspondant à la date choisie
            humidity_datechoisie.append(float(humidity[p1]))#on ajoute dans cette liste que les valeurs de humidity correspondant à la ou aux date(s) choisie(s)
            lum_datechoisie.append(float(lum[p1]))#on ajoute dans cette liste que les valeurs de lum correspondant à la ou aux date(s) choisie(s)
            co2_datechoisie.append(float(co2[p1]))#on ajoute dans cette liste que les valeurs de co2 correspondant à la ou aux date(s) choisie(s)
            heures_datechoisie.append(heures[p1])#on ajoute dans cette liste les valeurs des heures correspondant à la ou aux date(s) choisie(s)
    noise_datechoisietriees=tridates([d1 for d1 in datesheures_datechoisie],[d2 for d2 in noise_datechoisie])[1]#on trie la liste des valeurs de noise obtenue pour la ou les date(s) choisie(s) selon le même ordre que l'ordre chronologique des dates
    temp_datechoisietriees=tridates([d3 for d3 in datesheures_datechoisie],[d4 for d4 in temp_datechoisie])[1]#on trie la liste des valeurs de temp obtenue pour la ou les date(s) choisie(s) selon le même ordre que l'ordre chronologique des dates
    humidity_datechoisietriees=tridates([d5 for d5 in datesheures_datechoisie],[d6 for d6 in humidity_datechoisie])[1]#on trie la liste des valeurs de humidity obtenue pour la ou les date(s) choisie(s) selon le même ordre que l'ordre chronologique des dates
    lum_datechoisietriees=tridates([d7 for d7 in datesheures_datechoisie],[d8 for d8 in lum_datechoisie])[1]#on trie la liste des valeurs de lum obtenue pour la ou les date(s) choisie(s) selon le même ordre que l'ordre chronologique des dates
    co2_datechoisietriees=tridates([d9 for d9 in datesheures_datechoisie],[d10 for d10 in co2_datechoisie])[1]#on trie la liste des valeurs de co2 obtenue pour la ou les date(s) choisie(s) selon le même ordre que l'ordre chronologique des dates
    datesheures_datechoisietriees=tridates([d11 for d11 in datesheures_datechoisie],[d12 for d12 in noise_datechoisie])[0]#cette liste correspond à la liste des dates+heures triée par ordre chronologique
    for g1 in range(len(datesheures_datechoisietriees)):#cela permet d'obtenir les heures classées par ordre chronologique si un intervalle de jours est mentionnée. La fonction tridates ne permettrait pas de faire cela.
        g2=datesheures_datechoisietriees[g1].split(" ")
        heures_datechoisietriees.append(g2[1])
    for x1 in range (1,len(noise_datechoisietriees)):
        if (float(noise_datechoisietriees[x1])>float(noise_datechoisietriees[x1-1])+((15/100)*float(noise_datechoisietriees[x1-1])) or float(noise_datechoisietriees[x1])<float(noise_datechoisietriees[x1-1])-((15/100)*float(noise_datechoisietriees[x1-1]))) and (('00:00:00'<heures_datechoisietriees[x1]<'08:00:00') or ('20:00:00'<heures_datechoisietriees[x1]<'23:59:00')):#si on a une augmentation ou une diminution de 15% sur une valeur de noise_datechoisietriees par rapport à la précédente et que l'heure correspondant à cette valeur est entre minuit et 8h ou entre 20h et 23h59, on ajoute la valeur date+heure correspondante, le nom du paramètre(ici noise) sur lequel porte l'anomalie et la valeur de cette anomalie(noise_datechoisietriees[x1]) dans W1
            W1.append([datesheures_datechoisietriees[x1],'noise',noise_datechoisietriees[x1]])
        elif (float(noise_datechoisietriees[x1])>float(noise_datechoisietriees[x1-1])+((40/100)*float(noise_datechoisietriees[x1-1])) or float(noise_datechoisietriees[x1])<float(noise_datechoisietriees[x1-1])-((40/100)*float(noise_datechoisietriees[x1-1]))) and ('08:00:00'<=heures_datechoisietriees[x1]<='20:00:00'):#si on a une augmentation ou une diminution de 40% sur une valeur de noise_datechoisietriees par rapport à la précédente et que l'heure correspondant à cette valeur est entre 8h et 20h, on ajoute la valeur date+heure correspondante, le nom du paramètre(ici noise) sur lequel porte l'anomalie et la valeur de cette anomalie( noise_datechoisietriees[x1])dans W1
            W1.append([datesheures_datechoisietriees[x1],'noise',noise_datechoisietriees[x1]])
    for a1 in range (1,len(temp_datechoisietriees)):
        if (float(temp_datechoisietriees[a1])>float(temp_datechoisietriees[a1-1])+((7/100)*float(temp_datechoisietriees[a1-1])) or float(temp_datechoisietriees[a1])<float(temp_datechoisietriees[a1-1])-((7/100)*float(temp_datechoisietriees[a1-1]))):#si on a une augmentation ou une diminution de 10% sur une valeur de temp_datechoisietriees par rapport à la précédente
            b1=False
            if len(W1)!=0:#il faut que la liste W1 contienne des anomalies liées aux paramètres précédents
                for a2 in range (len(W1)):
                    if W1[a2][0]==datesheures_datechoisietriees[a1]:#si la date d'une anomalie (contenue dans une liste dans W1) correspondant à un paramètre précédent est la même que celle de l'anomalie décelée par le dernier if, on ajoute à cette liste de W1 'temp' pour indiquer que l'anomalie vient aussi du paramètre temp et on rajoute la valeur de cette anomalie. On change alors la valeur de b1 en true
                        W1[a2].append('temp')
                        W1[a2].append(float(temp_datechoisietriees[a1]))
                        b1=True
            if b1==False:#si b1==False, cela signifie qu'il n'y avait pas de liste de W1 contenant la même date que celle sur laquelle porte l'anomalie décelée par le dernier if. On ajoute alors la date+heure de cette anomalie, le paramètre (ici 'temp') et la valeur de cette anomalie dans W1
                W1.append([datesheures_datechoisietriees[a1],'temp',float(temp_datechoisietriees[a1])])
    for v1 in range (1,len(humidity_datechoisietriees)):
        if (float(humidity_datechoisietriees[v1])>float(humidity_datechoisietriees[v1-1])+((5/100)*float(humidity_datechoisietriees[v1-1])) or float(humidity_datechoisietriees[v1])<float(humidity_datechoisietriees[v1-1])-((5/100)*float(humidity_datechoisietriees[v1-1]))):#si on a une augmentation ou une diminution de 5% sur une valeur de humidity_datechoisietriees par rapport à la précédente 
            n1=False
            if len(W1)!=0:#il faut que la liste W1 contienne des anomalies liées aux paramètres précédents
                for v2 in range (len(W1)):
                    if W1[v2][0]==datesheures_datechoisietriees[v1]:#si la date d'une anomalie (contenue dans une liste dans W1) correspondant à un paramètre précédent est la même que celle de l'anomalie décelée par le dernier if, on ajoute à cette liste de W1 'humidity' pour indiquer que l'anomalie vient aussi du paramètre humidity et on rajoute la valeur de cette anomalie. On change alors la valeur de b1 en true
                        W1[v2].append('humidity')
                        W1[v2].append(float(humidity_datechoisietriees[v1]))
                        n1=True
            if n1==False:#si n1==False, cela signifie qu'il n'y avait pas de liste de W1 contenant la même date que celle sur laquelle porte l'anomalie décelée par le dernier if. On ajoute alors la date+heure de cette anomalie, le paramètre (ici 'humidity') et la valeur de cette anomalie dans W1
                W1.append([datesheures_datechoisietriees[v1],'humidity',float(humidity_datechoisietriees[v1])])
    for a3 in range (1,len(lum_datechoisietriees)):
        if (float(lum_datechoisietriees[a3])>float(lum_datechoisietriees[a3-1])+((10/100)*float(lum_datechoisietriees[a3-1])) or float(lum_datechoisietriees[a3])<float(lum_datechoisietriees[a3-1])-((10/100)*float(lum_datechoisietriees[a3-1]))) and (('00:00:00'<heures_datechoisietriees[a3]<'07:30:00') or ('20:00:00'<heures_datechoisietriees[a3]<'23:59:00')):#si on a une augmentation ou une diminution de 10% sur une valeur de lum_datechoisietriees par rapport à la précédente et que l'heure correspondant à cette valeur est entre minuit et 07h30 ou entre 20h et 23h59. On ne détermine pas les erreurs entre 07:30 et 8h30 car la variation de luminosité due au lever du soleil n'est pas considérée comme une anomalie
            b2=False
            if len(W1)!=0:#il faut que la liste W1 contienne des anomalies liées aux paramètres précédents
                for a4 in range (len(W1)):
                    if W1[a4][0]==datesheures_datechoisietriees[a3]:#si la date d'une anomalie (contenue dans une liste dans W1) correspondant à un paramètre précédent est la même que celle de l'anomalie décelée par le dernier if, on ajoute à cette liste de W1 'lum' pour indiquer que l'anomalie vient aussi du paramètre lum et on rajoute la valeur de cette anomalie. On change alors la valeur de b2 en true
                        W1[a4].append('lum')
                        W1[a4].append(float(lum_datechoisietriees[a3]))
                        b2=True
            if b2==False:#si b2==False, cela signifie qu'il n'y avait pas de liste de W1 contenant la même date que celle sur laquelle porte l'anomalie décelée par le dernier if. On ajoute alors la date+heure de cette anomalie, le paramètre (ici 'lum') et la valeur de cette anomalie dans W1
                W1.append([datesheures_datechoisietriees[a3],'lum',float(lum_datechoisietriees[a3])])
        elif (float(lum_datechoisietriees[a3])>float(lum_datechoisietriees[a3-1])+((50/100)*float(lum_datechoisietriees[a3-1])) or float(lum_datechoisietriees[a3])<float(lum_datechoisietriees[a3-1])-((50/100)*float(lum_datechoisietriees[a3-1]))) and ('08:30:00'<=heures_datechoisietriees[a3]<='19:00:00'):#si on a une augmentation ou une diminution de 50% sur une valeur de lum_datechoisietriees par rapport à la précédente et que l'heure correspondant à cette valeur est entre 09h et 19h. On ne détermine pas les erreurs entre 19h et 20h car la variation de luminosité due au coucher du soleil n'est pas considérée comme une anomalie
            b2=False
            if len(W1)!=0:#il faut que la liste W1 contienne des anomalies liées aux paramètres précédents
                for a4 in range (len(W1)):
                    if W1[a4][0]==datesheures_datechoisietriees[a3]:#si la date d'une anomalie (contenue dans une liste dans W1) correspondant à un paramètre précédent est la même que celle de l'anomalie décelée par le dernier if, on ajoute à cette liste de W1 'lum' pour indiquer que l'anomalie vient aussi du paramètre lum et on rajoute la valeur de cette anomalie. On change alors la valeur de b2 en true
                        W1[a4].append('lum')
                        W1[a4].append(float(lum_datechoisietriees[a3]))
                        b2=True
            if b2==False:#si b2==False, cela signifie qu'il n'y avait pas de liste de W1 contenant la même date que celle sur laquelle porte l'anomalie décelée par le dernier if. On ajoute alors la date+heure de cette anomalie, le paramètre (ici 'lum') et la valeur de l'anomalie dans W1
                W1.append([datesheures_datechoisietriees[a3],'lum',float(lum_datechoisietriees[a3])])
    for a5 in range (1,len(co2_datechoisietriees)):
        if (float(co2_datechoisietriees[a5])>float(co2_datechoisietriees[a5-1])+((15/100)*float(co2_datechoisietriees[a5-1])) or float(co2_datechoisietriees[a5])<float(co2_datechoisietriees[a5-1])-((15/100)*float(co2_datechoisietriees[a5-1]))) and (('00:00:00'<heures_datechoisietriees[a5]<'08:00:00') or ('20:00:00'<heures_datechoisietriees[a5]<'23:59:00')):
            b3=False
            if len(W1)!=0:
                for a6 in range (len(W1)):
                    if W1[a6][0]==datesheures_datechoisietriees[a5]:
                        W1[a6].append('co2')
                        W1[a6].append(float(co2_datechoisietriees[a5]))
                        b3=True
            if b3==False:
                W1.append([datesheures_datechoisietriees[a5],'co2',float(co2_datechoisietriees[a5])])
        elif (float(co2_datechoisietriees[a5])>float(co2_datechoisietriees[a5-1])+((50/100)*float(co2_datechoisietriees[a5-1])) or float(co2_datechoisietriees[a5])<float(co2_datechoisietriees[a5-1])-((50/100)*float(co2_datechoisietriees[a5-1]))) and ('08:00:00'<=heures_datechoisietriees[a5]<='20:00:00'):
            b3=False
            if len(W1)!=0:
                for a6 in range (len(W1)):
                    if W1[a6][0]==datesheures_datechoisietriees[a5]:
                        W1[a6].append('co2')
                        W1[a6].append(float(co2_datechoisietriees[a5]))
                        b3=True
            if b3==False:
                W1.append([datesheures_datechoisietriees[a5],'co2',float(co2_datechoisietriees[a5])])
    for k1 in range (len(W1)):
        for k2 in range (1,len(W1[k1])-1,2):
            if W1[k1][k2]==r:#si le nom du paramètre qui précède la valeur de l'anomalie est celui choisi
                liste_abscissestrace.append(W1[k1][0])#on ajoute à liste_abscissestrace la date+heure de cette anomalie
                liste_ordonneestrace.append(W1[k1][k2+1])#on ajoute à liste_ordonneestrace la valeur de l'anomalie
    for i in range (len(g)):
        if (g[i][6]<=datechoisie2) and (g[i][6]>=datechoisie1):#grâce au module datetime importé au début, on peut comparer deux dates sous la forme str et au format 'aaaa-mm-jj'. On parcourt la liste J[['id1', 'noise1','temp1','humidity1','lum1','co2 1','aaaa-mm-jj','aaaa-mm-jj hh:mm:ss+0200','hh:mm:ss'],...] et on compare les 6°éléments de ces sous listes au dates rentrées par l'utilisateur. Si cette date est comprise entre la date de départ et la date finale rentrées par l'utilisateur, on ajoute à la liste K les éléments que on va mettre en ordonnée( soit noise, soit temp, soit humidity, soit lum, soit co2) et à S la date sous la forme 'aaaa-mm-jj hh:mm:ss+0200'
            P.append(g[i])#on ajoute dans P si la valeur de liste_date est comprise dans l'intervalle de temps mentionné ou correspond à l'unique date rentrée dans datechoisie1 et dans datechoisie2: liste_id,liste_noise,liste_temp,liste_humidity,liste_lum,liste_co2,liste_date,liste_dateheure,liste_heure 
    if r=='noise':
        for j in range (len(P)):
            K.append(P[j][1])
            S.append(P[j][7])
    elif r=='temp':
        for h in range(len(P)):
            K.append(P[h][2])
            S.append(P[h][7])
    elif r=='humidity':
        for k in range(len(P)):
            K.append(P[k][3])
            S.append(P[k][7])
    elif r=='lum':
        for l in range (len(P)):
            K.append(P[l][4])
            S.append(P[l][7])
    elif r=='co2':
        for m in range (len(P)):
            K.append(P[m][5])
            S.append(P[m][7])
    for a in range(len(K)):
        K[a]=float(K[a])#conversion de tous les éléments de K de str en float
    pl.plot(tridates(S,K)[0],tridates(S,K)[1])#on trie les dates pour qu'elles apparaissent par ordre chronologique sur l'axe des abscisses et on leur associe la valeur en ordonnée correspondante
    pl.plot(liste_abscissestrace,liste_ordonneestrace,linestyle='none', marker="o",c='lime',markersize=3)#on fait apparaître les points correspondant à des anomalies
    pl.annotate('points verts=anomalies', (0.65,0.95),xycoords='axes fraction')
    pl.xticks(rotation='vertical')
    pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
    pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
    pl.tick_params(axis = 'x', labelsize = 3)
    if r=='noise':
        pl.ylabel('noise(dBA)')
    elif r=='temp':
        pl.ylabel('temp(°C)')
    elif r=='humidity':
        pl.ylabel('humidity(%)')
    elif r=='lum':
        pl.ylabel('lum(lux)')
    elif r=='co2':
        pl.ylabel('co2(ppm)')
    pl.show()
    return()

print(anomalies())


def maxecart(L):#renvoie l'indice dont la valeur associée correspond à un écart maximal par rapport à la valeur précédente. Si la liste ne contient qu'un ou deux éléments, on renvoie l'indice 0 
    if len(L)==1:
        return(0)
    elif len(L)==2:
        return(0)
    else:
        y=float(L[1])-float(L[0])
        k=0
        for i in range (2,(len(L))-1,2):
            if float(L[i+1])-float(L[i])>y:
                y=float(L[i+1])-float(L[i])
                k=i
    return(k)
        
def minecart(L):#renvoie l'indice dont la valeur associée correspond à un écart minimal par rapport à la valeur précédente. Si la liste ne contient qu'un ou deux éléments, on renvoie l'indice 0 
    if len(L)==1:
        return(0)
    elif len(L)==2:
        return(0)
    else:
        u=float(L[1])-float(L[0])
        h=0
        for i in range (2,len(L)-1,2):
            if float(L[i+1])-float(L[i])<u:
                h=i
                u=float(L[i+1])-float(L[i])
    return(h)



def horaires():
    r=input('Pour quelle date souhaitez-vous connaître les horaires occupation des bureaux?(aaaa-mm-jj sauf 2019-08-11, 2019-08-25(car nous ne disposons pas des horaires de mesure sur toute la journée)')
    g=separation()[8]#liste de sous listes contenant une date avec ses trois formes ('aaaa-mm-ss hh:mm:ss+02:00'(liste_dateheure[u]), 'aaaa-mm-jj'(liste_date[u]), 'hh:mm:ss'(liste_heure[u])) et les éléments 'id', 'noise', 'temp', 'humidity', 'lum', 'co2' associés
    L=[]#la liste L contiendra les valeurs des heures pour la date choisie
    M=[]#la liste M contiendra les valeurs de lum pour la date choisie
    N=[]#la liste N contiendra les valeurs de co2 pour la date choisie
    U=[]#la liste U contiendra les valeurs de noise pour la date choisie
    P=[]#liste qui, si les listes I,K et F sont vides recevra les valeurs de co2 pour lesquelles l'heure associée est comprise entre 07:45 et 09:40 et la luminosité associée est supérieure à 108 lux. Sinon, cette liste comporte les valeurs de co2 de K pour lesquelles l'heure associée dans I est comprise entre 07:45 et 09:40 et la valeur de lum associée dans F est supérieure à 120lux.
    G=[]#liste qui, si les listes I,K et F sont vides recevra les valeurs des heures si celles-ci sont comprises entre 07:45 et 09:40 et si la luminosité associée est supérieure à 108 lux. Sinon, cette liste comporte les valeurs des heures de I comprises entre 07:45 et 09:40 et pour lesquelles la valeur de lum associée dans F est supérieure à 120lux
    F=[]#liste qui contiendra toutes les valeurs du paramètre lum associées à une date pour laquelle il y a une augmentation de bruit par rapport à la précédente après avoir ordonné les paramètres selon l'ordre chronologique des dates avec la fonction tridates
    I=[]#liste qui contiendra toutes les heures correspondant à une augmentation de bruit  après avoir ordonné les paramètres selon l'ordre chronologique des dates avec la fonction tridates
    K=[]#liste qui contiendra toutes les valeurs du paramètre co2 associées à une date pour laquelle il y a une augmentation de bruit par rapport à la précédente après avoir ordonné les paramètres selon l'ordre chronologique des dates avec la fonction tridates
    O=[]#liste qui contiendra toutes les valeurs des heures correspondant à une diminution du paramètre noise associé par rapport à la date précécdente 
    Q=[]#liste qui contiendra toutes les valeurs du paramètre co2 correspondant à une diminution du paramètre noise associé par rapport à la date précédente
    V=[]#liste qui contiendra toutes les valeurs du paramètre lum correspondant à une diminution du paramètre noise associé par rapport à la date précédente
    A1=[]#la liste A1 comporte les valeurs du co2 contenues dans Q et dont la date associée est comprise entre 11:45 et 13:30
    A2=[]#la liste A1 comporte les heures contenues dans O et comprises entre 11:45 et 13:30
    X=[]#liste qui contiendra toutes les heures dont la valeur de noise associée correspond à une augmentation par rapport à la précédente
    H=[]#liste qui contiendra toutes les valeurs de co2 dont la valeur de noise associée à la même date correspond à une augmentation par rapport à la précédente
    E=[]#liste qui contiendra toutes les valeurs de lum dont la valeur de noise associée à la même date correspond à une augmentation par rapport à la précédente
    B1=[]#liste qui contiendra les valeurs de co2 de H dont les heures associées sont  comprises entre 13:45 et 14:30 dont la valeur de lum associée est supérieure à 120 lux
    B2=[]#liste qui contiendra les heures de X comprises entre 13:45 et 14:30 dont la valeur de lum associée est supérieure à 120 lux
    C1=[]#liste qui contiendra toutes les heures dont la valeur de noise associée correspond à une diminution par rapport à la précédente
    C2=[]#liste qui contiendra toutes les valeurs de co2 dont la valeur de noise associée à la même date correspond à une diminution par rapport à la précédente
    C3=[]#liste qui contiendra toutes les valeurs de lum dont la valeur de noise associée à la même date correspond à une diminution par rapport à la précédente
    C4=[]#liste qui contiendra les valeurs de co2 de C2 dont l'heure associée est comprise entre 16:30 et 19:30
    C5=[]#liste qui contiendra les valeurs des heures de C1 comprises entre 16:30 et 19:30
    W=['heure arrivée matin','heure départ pause déjeuner','heure retour pause déjeuner','heure départ soir']
    for i in range (len(g)):
        if g[i][6]==r:
            L.append(g[i][8])#on ajoute dans L les heures 'hh:mm:ss+02:00' de la date choisie
            U.append(g[i][1])#on ajoute dans U les noises de la date choisie
            M.append(g[i][4])#on ajoute dans M les lum de la date choisie
            N.append(g[i][5])#on ajoute dans N les co2 de la date choisie
    A=tridates(L,M)[0]# on récupère dans A les heures choisies classées par ordre chronologique
    B=tridates(L,M)[1]#on récupère dans B les valeurs de lum classées selon l'ordre de A
    C=tridates(L,N)[1]#on récupère dans C les valeurs de co2 classées selon l'ordre de A
    D=tridates(L,U)[1]#on récupère dans D les valeurs de noise classées selon l'ordre de A
    t=0
    while t<len(D)-1:
        if D[t+1]>=D[t]:#si il y a une augmentation du bruit d'une heure t hh:mm:ss à la suivante t+1( qui est sûrement liée à l'arrivée des employés dans le bureau, on ajoute l'heure t dans I, le co2 de cette date dans K et le lum de cette date dans F. On fait ça pour tous les éléments de D
            I.append(A[t])
            K.append(C[t])
            F.append(B[t])
        t=t+1 
    if len(I)==0:
        w1=0
        while w1<len(A):
            if '07:45:00'<A[w1]<'09:40:00' and int(B[w1])>=108:#si la liste I est vide, on enlève la contrainte de l'augmentation du bruit d'une heure à la suivante et on réduit la contrainte sur les 120 lux qui va suivre dans la prochaine boucle while de 10%
                P.append(C[w1])
                G.append(A[w1])
            w1=w1+1
    else:
        j=0
        while j<len(I):
            if '07:45:00'<I[j]<'09:40:00' and int(F[j])>=120:#parmi les dates de la liste I triées avec la boucle while précédente, on ne sélectionne que celles comprises entre 07:45:00 et 09:40:00( environ la plage horaire où les employés arrivent) et dont la luminosité est supérieure à 120 lux(une règlementation oblige aux patrons un minimum de  120 lux pour ses employés pour travailler dans un bureau) et on ajoute dans G ces dates et dans P le co2 de ces dates
                P.append(K[j])
                G.append(I[j])
            j=j+1
        if len(P)==0 and len(G)==0:#si avec les contraintes de l'augmentation du bruit d'une heure à la suivante, la date comprise entre 07:45:00 et 09:40:00 et la luminosité d'une date supérieure à 120, il n'y a aucune date remplissant ces critères dans A, on enlève la contrainte de l'augmentation du bruit d'une heure de A à la suivante
            w2=0
            while w2<len(A):
                if '07:45:00'<A[w2]<'09:40:00' and int(B[w2])>=120:
                    P.append(C[w2])
                    G.append(A[w2])
                w2=w2+1
    z=maxecart(P)#parmi les dates restantes dans G, la fonction maxecart me permet de calculer l'écart maximal entre le co2 d'une date et de la suivante( pour l'horaore d'arrivée au bureau, il devrait y avoir une forte augmentation de co2 causé par la respiration des employés) et de renvoyer l'indice de la date pour laquelle l'augmentation du co2 est maximale avec celle qui suit.
    W.append(G[z])#on ajoute dans W la date sélectionnée juste avant: c'est la date d'arrivée des employés au bureau le matin
    s=0
    while s<len(D)-1:
        if D[s+1]<=D[s]:
            O.append(A[s])
            Q.append(C[s])
            V.append(B[s])
        s=s+1
    d=0
    while d<len(O):
        if '11:45:00'<O[d]<'13:30:00':#parmi les dates triées avec la boucle while précédente et mises dans la liste O, on ne fait pas intervenir la luminosité car aux alentours de midi, celle-ci reste supérieure à 120 lux avec la contribution de la lumière naturelle et comme les employés ne sont plus présents, la réglementation imposant 120 lux pour le travail en bureau ne s'applique plus
            A1.append(Q[d])
            A2.append(O[d])
        d=d+1
    w=minecart(A1)
    W.append(A2[w])
    l=0
    while l<len(D)-1:
        if D[l+1]>=D[l]:
            X.append(A[l])
            H.append(C[l])
            E.append(B[l])
        l=l+1
    k=0
    while k<len(X):
        if '13:45:00'<X[k]<'14:30:00' and int(E[k])>=120:#pour le retour de la pose déjeuner, on reprend le critère lum>120 car les employés se remettent à travailler et la règlementation impose ce minimum de luminosité. Je n'enlève pas de conditions comme précédemment pour l'horaire d'arrivée si X et H sont vides ou si B1 et B2 sont vides car en testant sur les dates, je n'ai pas eu de problème de ce type( alors qu'on en avait eu pour l'horaire d'arrivée)
            B1.append(H[k])
            B2.append(X[k])
        k=k+1
    v=maxecart(B1)
    W.append(B2[v])
    z1=0
    while z1<len(L)-1:
        if D[z1+1]<=D[z1]:
            C1.append(A[z1])
            C2.append(C[z1])
            C3.append(B[z1])
        z1=z1+1
    e1=0
    while e1<len(C1):
        if '16:30:00'<C1[e1]<'19:30:00':#on ne rajoute pas le critère de la luminosité inférieure à 120 car les dates sont en Août et Septembre et la luminosité reste supérieure à 120 lux entre 16:30:00 et 19:30:00 du fait de la lumière naturelle à ce moment de l'année
                C4.append(C2[e1])
                C5.append(C1[e1])
        e1=e1+1
    n=minecart(C4)
    W.append(C5[n])
    return(W)#W contient les horaires dans l'ordre suivant: arrivée matin, départ déjeuner, retour déjeuner, départ soir
    
#print(horaires())