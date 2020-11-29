
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
            return(valeurcorrelation(C,A,B),D)
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
            return(valeurcorrelation(C,A,B),D)
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
            return(valeurcorrelation(C,A,B),D)
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
            return(valeurcorrelation(C,A,B),D)
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
            return(valeurcorrelation(C,A,B),D)
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
            return(valeurcorrelation(C,A,B),D)
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
            return(valeurcorrelation(C,A,B),D)
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
            return(valeurcorrelation(C,A,B),D)
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
            return(valeurcorrelation(C,A,B),D)
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
            return(valeurcorrelation(C,A,B),D)
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
            return(valeurcorrelation(C,A,B),D)
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
            return(valeurcorrelation(C,A,B),D)
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
            return(valeurcorrelation(C,A,B),D)
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
            return(valeurcorrelation(C,A,B),D)
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
            return(valeurcorrelation(C,A,B),D)
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
            return(valeurcorrelation(C,A,B),D)
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
            return(valeurcorrelation(C,A,B),D)
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
            return(valeurcorrelation(C,A,B),D)
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
            return(valeurcorrelation(C,A,B),D)
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
            return(valeurcorrelation(C,A,B),D)
    return()
                
#print(indicecorrelation())