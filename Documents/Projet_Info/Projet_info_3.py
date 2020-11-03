import matplotlib.pyplot as pl
import matplotlib
import numpy as np
import math as mp
import time
from datetime import datetime
from datetime import time

def fonction1():#fonction pour afficher le tableau où toutes les données sont séparées par des points virgules et sous le format str: 'id1';'noise1';'temp1';'humidity1';'lum1';'co2 1';'aaaa-mm-jj hh:mm:ss+0200';'id2';'noise2'...
    f=open('/Users/felixmaquin/Documents/Projet Info/données tableau texte.txt')
    tab=f.readlines()
    for ligne in (tab):
        return(ligne)
#print(fonction1())

def separation():
    L=[] #liste contenant les id sous la forme 'id'
    M=[] # liste contenant  le paramètre noise sous la forme 'noise'
    N=[] # liste contenant le paramètre temp sous la forme 'temp'
    P=[] # liste contenant le paramètre humidity sous la forme 'humidity'
    I=[] # liste contenant le paramètre lum sous la forme 'lum'
    E=[] # liste contenant le paramètre co2 sous la forme 'co2'
    C=[] # liste contenant date et heure sous la forme 'aaaa-mm-jj hh:mm:ss +0200'
    Y=[] # liste contenant seulement la date sous la forme 'aaaa-mm-jj'
    J=[]
    Z=[] # liste contenant seulement les heures sous la forme 'hh:mm:ss'
    Q=fonction1()
    A=Q.split(";")#dès qu'un point virgule est rencontré, la fonction split prend l'élément juste avant et juste après le point virgule et les met dans une liste séparés par des virgules
    for i in range (0,len(A)-6,7):#je ne sélectionne que les identifiants qui sont présents dans la liste aux positions multiples de 7: id1,noise1,temp1,humidity1,lum1,co2 1, sent_at1,id2,...
        L.append(A[i])
    for j in range(1,len(A)-5,7):#je ne sélectionne que les éléments de noise que je mets dans une liste
        M.append(A[j])
    for k in range(2,len(A)-4,7):#je ne sélectionne que les éléments de temp que je mets dans une liste
        N.append(A[k])
    for g in range(3,len(A)-3,7):#je ne sélectonne que les éléments de humidity que je mets dans une liste
        P.append(A[g])
    for h in range(4,len(A)-2,7):#je ne sélectionne que les éléments de lum  que je mets dans une liste
        I.append(A[h])
    for z in range(5,len(A)-1,7):#je ne sélectionne que les éléments de co2 que je mets dans une liste
        E.append(A[z])
    for r in range (6,len(A),7):#je ne sélectionne que les éléments de sent_at sous la forme aaaa-mm-jj hh:mm:ss+0200 que je mets dans une liste
        C.append(A[r])
    for b in range(len(C)):#dans la liste précédente, pour chaque sent_at, dès que l'espace séparant le jour et l'heure est rencontré, je place dans la liste Y que 'aaaa-mm-jj' et dans la liste Z que 'hh:mm:ss'(je ne sais pas pourquoi le +0200 disparait)
        e=C[b].split(" ")
        Y.append(e[0])
        Z.append(e[1])
    for u in range (len(L)):
        J.append([L[u],M[u],N[u],P[u],I[u],E[u],Y[u],C[u],Z[u]])#la liste J contient donc des sous listes contenant une date avec ses trois formes ('aaaa-mm-ss hh:mm:ss+0200'(C[u]), 'aaaa-mm-jj'(Y[u]), 'hh:mm:ss'(Z[u])) et les éléments id, noise, temp, humidity, lum, co2 associés
    d=len(J)
    J[d-1][7].strip('"\n')
    return(L,M,N,P,I,E,C,Y,J,Z)
#print(separation())



#print(separation(Q)[7])    
import math as mp
import time
from datetime import datetime
from matplotlib.dates import AutoDateLocator

