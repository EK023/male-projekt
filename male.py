import pygame

pygame.init()
WIDTH = 900
HEIGHT = 850
screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.RESIZABLE ) #ekraani loomine, loodetavasti saab ekraani suuruse muutmise tööle
pygame.display.set_caption("Kahe mängijaga male!")
kell = pygame.time.Clock()
fps = 60

    
            
#Castle-imise ja en passanti jaoks oleks vist vaja käike meeles pidada
#ettur(pawn),vanker(rook),ratsu(horse),oda(bishop),kuningas,lipp(queen)//
algseis= [['v','r','o','l','k','o','r','v'],
          ['e','E','e','e','e','e','e','e'],		#väikse tähega on mustad ja esitähega on eristatavad nupud
          [' ','L',' ','R',' ',' ',' ','L'],
          [' ',' ','V',' ','L',' ',' ',' '],
          [' ',' ',' ','K','e',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' '],
          ['E','E','E','E','E','E','E','E'],		#suure tähega valged
          ['V','R','O','L','K','O','R','V']]
valged=['V','R','O','L','K','E']
mustad=['v','r','o','l','k','e']
def värv(seis,nupu_pos):		#Leiab, mis värvi nupuga tegemist on, vastavalt, kas tegemist on suure või väikse tähega
    if seis[nupu_pos[0]][nupu_pos[1]].islower():
        pool='M'
    else:
        pool='V'
    return pool
def vaenlased(pool):		#tagastab järjendi, kus on kõik võimalikud vaenlased
    if pool == 'V':
        return mustad
    else:
        return valged
def omad(pool):
    if pool == 'V':
        return valged
    else:
        return mustad


käigu_järk = 0 #0 - valge käik; 1 - valge käik, nupp valitud; 2 - musta käik; 3 - musta käik, nupp valitud
valik = 100  #default, käigu ajal võtab nupu väärtuse
sobivad_käigud = []


must_lipp = pygame.image.load('Pildid\must_lipp.png')
must_lipp = pygame.transform.scale(must_lipp, (80,80))
must_lipp_v = pygame.transform.scale(must_lipp, (25,25))
must_kuningas = pygame.image.load('Pildid\must_kuningas.png')
must_kuningas = pygame.transform.scale(must_kuningas, (80, 80))
must_kuningas_v = pygame.transform.scale(must_kuningas, (25, 25))
must_oda = pygame.image.load('Pildid\must_oda.png')
must_oda = pygame.transform.scale(must_oda, (80,80))
must_oda_v = pygame.transform.scale(must_oda, (25, 25))
must_ratsu = pygame.image.load('Pildid\must_ratsu.png')
must_ratsu = pygame.transform.scale(must_ratsu, (80,80))
must_ratsu_v = pygame.transform.scale(must_ratsu, (25, 25))
must_vanker = pygame.image.load('Pildid\must_vanker.png')
must_vanker = pygame.transform.scale(must_vanker, (80,80))
must_vanker_v = pygame.transform.scale(must_vanker, (25, 25))
must_ettur = pygame.image.load('Pildid\must_ettur.png')
must_ettur = pygame.transform.scale(must_ettur, (80,80))
must_ettur_v = pygame.transform.scale(must_ettur, (25, 25))

valge_lipp = pygame.image.load('Pildid\\valge_lipp.png')
valge_lipp = pygame.transform.scale(valge_lipp, (80,80))
valge_lipp_v = pygame.transform.scale(valge_lipp, (25, 25))
valge_kuningas = pygame.image.load('Pildid\\valge_kuningas.png')
valge_kuningas = pygame.transform.scale(valge_kuningas, (80,80))
valge_kuningas_v = pygame.transform.scale(valge_kuningas, (25, 25))
valge_oda = pygame.image.load('Pildid\\valge_oda.png')
valge_oda = pygame.transform.scale(valge_oda, (80,80))
valge_oda_v = pygame.transform.scale(valge_oda, (25, 25))
valge_ratsu = pygame.image.load('Pildid\\valge_ratsu.png')
valge_ratsu = pygame.transform.scale(valge_ratsu, (80,80))
valge_ratsu_v = pygame.transform.scale(valge_ratsu, (25, 25))
valge_vanker = pygame.image.load('Pildid\\valge_vanker.png')
valge_vanker = pygame.transform.scale(valge_vanker, (80,80))
valge_vanker_v = pygame.transform.scale(valge_vanker, (25, 25))
valge_ettur = pygame.image.load('Pildid\\valge_ettur.png')
valge_ettur = pygame.transform.scale(valge_ettur, (80,80))
valge_ettur_v = pygame.transform.scale(valge_ettur, (25, 25))
valged_pildid = [valge_vanker, valge_ratsu, valge_oda, valge_lipp, valge_kuningas, valge_ettur]
väiksed_valged_pildid = [valge_vanker_v, valge_ratsu_v, valge_oda_v, valge_lipp_v, valge_kuningas_v, valge_ettur_v]
mustad_pildid = [must_vanker, must_ratsu, must_oda, must_lipp, must_kuningas, must_ettur]
väiksed_mustad_pildid = [must_vanker_v, must_ratsu_v, must_oda_v, must_lipp_v, must_kuningas_v, must_ettur_v]
malendid = ['vanker', 'ratsu', 'oda', 'lipp', 'kuningas', 'ettur']

