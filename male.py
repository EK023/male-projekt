import pygame

pygame.init()


    
            

#ettur(pawn),vanker(rook),ratsu(horse),oda(bishop),kuningas,lipp(queen)//
algseis= [['v','r','o','l','k','o','r','v'],
          ['e','E','e','e','e','e','e','e'],		#väikse tähega on mustad ja esitähega on eristatavad nupud
          [' ','L',' ','r',' ',' ',' ','L'],
          [' ',' ',' ',' ',' ',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' '],
          ['E','E','E','E','E','E','E','E'],		#suure tähega valged
          ['V','R','O','L','K','O','R','V']]
valged=['V','R','O','L','K','E']
mustad=['v','r','o','l','k','e']
def värv(nupu_pos):		#Leiab, mis värvi nupuga tegemist on, vastavalt, kas tegemist on suure või väikse tähega
    if algseis[nupu_pos[0]][nupu_pos[1]].islower():
        pool='M'
    else:
        pool='V'
    return pool
def vaenlased(pool):		#tagastab järjendi, kus on kõik võimalikud vaenlased
    if pool == 'V':
        return mustad
    else:
        return valged
def omad(pool):		#Pole vist isegi vaja
    if pool == 'V':
        return valged
    else:
        return mustad
def vankri_käigud(seis,vankri_pos): 		#värvi on tegelikult võimalik leida ka nupu positsioonist(kas ta on väike või suur täht)
    pool=värv(vankri_pos)
    vastased = vaenlased(pool)
    rida=vankri_pos[0]
    veerg=vankri_pos[1]
    käigud=[]
    for i in range(rida+1,8):	#paremale käigud
        if seis[i][veerg] in vastased:
            käigud.append([i,veerg])
            break
        elif seis[i][veerg] == ' ':
            käigud.append([i,veerg])
        else:
            break
        
    i=vankri_pos[0]-9
    while i >= -8:			#Vasakule käigud
        if seis[i][veerg] in vastased:
            käigud.append([i+8,veerg])
            break
        elif seis[i][veerg] == ' ':
            käigud.append([i+8,veerg])
        else:
            break 
        i-=1
    for j in range(veerg+1,8):	#alla käigud
        if seis[rida][j] in vastased:
            käigud.append([rida,j])
            break
        elif seis[rida][j] == ' ':
            käigud.append([rida,j])
        else:
            break
    j=vankri_pos[1]-9
    while j >= -8:		#üles käigud
        if seis[rida][j] in vastased:
            käigud.append([rida,j+8])
            break
        elif seis[rida][j] == ' ':
            käigud.append([rida,j+8])
        else:
            break
        j-=1
    return käigud
'''def kuninga_käigud(seis,kuninga_pos):
    värv=värv(kuninga_pos)'''
def oda_käigud(seis,oda_pos):
    pool=värv(oda_pos)
    käigud=[]
    vastased=vaenlased(pool)
    for i in range(4):
        võimalik= True
        kordaja=1
        if i ==0:		#Siin on iga if-iga toodud oda võimalik liikumissuund
            x=1
            y=1
        elif i==1:
            x=1
            y=-1
        elif i==2:
            x=-1
            y=1
        else:
            x=-1
            y=-1
        while võimalik:
            x_koord=oda_pos[0]+kordaja*x	#Niikaua, kui on võimalik liigume ühes suunas
            y_koord=oda_pos[1]+kordaja*y	#Kui enam pole võimalik võtame uue suuna kontrollimiseks
            if x_koord < 0 or y_koord < 0 or x_koord >7 or y_koord >7:
                võimalik =False		#Vaatab, kas koordinaadid jäävad laua suuruse sisse
            elif seis[x_koord][y_koord] == ' ' or seis[x_koord][y_koord] in vastased:
                käigud.append([x_koord,y_koord])
                if seis[x_koord][y_koord] in vastased:
                    võimalik = False	#Vastaseni jõudes väljume tsüklist, aga käigu paneme enne kirja
                kordaja+=1
            else:
                võimalik=False
    return käigud
def lipu_käigud(seis,lipu_pos):
    käigud=[]		#lipu käigud koosnevad oda ja vankri käikudest, seega saab eelnevaid fun kasutada
    käigud.append(oda_käigud(seis,lipu_pos))
    käigud.append(vankri_käigud(seis,lipu_pos))
    return käigud
def etturi_käigud(seis,etturi_pos):
    pool=värv(etturi_pos)
    vastased=vaenlased(pool)
    käigud=[]
    käik= []
    x=etturi_pos[0]
    y=etturi_pos[1]
    if pool == 'V':
        i=-1
        if etturi_pos[0]==6:		#vaatab, kas ettur on algpositsioonil ja lisab topelt käigu võimaluse
            käik=[4,y]
    else:
        i=1
        if etturi_pos[0]==1:
            käik=[3,y]
    if seis[x+1][y]==' ':		#Kas on võimalik edasi liikuda
        käigud.append([x+i,y])
        if käik!=[] and seis[käik[0]][käik[1]]:	#kontrollib, kas topeltkäik on võimalik
            käigud.append(käik)
    if seis[x+i][y+1] in vastased and y+1 <=7: 		#Kas on võimalik võtta diagonaalis
        käigud.append([x+i,y+1])
    if seis[x+i][y-1] in vastased and y-1 >=0:
        käigud.append([x+i,y-1])
    return käigud #Veel on vaja enpassanti ja castle-imist + käikude eemaldamist, mis avaksid tule kuningale
def üks_ratsu(seis,ratsu_pos): #kaks võtab koordinaadi, mille suhtes liigutakse 2 ruutu
    pool=värv(ratsu_pos)
    x=ratsu_pos[0]
    y=ratsu_pos[1]
    x_koord=x
    y_koord=y
    oma=omad(pool)
    suund=2
    käik=[]
    for i in range(2):
        if i==1:
            suund=-2
        if x_koord+suund<8 and x_koord+suund >=0:
            if y_koord+1<8 and seis[x_koord+suund][y_koord+1] not in oma:
                käik.append([x_koord+suund,y_koord+1])
            if y_koord-1>=0 and seis[x_koord+suund][y_koord-1] not in oma:
                käik.append([x_koord+suund,y_koord-1])
        if y_koord+suund<8 and y_koord+suund >=0:
            if x_koord+1<8 and seis[x_koord+1][y_koord+suund] not in oma:
                käik.append([x_koord+1,y_koord+suund])
            if x_koord-1<8 and seis[x_koord-1][y_koord+suund] not in oma:
                käik.append([x_koord-1,y_koord+suund])
    return käik
            
        
def ratsu_käigud(seis,ratsu_pos):
    käigud=[]

    for i in range(4):
        if i == 0:
            if x_koord+2 <=7:
                a='sd'
                
        
print(üks_ratsu(algseis,[2,3]))   