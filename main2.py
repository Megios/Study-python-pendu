#!/usr/bin/env python3
from datetime import datetime

def newProduit():
  produit = str(input('Entre le nom du nouveau produit : '))
  prix = float(input('Et son prix :'))
  message1='Ok, donc %s est le nouveau produit et son prix est %s€ HT' % (produit, prix)
  print(message1)
  return [produit,prix]

def prixWithTax(prix):
  prixTTC= prix*1.20
  print('A oui et avec les taxe ça donne %s€ TTC' % (prixTTC))
  return prixTTC

print('Bonjour')
beforeChoice = 'Que voulez vous faire:\n'
possibilite= '1: Ajoutez un produit \n2: Juste afficher les produits déja existant \n'
choix = 1
while choix == 1 :
  produit= newProduit()
  prixTTC= prixWithTax(produit[1])
  choix = int(input(beforeChoice + possibilite))
  print('le choix actuel est : %d' % (choix))
  if choix ==2 :
    break
now = datetime.now()
currentTime = now.strftime("%d/%m/%Y à %H:%M")
print(now)
print(currentTime)


  




