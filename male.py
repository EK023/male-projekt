import pygame

pygame.init()


    
            

#ettur(pawn),vanker(rook),ratsu(horse),oda(bishop),kuningas,lipp(queen)//
algseis= [['v','r','o','l','k','o','r','v'],
          ['','e','e','e','e','e','e','e'],		#väikse tähega on mustad ja esitähega on eristatavad nupud
          ['','','','','','','',''],
          ['','','','','','','',''],
          ['','','','','','','',''],
          ['','','','','','','',''],
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
'''def rea_kontroll(seis,vankri_pos,värv, kumb, märk):	#kumb võtab sisendiks kas 'Veerg' või 'Rida' 
    rida=vankri_pos[0]
    veerg=vankri_pos[1]
    võimalused=[]
    for i in range(rida+1,8):
        if seis[i][veerg] in vaenlased(värv):
            võimalused.append([i,veerg])
            return võimalused
        if seis[i][veerg] in omad(värv):
            return võimalused
        if seis[i][veerg] == '':
            võimalused.append([i,veerg])'''		#seda ära pane tähele :D
vankri_käigud(seis,vankri_pos,värv) 		#värvi on tegelikult võimalik leida ka nupu positsioonist(kas ta on väike või suur täht)
    rida=vankri_pos[0]
    veerg=vankri_pos[1]
    käigud=[]
    for i in range(rida+1,8):
        if seis[i][veerg] in vaenlased(värv):
            käigud.append([i,veerg])
            break
        if seis[i][veerg] in omad(värv):
            break
        if seis[i][veerg] == '':
            käigud.append([i,veerg])
    for j in range(veerg+1,8):
        if seis[rida][j] in vaenlased(värv):
            käigud.append([rida,j])
            break
        if seis[rida][j] in omad(värv):
            break
        if seis[rida][j] == '':
            käigud.append([rida,j])
    return käigud							#Hetkel peaks siia kaks samasugust for tsüklit veel tulema,
print(vankri_käigud(algseis,[0,0],'must'))	#millega leiame ka ülesse ja vaskule jäävad võimalikud käigud

        