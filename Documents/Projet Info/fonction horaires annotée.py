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