def calcmin(L):
    c=0
    for i in range (len(L)):
        if float(L[i])<=float(L[c]):#je mets des float car dans les listes que je crée avec la fonction separation, les éléments sont sous la forme '134' par exemple
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
    
  
def tridates(L,M):# j'ai crée cette fonction parce que dans le tableau des dates, tu as des données pour une date à différents endroits du tableau. Comme je vais faire mes tracés avec la liste C de séparation qui prend les dates suivant l'ordre du tableau de données, lors de mes tracés, j'avais sur l'axe des abscisses des données pas classées par ordre chronologique de gauche à droite sur l'axe. Cette fonction trie les dates par ordre croissant dans une liste et met à la même position de cette date la valeur de noise, temp, humidity, lum ou co2 dans la liste correspondante. 
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
    K=[]
    S=[]
    g=separation()[8]#la liste J de la fonction separation
    a1=separation()[1]#liste des éléments de noise
    a2=separation()[2]#liste des éléments de temp
    a3=separation()[3]#liste des éléments de humidity
    a4=separation()[4]#liste des éléments de lum
    a5=separation()[5]#liste des éléments de co2
    r=input('Quelle variable souhaitez vous utiliser?((noise,temp, humidity, lum ou co2)')
    o=input('Souhaitez-vous spécifier un intervalle de temps?(oui/non)')
    if o=='non':
        if r=='noise':
            for b1 in range(len(a1)):
                K.append(float(a1[b1]))#je rajoute chaque élément de a1 dans K sous la forme d'un float
            pl.plot(tridates(separation()[6],K)[0],tridates(separation()[6],K)[1])#je trace avec un ordre chronologique sur l'axe des abscisses avec la fonction tridates
            pl.ylabel('noise(UI)')
            pl.xticks(rotation='vertical')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))#je fais apparaitre que 8 dates clés sur l'axe des ordonnées
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))#je fais apparaître que 8 dates clés sur l'axe des abscisses
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.show()
        elif r=='temp':
            for b2 in range (len(a2)):
                K.append(float(a2[b2]))
            pl.plot(tridates(separation()[6],K)[0],tridates(separation()[6],K)[1])
            pl.ylabel('temp(UI)')
            pl.xticks(rotation='vertical')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.show()
        elif r=='humidity':
            for b3 in range (len(a3)):
                K.append(float(a3[b3]))
            pl.plot(tridates(separation()[6],K)[0],tridates(separation()[6],K)[1])
            pl.ylabel('humidity(UI)')
            pl.xticks(rotation='vertical')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.show()
        elif r=='lum':
            for b4 in range (len(a4)):
                K.append(float(a4[b4]))
            pl.plot(tridates(separation()[6],K)[0],tridates(separation()[6],K)[1])
            pl.ylabel('lum(UI)')
            pl.xticks(rotation='vertical')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.show()
        elif r=='co2':
            for b5 in range (len(a5)):
                K.append(a5[b5])
            pl.plot(tridates(separation()[6],K)[0],tridates(separation()[6],K)[1])
            pl.ylabel('co2(UI)')
            pl.xticks(rotation='vertical')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.show()
    else:
        t=input('Quelle date initiale souhaitez-vous pour évolution de cette variable?(aaaa-mm-jj)')
        f=input('Quelle date finale souhaitez-vous pour évolution de cette variable?(aaaa-mm-jj)')
        for i in range (len(g)):
            if g[i][6]<=f and g[i][6]>=t:#grâce au module datetime importé au début, je peux comparer deux dates sous la forme str et au format 'aaaa-mm-jj'. Je parcours la liste J[['id1', 'noise1','temp1','humidity1','lum1','co2 1','aaaa-mm-jj','aaaa-mm-jj hh:mm:ss+0200','hh:mm:ss'],...] et je compare les 6°éléments de ces sous listes au dates rentrées par l'utilisateur. Si cette date est comprise entre la date de départ et la date finale rentrées par l'utilisateur, j'ajoute à la liste K les éléments que je vais mettre en ordonnée( soit noise, soit temp, soit humidity, soit lum, soit co2) et à S la date sous la forme 'aaaa-mm-jj hh:mm:ss+0200'
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
    for a in range(len(K)):
        K[a]=float(K[a])#je convertis tous les éléments de K de str en float
    pl.xticks(rotation='vertical')
    pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
    pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
    pl.tick_params(axis = 'x', labelsize = 3)
    if r=='noise':
        pl.ylabel('noise(UI)')
    elif r=='temp':
        pl.ylabel('temp(UI)')
    elif r=='humidity':
        pl.ylabel('humidity(UI)')
    elif r=='lum':
        pl.ylabel('lum(UI)')
    elif r=='co2':
        pl.ylabel('co2(UI)')
    pl.plot(tridates(S,K)[0],tridates(S,K)[1])#je trie les dates pour qu'elles apparaissent par ordre chronologique sur l'axe des abscisses
    pl.show()
    return()
            
