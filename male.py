import pygame

pygame.init()


    
            

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
def vankri_käigud(seis,vankri_pos,värv): 		#värvi on tegelikult võimalik leida ka nupu positsioonist(kas ta on väike või suur täht)
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
    if kuninga_pos.islower:
        värv='M'
    else:
        värv='V'
    
print(vankri_käigud(algseis,[4,6],'M'))	
#print(algseis[0][3-8])
        