import pygame

pygame.init()
WIDTH = 750
HEIGHT = 650
screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.RESIZABLE) #ekraani loomine
pygame.display.set_caption("Kahe mängijaga male!")
kell = pygame.time.Clock()
fps = 60
suur_font = pygame.font.Font(pygame.font.get_default_font(), 25)
kesk_font = pygame.font.Font(pygame.font.get_default_font(), 20)
    
            
#Castle-imise ja en passanti jaoks oleks vist vaja käike meeles pidada
#ettur(pawn),vanker(rook),ratsu(horse),oda(bishop),kuningas,lipp(queen)//
algseis= [['v','r','o','l','k','o','r','v'],
          ['e','e','e','e','e','e','e','e'],		#väikse tähega on mustad ja esitähega on eristatavad nupud
          [' ',' ',' ',' ','L',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ','k',' '],
          [' ',' ',' ',' ',' ',' ',' ',' '],
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
def tule_kontroll(nupp,kas_tuli):
    if nupp.lower()=='k' or kas_tuli:
        return True
    else:
        return False

käigu_järk = 0 #0 - valge käik; 1 - musta käik

def vähim_kordaja():  #akna suuruse muutmise kordaja
    suurus = pygame.display.get_window_size()
    kordaja_x = suurus[0]/WIDTH
    kordaja_y = suurus[1]/HEIGHT
    return min(kordaja_x, kordaja_y)

def pildi_laadimine(pilt, k):  #k - kordaja, võimaldab muuta piltide suurust koos aknaga, tagastab nii väikse kui suure pildi
    suurus=(60*k,60*k)	#siit on võimalik seda suurust muuta, võib ka täitsa algusesse tõsta
    v_suurus = (25*k, 25*k)
    l_pilt = pygame.image.load(pilt)  # load
    s_pilt = pygame.transform.scale(l_pilt, suurus)  #suur
    v_pilt = pygame.transform.scale(s_pilt, v_suurus)  #väike
    return s_pilt, v_pilt

def pildid():
    k = vähim_kordaja()
    global must_lipp, must_lipp_v
    must_lipp, must_lipp_v= pildi_laadimine('Pildid\\must_lipp.png', k)

    global must_kuningas, must_kuningas_v
    must_kuningas, must_kuningas_v = pildi_laadimine('Pildid\\must_kuningas.png', k)

    global must_oda, must_oda_v
    must_oda, must_oda_v = pildi_laadimine('Pildid\\must_oda.png', k)

    global must_ratsu, must_ratsu_v
    must_ratsu, must_ratsu_v = pildi_laadimine('Pildid\\must_ratsu.png', k)

    global must_vanker, must_vanker_v
    must_vanker, must_vanker_v = pildi_laadimine('Pildid\\must_vanker.png', k)

    global must_ettur, must_ettur_v
    must_ettur = pygame.image.load('Pildid\\must_ettur.png')
    must_ettur = pygame.transform.scale(must_ettur, (50*k,50*k))
    must_ettur_v = pygame.transform.scale(must_ettur, (25*k, 25*k))

    global valge_lipp, valge_lipp_v
    valge_lipp, valge_lipp_v = pildi_laadimine('Pildid\\valge_lipp.png', k)

    global valge_kuningas, valge_kuningas_v
    valge_kuningas, valge_kuningas_v = pildi_laadimine('Pildid\\valge_kuningas.png', k)

    global valge_oda, valge_oda_v
    valge_oda, valge_oda_v = pildi_laadimine('Pildid\\valge_oda.png', k)

    global valge_ratsu, valge_ratsu_v
    valge_ratsu, valge_ratsu_v = pildi_laadimine('Pildid\\valge_ratsu.png', k)

    global valge_vanker, valge_vanker_v
    valge_vanker, valge_vanker_v = pildi_laadimine('Pildid\\valge_vanker.png', k)

    global valge_ettur, valge_ettur_v
    valge_ettur = pygame.image.load('Pildid\\valge_ettur.png')
    valge_ettur = pygame.transform.scale(valge_ettur, (50*k,50*k))
    valge_ettur_v = pygame.transform.scale(valge_ettur, (25*k, 25*k))

pildid()
valged_pildid = [valge_vanker, valge_ratsu, valge_oda, valge_lipp, valge_kuningas, valge_ettur]
väiksed_valged_pildid = [valge_vanker_v, valge_ratsu_v, valge_oda_v, valge_lipp_v, valge_kuningas_v, valge_ettur_v]
mustad_pildid = [must_vanker, must_ratsu, must_oda, must_lipp, must_kuningas, must_ettur]
väiksed_mustad_pildid = [must_vanker_v, must_ratsu_v, must_oda_v, must_lipp_v, must_kuningas_v, must_ettur_v]
malendid = ['vanker', 'ratsu', 'oda', 'lipp', 'kuningas', 'ettur']

# muutujad
võitja = ''
game_over = False



def malelaud():
    k = vähim_kordaja()
    pygame.draw.rect(screen, 'gray', [0, 0, 600*k, 50*k])
    pygame.draw.rect(screen, 'gray', [600*k, 600*k, 150*k, 50*k])
    pygame.draw.rect(screen, 'gold', [0, 0, 600*k, 50*k], 3)
    pygame.draw.rect(screen, 'gold2', [600*k, 0, 150*k, HEIGHT*k], 3)
    pygame.draw.rect(screen, 'gold', [600*k, 600*k, 150*k, 50*k], 3)
    for i in range(32):
        veerg = i % 4
        rida = i // 4
        if rida % 2 != 0:
            pygame.draw.rect(screen, 'chartreuse4', [(450 - (veerg*150))*k, (rida * 75 + 50)*k, 75*k, 75*k])
        else:
            pygame.draw.rect(screen, 'chartreuse4', [(525 - (veerg*150))*k, (rida * 75 + 50)*k, 75*k, 75*k])
    for i in range(9):
        pygame.draw.line(screen, 'black', (0, (75 * i + 50)*k), (600*k, (75 * i + 50)*k), 2)
        pygame.draw.line(screen, 'black', (75 * i*k, 50*k), (75 * i*k  , 650*k), 2)
    käigu_tekst = ['Valge käik!', 'Musta käik!']
    screen.blit(suur_font.render(käigu_tekst[käigu_järk], True, 'black'), (190*k, 15*k))
    screen.blit(kesk_font.render('Forfeit', True, 'black'), (640*k, 615*k))

def malendidlaual():
    k = vähim_kordaja()
    for y in range(len(algseis)):
        for x in range(len(algseis[y])):
            if algseis[y][x] in valged:
                i = valged.index(algseis[y][x])
                if i == 5:
                    screen.blit(valged_pildid[i], (((15 + x * 75)*k), ((65 + y * 75)*k)))
                else:
                    screen.blit(valged_pildid[i], (((10 + x * 75)*k), ((60 + y * 75)*k)))
            elif algseis[y][x] in mustad:
                i = mustad.index(algseis[y][x])
                if i == 5:
                    screen.blit(mustad_pildid[i], (((15 + x * 75)*k), ((65 + y * 75)*k)))
                else:
                    screen.blit(mustad_pildid[i], (((10 + x * 75)*k), ((60 + y * 75)*k)))

def muuda_suurust():  #resizeimine
    global suur_font, kesk_font
    suur_font = pygame.font.Font(pygame.font.get_default_font(), int(25*vähim_kordaja()))
    kesk_font = pygame.font.Font(pygame.font.get_default_font(), int(20*vähim_kordaja()))
    pildid()
    global valged_pildid, väiksed_valged_pildid, mustad_pildid, väiksed_mustad_pildid
    valged_pildid = [valge_vanker, valge_ratsu, valge_oda, valge_lipp, valge_kuningas, valge_ettur]
    väiksed_valged_pildid = [valge_vanker_v, valge_ratsu_v, valge_oda_v, valge_lipp_v, valge_kuningas_v, valge_ettur_v]
    mustad_pildid = [must_vanker, must_ratsu, must_oda, must_lipp, must_kuningas, must_ettur]
    väiksed_mustad_pildid = [must_vanker_v, must_ratsu_v, must_oda_v, must_lipp_v, must_kuningas_v, must_ettur_v]
    malelaud()
    malendidlaual()
    screen = pygame.display.set_mode((WIDTH*vähim_kordaja(), HEIGHT*vähim_kordaja()),pygame.RESIZABLE)
    pygame.display.update()


def vankri_käigud(seis,vankri_pos): 		
    pool=värv(seis,vankri_pos)
    vastased = vaenlased(pool)
    rida, veerg=vankri_pos[0], vankri_pos[1]
    käigud=[]
    tuli=False
    for i in range(rida+1,8):	#paremale käigud
        if seis[i][veerg] in vastased:
            käigud.append([i,veerg])
            tuli=tule_kontroll(seis[i][veerg],tuli)
            break
        elif seis[i][veerg] == ' ':
            käigud.append([i,veerg])
        else:
            break
        
    i=vankri_pos[0]-9
    while i >= -8:			#Vasakule käigud
        if seis[i][veerg] in vastased:
            käigud.append([i+8,veerg])
            tuli=tule_kontroll(seis[i][veerg],tuli)
            break
        elif seis[i][veerg] == ' ':
            käigud.append([i+8,veerg])
        else:
            break 
        i-=1
    for j in range(veerg+1,8):	#alla käigud
        if seis[rida][j] in vastased:
            käigud.append([rida,j])
            tuli=tule_kontroll(seis[rida][j],tuli)
            break
        elif seis[rida][j] == ' ':
            käigud.append([rida,j])
        else:
            break
    j=vankri_pos[1]-9
    while j >= -8:		#üles käigud
        if seis[rida][j] in vastased:
            käigud.append([rida,j+8])
            tuli=tule_kontroll(seis[rida][j],tuli)
            break
        elif seis[rida][j] == ' ':
            käigud.append([rida,j+8])
        else:
            break
        j-=1
    return käigud, tuli
def oda_käigud(seis,oda_pos):
    pool=värv(seis,oda_pos)
    käigud=[]
    vastased=vaenlased(pool)
    tuli=False
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
                kordaja+=1
                if seis[x_koord][y_koord] in vastased:
                    tuli=tule_kontroll(seis[x_koord][y_koord],tuli)
                    võimalik = False	#Vastaseni jõudes väljume tsüklist, aga käigu paneme enne kirja
            else:
                võimalik=False
            
    return käigud, tuli

def lipu_käigud(seis,lipu_pos):
    käigud=[]		#lipu käigud koosnevad oda ja vankri käikudest, seega saab eelnevaid fun kasutada
    tuli=False
    käik_o, tuli_o=oda_käigud(seis,lipu_pos)
    käik_v, tuli_v=vankri_käigud(seis,lipu_pos)
    käigud=käik_o+käik_v
    if tuli_o or tuli_v:
        tuli=True 
    return käigud, tuli
def etturi_käigud(seis,etturi_pos):
    pool=värv(seis,etturi_pos)
    vastased=vaenlased(pool)
    käigud=[]
    käik= []
    tuli=False 
    x, y=etturi_pos[0], etturi_pos[1]
    if pool == 'V':
        i=-1
        if etturi_pos[0]==6:		#vaatab, kas ettur on algpositsioonil ja lisab topelt käigu võimaluse
            käik=[4,y]
    else:
        i=1
        if etturi_pos[0]==1:
            käik=[3,y]
    if seis[x+i][y]==' ':		#Kas on võimalik edasi liikuda
        käigud.append([x+i,y])
        if käik!=[] and seis[käik[0]][käik[1]] == ' ':	#kontrollib, kas topeltkäik on võimalik
            käigud.append(käik)
    try:
        if seis[x+i][y+1] in vastased and y+1 <=7: 		#Kas on võimalik võtta diagonaalis võtta
            käigud.append([x+i,y+1])
            tuli=tule_kontroll(seis[x+i][y+1],tuli)
    finally: 
        try:
            if seis[x+i][y-1] in vastased and y-1 >=0:
                käigud.append([x+i,y-1])
                tuli=tule_kontroll(seis[x+i][y+1],tuli)
        finally:
            return käigud, tuli #Veel on vaja enpassanti ja castle-imist + käikude eemaldamist, mis avaksid tule kuningale

def ratsu_käigud(seis,ratsu_pos): #kaks võtab koordinaadi, mille suhtes liigutakse 2 ruutu
    pool=värv(seis,ratsu_pos)
    x_koord, y_koord=ratsu_pos[0], ratsu_pos[1]
    oma=omad(pool)
    vastased=vaenlased(pool)
    suund=2
    käik=[]
    tuli=False
    for i in range(2):
        if i==1:		#alguses otsib käigud, mis jäävad alla ja paremale
            suund=-2	#Siin otsib ülejäänud suunda jäävad käigud
        if x_koord+suund<8 and x_koord+suund >=0:		#2 käiku x-teljel
            for k in range(-1,2,2):
                if y_koord+k<8 and seis[x_koord+suund][y_koord+k] not in oma:
                    käik.append([x_koord+suund,y_koord+k])
                    if seis[x_koord+suund][y_koord+k] in vastased:
                        tuli=tule_kontroll(seis[x_koord+suund][y_koord+k],tuli)
        if y_koord+suund<8 and y_koord+suund >=0:		#2 käiku y-teljel
            for j in range(-1,2,2):
                if x_koord+j<8 and seis[x_koord+j][y_koord+suund] not in oma:
                    käik.append([x_koord+j,y_koord+suund])
                    if seis[x_koord+j][y_koord+suund] in vastased:
                        tuli=tule_kontroll(seis[x_koord+j][y_koord+suund],tuli)
    return käik, tuli
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
                if seis[x+suund][y+ysuund] not in oma:
                    käigud.append([x+suund,y+ysuund])
    return käigud

def nupu_käigud(seis, nupu_pos):
    x,y =nupu_pos
    käigud=[]
    if seis[x][y].lower()== 'k':
        käigud=kuninga_käigud(seis, nupu_pos)
        käigud=(käigud,'midagi hästi tarka') # Teiste nuppude puhul on liskas tule asi
    elif seis[x][y].lower()== 'l':
        käigud=lipu_käigud(seis, nupu_pos)
    elif seis[x][y].lower()== 'o':
        käigud=oda_käigud(seis, nupu_pos)
    elif seis[x][y].lower()== 'r':
        käigud=ratsu_käigud(seis, nupu_pos)
    elif seis[x][y].lower()== 'v':
        käigud= vankri_käigud(seis, nupu_pos)
    elif seis[x][y].lower()== 'e':
        käigud=etturi_käigud(seis, nupu_pos)
    elif seis[x][y]==' ':
        käigud=[[],'lasfknlfkadn']
    return käigud

def lõpukast():
    k = vähim_kordaja()
    pygame.draw.rect(screen, 'black', [110*k, 150*k, 400*k, 100*k])
    screen.blit(suur_font.render(f'{võitja} võitis!', True, 'white'), (225*k, 170*k))
    screen.blit(kesk_font.render(f'Uue mängu jaoks vajuta enterit!', True, 'white'), (160*k, 200*k))
   
#print(kuninga_käigud(algseis,[4,3]))	
#print(algseis[0][3-8])
#print(lipu_käigud(algseis,[3,0]))	
#print(nupu_käigud(algseis,[2,3]))
asi = 0

run = True
while run:
    kell.tick(fps)
    screen.fill('light yellow')
    malelaud()
    malendidlaual()
    if asi != 1:
        pygame.display.flip() 
    muudetav_suurus=75*vähim_kordaja()			#muudetav suurus oleks ühe malelaua ruudu suurus
    ülemise_kasti_suurus=50*vähim_kordaja()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x = int((event.pos[1]- ülemise_kasti_suurus) // muudetav_suurus) #kuna üleval on tekstikast, siis see suurus on vaja maha lahutada
            y = int(event.pos[0] // muudetav_suurus) 		# leiab x ja y koordinaadi
            if x<8 and y< 8:
                if asi==1 and [x,y] in käigud[0]:
                    nupp= algseis[nupu_x][nupu_y]
                    if algseis[x][y].lower() == 'k':
                        if käigu_järk == 0:
                            võitja = 'Valge'
                        if käigu_järk == 1:
                            võitja = 'Must'
                    if nupp== 'e' and x==7:         #etturi automaatne muutmine lipuks
                        nupp='l'
                    if nupp=='E' and x==0:
                        nupp='L'
                    algseis[nupu_x][nupu_y]= ' '
                    algseis[x][y]= nupp
                    asi = 0                     #et ei kuvaks topelt
                    if game_over == False:
                        if käigu_järk == 0:
                            käigu_järk = 1
                        else:
                            käigu_järk = 0
                    #if algseis[x][y] != ' ':'''
                else:
                    nupu_x= x
                    nupu_y= y
                    nupp= algseis[nupu_x][nupu_y]
                    if (nupp in mustad and käigu_järk == 1) or (nupp in valged and käigu_järk == 0):            #Käigud vahelduksid
                        käigud=nupu_käigud(algseis,[x,y])
                        for el in käigud[0]:
                            y_koord, x_koord= el
                            ring=pygame.image.load('Pildid\\ring.png')
                            ring = pygame.transform.scale(ring, (40*vähim_kordaja(),40*vähim_kordaja()))
                            if x_koord<8 and y_koord<8 and x_koord>=0 and y_koord>=0:
                                screen.blit(ring,(((20+ x_koord * 75)*vähim_kordaja()), ((70 + y_koord * 75)*vähim_kordaja())))
                                pygame.display.update()
                                asi = 1                 #et käikude võimalused jääksid kuvama
        elif event.type == pygame.VIDEORESIZE:
            muuda_suurust()

    if võitja!='':
        game_over= True
        lõpukast()
        pygame.display.flip()
    
pygame.quit()

    