#print(trace1())

def inter():# exactement la même fonction que trace1 sauf qu'au lieu de faire un tracé, je renvoie les listes qui me servent à faire les tracés de la fonction trace1
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



def ajouttrace():# dans cette fonction, je vais faire apparaitre le min, le max, la moyenne, l'écart type, la médiane et la variance si l'utilisateur le souhaite
    u=input('Voulez vous faire apparaître min, max, moyenne, ecart type, mediane, variance?')
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
            pl.ylabel('noise(UI)')
        elif v[2]=='temp':
            pl.ylabel('temp(UI)')
        elif v[2]=='humidity':
            pl.ylabel('humidity(UI)')
        elif v[2]=='lum':
            pl.ylabel('lum(UI)')
        elif v[2]=='co2':
            pl.ylabel('co2(UI)')
        pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
        pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
        pl.xticks(rotation='vertical')#j'écris les dates sur l'axe des abscisses verticalement
        pl.tick_params(axis = 'x', labelsize = 3)#je réduis la taille de la police sur l'axe des abscisses.
        pl.show()
    return()

#print(ajouttrace())  


    
def temprosee(T,h):#j'ai trouvé la formule sur internet
    a=17.27
    b=237.7
    return((b*(((a*T)/b+T)+np.log(h/100)))/(a-(((a*T)/(b+T))+np.log(h/100))))
    
def humidex(T,h):#j'ai trouvé la formule sur internet. T est la température et h l'humidité
    return(T+0.5555*(6.11*np.exp(5417.7530*((1/273.16)-(1/(273.15+temprosee(T,h))))-10)))
    
def tracehumidex():#cette fonction permet de tracer l'indice humidex en fonction des dates
    I=[]
    M=[]
    P=[]
    g=separation()[8]
    f=input('Souhaitez vous spécifier un intervalle de temps?')
    if f=='non':
        for i in range (len(g)):
            I.append(humidex(float(g[i][2]),float(g[i][3])))
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
        pl.plot(tridates(P,I)[0],tridates(P,I)[1])
        pl.ylabel('humidex')
        pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
        pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
        pl.xticks(rotation='vertical')
        pl.tick_params(axis = 'x', labelsize = 3)
        pl.show()
    return()
        
#print(tracehumidex())
       
