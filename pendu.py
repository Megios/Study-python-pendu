#!/usr/bin/env python3
import random
def display_hangman(num_tries):
  print(" ____")
  print("|    |")
  print("|    %s" % ("O" if num_tries >= 1 else " "))
  print("|   %s%s%s" % ("/" if num_tries >= 3 else " ", "|" if num_tries >= 2 else " ", "\\" if num_tries >= 4 else " "))
  print("|   %s %s" % ("/" if num_tries >= 5 else " ", "\\" if num_tries >= 6 else " "))

#Paramettrages des différents mots utilisé 
mots =['Foudre','Dauphin', 'Pieds']
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letterFound= []
input("Bonjour, bienvenue dans le jeu du pendu, appuyez sur entrez pour lancer une partie")

#Tirage aléatoire du mot de la party
def newParty():
  num_tries = 0
  return mots[random.randint(0,len(mots)-1)]

#Fonction de saisie d'une lettre
def tried() :
  valide = False
  while valide == False:
    choix = input("Entrez une lettre: ")
    choix= choix.lower()
    if choix in alphabet and not choix in letterFound :
      valide = True
      return choix
    else :
      print('lettre non valide ou déja utilisé \n')

#function d'affichage du mots celon les tirages deja effectué
def motATrouver(letterFound,mot,win):
  affiche =''
  i=0
  win=True
  while i<len(mot) :
    if mot.lower()[i] in letterFound :
      affiche += '%s' % (mot[i])
      i+=1
    else :
      affiche += '_'
      i+=1
      win=False
  return affiche,win

#function du déroulement de la party 

def party(mots) :
  letterFound= []
  num_tries=0
  mot = newParty()
  win = False
  tent = motATrouver(letterFound,mot,win)
  print('Mot à trouver : ' + tent[0])
  while num_tries<6 and win == False :
    choix = tried()
    if choix in mot.lower() :
      letterFound.append(choix)
    else :
      num_tries += 1
      display_hangman(num_tries)
    tent = motATrouver(letterFound,mot,win)
    win=tent[1]
    print('Mot à trouver : ' + tent[0])

  if num_tries==6 :
    print("Perdu, le mot était %s! " % (mot))
  else :
    print("Bravo tu as trouver le bon mot, avec %d erreur !" %(num_tries))
  mots.remove(mot)

#Menu principal 
game=True
while game == True :
  if len(mots) < 1 :
    print('Nous sommes désolé nous n\'avons plus de mots en stock')
    break
  party(mots)
  valid=False
  while valid ==False :
    ask = input('Veux-tu rejouer?[Y / N]')
    if ask == 'N' or ask =='n' :
      valid = True
      game = False
    elif ask =='Y' or ask == 'y' :
      valid = True
print('Merci d\'avoir jouer')