# muutujad
#counter = 0 #ei saanud hästi aru, mis see tegema peaks, midagi checkiga seotud
võitja = ''
game_over = False



def malelaud():
    for i in range(32):
        veerg = i % 4
        rida = i // 4
        if rida % 2 == 0:
            pygame.draw.rect(screen, 'chartreuse4', [600 - (veerg*200), rida * 100, 100, 100])
        else:
            pygame.draw.rect(screen, 'chartreuse4', [700 - (veerg*200), rida * 100, 100, 100])
        pygame.draw.rect(screen, 'gray', [0, 800, WIDTH, 50])
        pygame.draw.rect(screen, 'gold', [0, 800, WIDTH, 50], 3)
        pygame.draw.rect(screen, 'gold2', [800, 0, 100, HEIGHT], 3)
        for i in range(9):
            pygame.draw.line(screen, 'black', (0, 100 * i), (800, 100 * i), 2)
            pygame.draw.line(screen, 'black', (100 * i, 0), (100 * i, 800), 2)


def vankri_käigud(seis,vankri_pos): 		#värvi on tegelikult võimalik leida ka nupu positsioonist(kas ta on väike või suur täht)
    pool=värv(seis,vankri_pos)
    vastased = vaenlased(pool)
    rida, veerg=vankri_pos[0], vankri_pos[1]
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
def oda_käigud(seis,oda_pos):
    pool=värv(seis,oda_pos)
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
    pool=värv(seis,etturi_pos)
    vastased=vaenlased(pool)
    käigud=[]
    käik= []
    x, y=etturi_pos[0], etturi_pos[1]
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
    if seis[x+i][y+1] in vastased and y+1 <=7: 		#Kas on võimalik võtta diagonaalis võtta
        käigud.append([x+i,y+1])
    if seis[x+i][y-1] in vastased and y-1 >=0:
        käigud.append([x+i,y-1])
    return käigud #Veel on vaja enpassanti ja castle-imist + käikude eemaldamist, mis avaksid tule kuningale
def ratsu_käigud(seis,ratsu_pos): #kaks võtab koordinaadi, mille suhtes liigutakse 2 ruutu
    pool=värv(seis,ratsu_pos)
    x_koord, y_koord=ratsu_pos[0], ratsu_pos[1]
    oma=omad(pool)
    suund=2
    käik=[]
    for i in range(2):
        if i==1:		#alguses otsib käigud, mis jäävad alla ja paremale
            suund=-2	#Siin otsib ülejäänud suunda jäävad käigud
        if x_koord+suund<8 and x_koord+suund >=0:		#2 käiku x-teljel 
            if y_koord+1<8 and seis[x_koord+suund][y_koord+1] not in oma:
                käik.append([x_koord+suund,y_koord+1])
            if y_koord-1>=0 and seis[x_koord+suund][y_koord-1] not in oma:
                käik.append([x_koord+suund,y_koord-1])
        if y_koord+suund<8 and y_koord+suund >=0:		#2 käiku y-teljel
            if x_koord+1<8 and seis[x_koord+1][y_koord+suund] not in oma:
                käik.append([x_koord+1,y_koord+suund])
            if x_koord-1<8 and seis[x_koord-1][y_koord+suund] not in oma:
                käik.append([x_koord-1,y_koord+suund])
    return käik
def kuninga_käigud(seis,kuninga_pos):
    pool=värv(seis,kuninga_pos)
    oma=omad(pool)
    vastane=vaenlased(pool)
    x , y = kuninga_pos[0], kuninga_pos[1]
    suund =1
    käigud=[]
    for j in range(3):
        if j==1:
            suund = -1
        if j==2:
            suund = 0 
        for i in range(3):
            ysuund=i
            if i== 2:
                ysuund=-1
            if x+suund >=0 and x+suund<8 and y+ysuund >=0 and y+ysuund <8:
                if seis[x+suund][y+ysuund]==' ':
                    käigud.append([x+suund,y+ysuund])
                #if y-1 >=0 and:#siit tuleks jätkata(ülevalt alt 3 käiku V-P vaadata ja siis eraldi Keskel V-P)
    return käigud
                    
                
   
#print(kuninga_käigud(algseis,[4,3]))	
#print(algseis[0][3-8])
#print(oda_käigud(algseis,[3,3]))	



run = True
while run:
    kell.tick(fps)
    screen.fill('light yellow')
    malelaud()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #elif event.type == pygame.VIDEORESIZE:
        #    screen.blit(pygame.transform.scale(malelaud(), event.dict['size']), (0, 0))
        #    pygame.display.update()

    

