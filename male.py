import pygame

pygame.init()
WIDTH = 900
HEIGHT = 850
screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.RESIZABLE ) #ekraani loomine, loodetavasti saab ekraani suuruse muutmise tööle
pygame.display.set_caption("Kahe mängijaga male!")
kell = pygame.time.Clock()
fps = 60

    
            

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
def vaenlased(värv):
    if värv == 'V':
        return mustad
    else:
        return valged
def omad(värv):
    if värv == 'V':
        return valged
    else:
        return mustad
def värv(nupu_pos):
    if algseis[nupu_pos[0]][nupu_pos[1]].islower:
        värv='M'
    else:
        värv='V'
    return värv

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


'''rea_kontroll(kumb):	#kumb võtab sisendiks kas 'Veerg' või 'Rida' 
    while i < 8:
    while i >=-8:
        if seis[i+9][veerg] in vaenlased(värv):
            käigud.append([i,veerg])
            break
        if seis[i+9][veerg] in omad(värv):
            break
        if seis[i+9][veerg] == '':
            käigud.append([i,veerg])
        i-=1'''
def vankri_käigud(seis,vankri_pos): 		#värvi on tegelikult võimalik leida ka nupu positsioonist(kas ta on väike või suur täht)
    värv=värv(vankri_pos)
    rida=vankri_pos[0]
    veerg=vankri_pos[1]
    käigud=[]
    for i in range(rida+1,8):
        if seis[i][veerg] in vaenlased(värv):
            käigud.append([i,veerg])
            break
        if seis[i][veerg] in omad(värv):
            break
        if seis[i][veerg] == ' ':
            käigud.append([i,veerg])
    i=vankri_pos[0]-9
    while i >= -8:
        if seis[i][veerg] in vaenlased(värv):
            käigud.append([i+8,veerg])
            break
        if seis[i][veerg] in omad(värv):
            break
        if seis[i][veerg] == ' ':
            käigud.append([i+8,veerg])
        i-=1
    for j in range(veerg+1,8):
        if seis[rida][j] in vaenlased(värv):
            käigud.append([rida,j])
            break
        if seis[rida][j] in omad(värv):
            break
        if seis[rida][j] == ' ':
            käigud.append([rida,j])
    j=vankri_pos[1]-9
    while j >= -8:
        if seis[rida][j] in vaenlased(värv):
            käigud.append([rida,j+8])
            break
        if seis[rida][j] in omad(värv):
            break
        if seis[rida][j] == ' ':
            käigud.append([rida,j+8])
        j-=1
    return käigud
def kuninga_käigud(seis,kuninga_pos):
    värv=värv(kuninga_pos)
def oda_käigud(seis,oda_pos):
    pool=värv(oda_pos)
    käigud=[]
    vastased=vaenlased(värv)
    for i in range(4):
        võimalik= True
        kordaja=1
        if i ==0:
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
            x_koord=oda_pos[0]+kordaja*x
            y_koord=oda_pos[1]+kordaja*y
            if x_koord < 0 or y_koord < 0 or x_koord >7 or y_koord >7:
                võimalik =False
            elif seis[x_koord][y_koord] == ' ' or seis[x_koord][y_koord] in vaenlased(pool):
                käigud.append([x_koord,y_koord])
                if seis[x_koord][y_koord] in vastased:
                    võimalik = False
                kordaja+=1
            else:
                võimalik=False
    return käigud
print(oda_käigud(algseis,[3,3]))	
#print(algseis[0][3-8])

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

    