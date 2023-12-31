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
          [' ',' ',' ',' ',' ',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' '],
          ['E','E','E','E','E','E','E','E'],		#suure tähega valged
          ['V','R','O','L','K','O','R','V']]
valged=['V','R','O','L','K','E']
mustad=['v','r','o','l','k','e']
läinud=[]


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
    if kas_tuli:
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
    v_suurus = (30*k, 30*k)
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
    pygame.draw.rect(screen, 'gray', [600*k, 575*k, 150*k, 75*k])
    pygame.draw.rect(screen, 'gold', [0, 0, 600*k, 50*k], 3)
    pygame.draw.rect(screen, 'gold2', [600*k, 0, 150*k, HEIGHT*k], 3)
    pygame.draw.rect(screen, 'gold', [600*k, 575*k, 150*k, 75*k], 3)
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
    screen.blit(kesk_font.render('Forfeit', True, 'black'), (640*k, 600*k))

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

def võetud_nupud(li):
    k = vähim_kordaja()
    valge = 0
    must = 0
    for el in li:
        if el in valged:
            i = valged.index(el)
            screen.blit(väiksed_valged_pildid[i], (625*k, (5 + 35*valge)*k))
            valge += 1
        if el in mustad:
            i = mustad.index(el)
            screen.blit(väiksed_mustad_pildid[i], (675*k, (5 + 35*must)*k))
            must += 1

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
def kuninga_käigud(seis,kuninga_pos,vasak,parem,kuningas):
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
    if kuningas and parem and seis[x][y+2] ==' 'and seis[x][y+1]==' ':
        käigud.append([x,y+2])
    if kuningas and vasak and seis[x][y-2] ==' 'and seis[x][y-1]==' ' and seis[x][y-3]==' ':
        käigud.append([x,y-2])
    return käigud

parem_V,vasak_V,kuningas_V,parem_m,vasak_m, kuningas_m=True,True,True,True,True,True #Vangerduse jaoks vajalikud
def nupu_käigud(seis, nupu_pos,parem_V,vasak_V,kuningas_V,parem_m,vasak_m, kuningas_m):
    x,y =nupu_pos
    käigud=[]
    if seis[x][y].lower()== 'k':
        pool=värv(seis,nupu_pos)
        if pool=='V':
            vasak,parem,kuningas = parem_V,vasak_V,kuningas_V
        else:
            vasak,parem,kuningas = parem_m,vasak_m, kuningas_m   
        käigud=kuninga_käigud(seis, nupu_pos,vasak,parem,kuningas)
        käigud=(käigud,' jljk') # Teiste nuppude puhul on lisaks tule asi      
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

#def võimalikud_käigud()

def lõpukast():
    k = vähim_kordaja()
    pygame.draw.rect(screen, 'black', [110*k, 150*k, 400*k, 100*k])
    screen.blit(suur_font.render(f'{võitja} võitis!', True, 'white'), (225*k, 170*k))
    screen.blit(kesk_font.render(f'Uue mängu jaoks vajuta enterit!', True, 'white'), (160*k, 200*k))
    