import time
from datetime import datetime
from datetime import time     
       
    
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
    return(round(((calcmoy(D))-((calcmoy(L))*(calcmoy(M))))/ecarttype(L)*ecarttype(M),2))


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
            A.append(float(g[a1][1]))
            B.append(float(g[a1][2]))
            C.append(float(g[a1][1])*float(g[a1][2]))
            D.append(g[a1][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label='temp')
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label='noise')
            pl.legend()
            pl.show()
        else:
            return(valeurcorrelation(C,A,B))
    elif b=='non' and a=='2':
        for a2 in range (len(g)):
            A.append(float(g[a2][1]))
            B.append(float(g[a2][3]))
            C.append(float(g[a2][1])*float(g[a2][3]))
            D.append(g[a2][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label="humidity")
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label="noise")
            pl.legend()
            pl.show()
        else:
            return(valeurcorrelation(C,A,B))
    elif b=='non' and a=='3':
        for a3 in range (len(g)):
            A.append(float(g[a3][1]))
            B.append(float(g[a3][4]))
            C.append(float(g[a3][1])*float(g[a3][4]))
            D.append(g[a2][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label="lum")
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label="noise")
            pl.legend()
            pl.show()
        else:
            return(valeurcorrelation(C,A,B))
    elif b=='non' and a=='4':
        for a4 in range (len(g)):
            A.append(float(g[a4][1]))
            B.append(float(g[a4][5]))
            C.append(float(g[a4][1])*float(g[a4][5]))
            D.append(g[a4][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label="co2")
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label="noise")
            pl.legend()
            pl.show()
        else:
            return(valeurcorrelation(C,A,B))
    elif b=='non' and a=='5':
        for a5 in range (len(g)):
            A.append(float(g[a5][2]))
            B.append(float(g[a5][3]))
            C.append(float(g[a5][2])*float(g[a5][3]))
            D.append(g[a5][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label="humidity")
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label="temp")
            pl.legend()
            pl.show()
        else:
            return(valeurcorrelation(C,A,B))
    elif b=='non' and a=='6':
        for a6 in range (len(g)):
            A.append(float(g[a6][2]))
            B.append(float(g[a6][4]))
            C.append(float(g[a6][2])*float(g[a6][4]))
            D.append(g[a6][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label="lum")
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label="temp")
            pl.legend()
            pl.show()
        else:
            return(valeurcorrelation(C,A,B))
    elif b=='non' and a=='7':
        for a7 in range (len(g)):
            A.append(float(g[a7][2]))
            B.append(float(g[a7][5]))
            C.append(float(g[a7][2])*float(g[a7][5]))
            D.append(g[a7][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label="co2")
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label="temp")
            pl.legend()
            pl.show()
        else:
            return(valeurcorrelation(C,A,B))
    elif b=='non' and a=='8':
        for a8 in range (len(g)):
            A.append(float(g[a8][3]))
            B.append(float(g[a8][4]))
            C.append(float(g[a8][3])*float(g[a8][4]))
            D.append(g[a8][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label="lum")
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label="humidity")
            pl.legend()
            pl.show()
        else:
            return(valeurcorrelation(C,A,B))
    elif b=='non' and a=='9':
        for a9 in range (len(g)):
            A.append(float(g[a9][3]))
            B.append(float(g[a9][5]))
            C.append(float(g[a9][3])*float(g[a9][5]))
            D.append(g[a9][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label="co2")
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label="humidity")
            pl.legend()
            pl.show()
        else:
            return(valeurcorrelation(C,A,B))
    elif b=='non' and a=='10':
        for a10 in range(len(g)):
            A.append(float(g[a10][4]))
            B.append(float(g[a10][5]))
            C.append(float(g[a10][4])*float(g[a10][5]))
            D.append(g[a10][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label="co2")
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label="lum")
            pl.legend()
            pl.show()
        else:
            return(valeurcorrelation(C,A,B))
    elif b=='oui' and a=='1':
        t=input('Quelle date initiale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        k=input('Quelle date finale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        for a1 in range (len(g)):
            if g[a1][6]<=k and g[a1][6]>=t:
                A.append(float(g[a1][1]))
                B.append(float(g[a1][2]))
                C.append(float(g[a1][1])*float(g[a1][2]))
                D.append(g[a1][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label="temp")
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label="noise")
            pl.legend()
            pl.show()
        else:
            return(valeurcorrelation(C,A,B))
    elif b=='oui' and a=='2':
        t=input('Quelle date initiale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        k=input('Quelle date finale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        for a2 in range (len(g)):
            if g[a2][6]<=k and g[a2][6]>=t:
                A.append(float(g[a2][1]))
                B.append(float(g[a2][3]))
                C.append(float(g[a2][1])*float(g[a2][3]))
                D.append(g[a2][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label="humidity")
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label="noise")
            pl.legend()
            pl.show()
        else:
            return(valeurcorrelation(C,A,B))
    elif b=='oui' and a=='3':
        t=input('Quelle date initiale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        k=input('Quelle date finale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        for a3 in range (len(g)):
            if g[a3][6]<=k and g[a3][6]>=t:
                A.append(float(g[a3][1]))
                B.append(float(g[a3][4]))
                C.append(float(g[a3][1])*float(g[a3][4]))
                D.append(g[a2][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label="lum")
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label="noise")
            pl.legend()
            pl.show()
        else:
            return(valeurcorrelation(C,A,B))
    elif b=='oui' and a=='4':
        t=input('Quelle date initiale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        k=input('Quelle date finale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        for a4 in range (len(g)):
            if g[a4][6]<=k and g[a4][6]>=t:
                A.append(float(g[a4][1]))
                B.append(float(g[a4][5]))
                C.append(float(g[a4][1])*float(g[a4][5]))
                D.append(g[a4][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label="co2")
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label="noise")
            pl.legend()
            pl.show()
        else:
            return(valeurcorrelation(C,A,B))
    elif b=='oui' and a=='5':
        t=input('Quelle date initiale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        k=input('Quelle date finale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        for a5 in range (len(g)):
            if g[a5][6]<=k and g[a5][6]>=t:
                A.append(float(g[a5][2]))
                B.append(float(g[a5][3]))
                C.append(float(g[a5][2])*float(g[a5][3]))
                D.append(g[a5][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label="humidity")
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label="temp")
            pl.legend()
            pl.show()
        else:
            return(valeurcorrelation(C,A,B))
    elif b=='oui' and a=='6':
        t=input('Quelle date initiale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        k=input('Quelle date finale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        for a6 in range (len(g)):
            if g[a6][6]<=k and g[a6][6]>=t:
                A.append(float(g[a6][2]))
                B.append(float(g[a6][4]))
                C.append(float(g[a6][2])*float(g[a6][4]))
                D.append(g[a6][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label="lum")
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label="temp")
            pl.legend()
            pl.show()
        else:
            return(valeurcorrelation(C,A,B))
    elif b=='oui' and a=='7':
        t=input('Quelle date initiale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        k=input('Quelle date finale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        for a7 in range (len(g)):
            if g[a7][6]<=k and g[a7][6]>=t:
                A.append(float(g[a7][2]))
                B.append(float(g[a7][5]))
                C.append(float(g[a7][2])*float(g[a7][5]))
                D.append(g[a7][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label="co2")
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label="temp")
            pl.legend()
            pl.show()
        else:
            return(valeurcorrelation(C,A,B))
    elif b=='oui' and a=='8':
        t=input('Quelle date initiale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        k=input('Quelle date finale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        for a8 in range (len(g)):
            if g[a8][6]<=k and g[a8][6]>=t:
                A.append(float(g[a8][3]))
                B.append(float(g[a8][4]))
                C.append(float(g[a8][3])*float(g[a8][4]))
                D.append(g[a8][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label="lum")
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label="humidity")
            pl.legend()
            pl.show()
        else:
            return(valeurcorrelation(C,A,B))
    elif b=='oui' and a=='9':
        t=input('Quelle date initiale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        k=input('Quelle date finale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        for a9 in range (len(g)):
            if g[a9][6]<=k and g[a9][6]>=t:
                A.append(float(g[a9][3]))
                B.append(float(g[a9][5]))
                C.append(float(g[a9][3])*float(g[a9][5]))
                D.append(g[a9][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label="co2")
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label="humidity")
            pl.legend()
            pl.show()
        else:
            return(valeurcorrelation(C,A,B))
    elif b=='oui' and a=='10':
        t=input('Quelle date initiale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        k=input('Quelle date finale souhaitez-vous pour évolution des variables?(aaaa-mm-jj)')
        for a10 in range (len(g)):
            if g[a10][6]<=k and g[a10][6]>=t:
                A.append(float(g[a10][4]))
                B.append(float(g[a10][5]))
                C.append(float(g[a10][4])*float(g[a10][5]))
                D.append(g[a10][7])
        if c=='1':
            pl.gca().annotate(valeurcorrelation(C,A,B),(0.93,0.95),xycoords='axes fraction')
            pl.gca().annotate('indicecorrelation=',(0.63,0.95),xycoords='axes fraction')
            pl.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
            pl.xticks(rotation='vertical')
            pl.tick_params(axis = 'x', labelsize = 3)
            pl.plot(tridates(D,B)[0],tridates(D,B)[1],label="co2")
            pl.plot(tridates(D,A)[0],tridates(D,A)[1],label="lum")
            pl.legend()
            pl.show()
        else:
            return(valeurcorrelation(C,A,B))
    return()
                
#print(indicecorrelation())
        
            
            
        
    
    
    

        
        






