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
    for r in range (6,len(A),7):#je ne sélectionne que les éléments de sent_at sous la forme 'aaaa-mm-jj hh:mm:ss+0200' que je mets dans une liste
        C.append(A[r])
    for b in range(len(C)):#dans la liste précédente, pour chaque sent_at, dès que l'espace séparant le jour et l'heure est rencontré, je place dans la liste Y que 'aaaa-mm-jj' et dans la liste Z que 'hh:mm:ss'(nous ne savons pas pourquoi le +0200 disparait)
        e=C[b].split(" ")
        Y.append(e[0])
        Z.append(e[1])
    for u in range (len(L)):
        J.append([L[u],M[u],N[u],P[u],I[u],E[u],Y[u],C[u],Z[u]])#la liste J contient donc des sous listes contenant une date avec ses trois formes ('aaaa-mm-ss hh:mm:ss+0200'(C[u]), 'aaaa-mm-jj'(Y[u]), 'hh:mm:ss'(Z[u])) et les éléments id, noise, temp, humidity, lum, co2 associés
    d=len(J)
    J[d-1][7].strip('"\n')
    return(L,M,N,P,I,E,C,Y,J,Z)
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
    w=input('Pour quelle date souhaitez vous voir si des anomalies sont présentes?(aaaa-mm-jj)')
    A=separation()[1]#liste des valeurs du paramètre noise
    B=separation()[2]#liste des valeurs du paramètre temp
    B2=separation()[3]#liste des valeurs de humidity
    C=separation()[4]#liste des valeurs du paramètre lum
    D=separation()[5]#liste des valeurs du paramètre co2
    E=separation()[6]#liste des valeurs des dates sous la forme 'aaaa-mm-jj hh:mm:ss+0200'
    I1=separation()[7]#liste des valeurs des dates sous la forme 'aaaa-mm-jj'
    S=[]
    H=[]
    O=[]
    M=[]
    K=[]
    L=[]
    T=[]
    W1=[]
    for p1 in range (len(I1)):
        if I1[p1]==w:
            S.append(float(A[p1]))
            H.append(float(B[p1]))
            O.append(float(B2[p1]))
            M.append(float(C[p1]))
            K.append(float(D[p1]))
            L.append(E[p1])
            T.append(U[p1])
    C1=tridates(L,S)[1]
    C2=tridates(L,H)[1]
    E1=tridates(L,O)[1]
    C3=tridates(L,M)[1]
    C4=tridates(L,K)[1]
    C5=tridates(L,K)[0]
    C6=tridates(T,S)[0]
    return(L)
    
print(anomalies())