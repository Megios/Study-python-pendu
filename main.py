#!/usr/bin/env python3

n= int(input('Entrez un nombre, et sa factorielle vous sera affichée : '))

if n < 0:
  raise ValueError('veuillez entrez un nombre positif')

fact = 1 
i = 2
while i <= n:
  fact *= i
  i += 1
print(fact)