ootus = 0
nupp_valitud = 0
run = True
while run:
    kell.tick(fps)
    screen.fill('light yellow')
    malelaud()
    malendidlaual()
    võetud_nupud(läinud)
    if nupp_valitud != 1:
        pygame.display.flip() 
    muudetav_suurus=75*vähim_kordaja()			#muudetav suurus oleks ühe malelaua ruudu suurus
    ülemise_kasti_suurus=50*vähim_kordaja()

    if võitja!='':
        game_over= True
        lõpukast()
        pygame.display.update()
        wait = True
        while wait:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    wait = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        wait = False
        game_over = False
        võitja = ''
        käigu_järk = 0
        läinud = []
        algseis=	[['v','r','o','l','k','o','r','v'],
                    ['e','e','e','e','e','e','e','e'],
                    [' ',' ',' ',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ',' ',' ',' '],
                    ['E','E','E','E','E','E','E','E'],
                    ['V','R','O','L','K','O','R','V']]
        malelaud()
        malendidlaual()
        pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x = int((event.pos[1]- ülemise_kasti_suurus) // muudetav_suurus) #kuna üleval on tekstikast, siis see suurus on vaja maha lahutada
            y = int(event.pos[0] // muudetav_suurus) 		# leiab x ja y koordinaadi
            if x>6 and y>7:                         # forfeit nupp
                if käigu_järk == 0:
                    võitja = 'Must'
                if käigu_järk == 1:
                    võitja = 'Valge'
            if x<8 and y< 8:
                
                if nupp_valitud==1 and [x,y] in käigud[0]:
                    nupp= algseis[nupu_x][nupu_y]
                    võetud_nupp = algseis[x][y]
                    läinud.append(võetud_nupp)
                    
                    #Vankri ära võtmisel vangerduse kaotamine
                    if võetud_nupp.lower() == 'v':
                        if x==0:
                            if y==0:
                                parem_m=False
                            else:
                                vasak_m=False 
                        else:
                            if y==0:
                                parem_V=False
                            else:
                                vasak_V=False #Bugfix:  Enne ei olnud me arvestanud sellega, et vanker võidakse enne ära võtta, kui
                                              #kuningas liigub, mistõttu ei kadunud vangerdusvõimalus ära vankriga, mida ei olnud enam laual(veel oli omale võimalik tasuta vanker teha)
                                              #Millegi pärast ei ole päris töökindel veel
                    if nupp== 'e' and x==7:         #etturi automaatne muutmine lipuks
                        nupp='l'
                    if nupp=='E' and x==0:
                        nupp='L'
                    if nupu_y-y==2 and nupp.lower()=='k':		#Vangerdus vasakule
                        if nupp=='K':
                            algseis[x][y+1]='V'
                            algseis[x][0]=' '
                        else:
                            algseis[x][y+1]='v'
                            algseis[x][0]=' '
                    if y-nupu_y==2 and nupp.lower()=='k': #Vangerdus paremale
                        if nupp=='K':
                            algseis[x][y-1]='V'
                            algseis[x][7]=' '
                        else:
                            algseis[x][y-1]='v'
                            algseis[x][7]=' '
                    algseis[nupu_x][nupu_y]= ' '
                    algseis[x][y]= nupp
                    if nupp.lower()=='k':		#võtab vangerduse võimaluse ära, kui liigutakse kuningat
                        if nupp=='K':
                            kuningas_V=False
                        else:
                            kuningas_m=False
                    if nupp.lower()=='v': #Kaotab vangerdusvõimaluse ühele poole ära, kui vankrit on liigutatud
                        if nupp=='V':
                            if y==0:
                                vasak_V=False
                            elif y==7:
                                parem_V=False
                        elif nupp=='v':
                            if y==0:
                                vasak_m=False
                            elif y==7:
                                parem_m=False
                    nupp_valitud = 0                     #et ei kuvaks topelt
                    if võetud_nupp.lower() == 'k':	#Mängu lõppemine, kui kuningas ära võetakse
                        if käigu_järk == 0:
                            võitja = 'Valge'
                        if käigu_järk == 1:
                            võitja = 'Must'
                    if game_over == False:
                        if käigu_järk == 0:
                            käigu_järk = 1
                        else:
                            käigu_järk = 0
                else:
                    nupu_x= x
                    nupu_y= y
                    nupp= algseis[nupu_x][nupu_y]
                    if nupp_valitud==1 and ((nupp in valged and käigu_järk == 1) or (nupp in mustad and käigu_järk == 0) or nupp == ' '):
                        nupp_valitud=0
                        pygame.display.flip()
                        break  #Bugfix: Ennem oli võimalik käia vastase nupp oma nupu võimalike käikude ruudule valides alguses oma nupu 
                               #ning enne käimist vajutades vastase nupu peale ning siis käiku tehes ilmus sinna kohale vastase nupp
                               #Lisaks kaovad nüüd nupu käigud ära kui vajutad kuhugile mujale
                    
                    if (nupp in mustad and käigu_järk == 1) or (nupp in valged and käigu_järk == 0):            #Käigud vahelduksid
                        käigud=nupu_käigud(algseis,[x,y],parem_V,vasak_V,kuningas_V,parem_m,vasak_m, kuningas_m)
                        for el in käigud[0]:
                            y_koord, x_koord= el
                            ring=pygame.image.load('Pildid\\ring.png')
                            ring = pygame.transform.scale(ring, (40*vähim_kordaja(),40*vähim_kordaja()))
                            if x_koord<8 and y_koord<8 and x_koord>=0 and y_koord>=0:
                                screen.blit(ring,(((20+ x_koord * 75)*vähim_kordaja()), ((70 + y_koord * 75)*vähim_kordaja())))
                                pygame.display.update()
                                nupp_valitud = 1                 #et käikude võimalused jääksid kuvama
        elif event.type == pygame.VIDEORESIZE:
            muuda_suurust()

pygame.quit()