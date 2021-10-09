import matplotlib.pyplot as plt  
import numpy as np
from random import *

def FACT(n):
 nombre = n - 1
 t, s = 0, 0
 while(nombre%2 == 0):
  s += 1
  nombre = int(nombre/2)
 t = nombre
 return(int(t),s)
def Alea(n):
 return(randrange(1,n-1))
 
def RAB(n,a):

 #nombre a est témoin de miller si a^t 
 # if (n%2 != 0) and (a < n) and (a > 0):
  t,r = FACT(n)
 
  xv = (a ** t)%n
  v = 0
  x = xv
  if x == 1 or x == n-1 :
   return 0
  while r>1 :
   x = (x**2)%n
   if x == 1:
    v = v+1 
   if x == n-1:
    return 0
   r -= 1
  if v != 0:
   # print(a,'y')
   return a
   
  # print('g')
  # print(a,'y')
  return a

def Miller_Rabin(n,k):
 if n%2 == 0:
  # print("le nombre doit etre impaire")
  return
 negatif = 0
 # global liste_Temoin 
 # liste_Temoin = []
 for i in range(k):
  number = Alea(n)
  # print(number)
  if RAB(n,number) == number:
   negatif += 1
   # liste_Temoin.append(number)
 if negatif != 0:
  print("Le nombre : ",n," est compose")
  return  1
 else:
  print("Le nombre : ",n," est premier")
  return 0

def graphe_Miller_Rabin():
 negatif = 0
 global liste_Temoin 
 # liste_Temoin = []
 global liste_Pourcentage 
 
 cpt = 0
 for j in range(3,1002):
  # print(j)
  if j%2 != 0:
   d = Miller_Rabin(j,50) 
   if d == 1:
    for i in range(2,j):
      cpt += 1
      if RAB(j,i) == i:
       negatif += 1
     
    if negatif != 0:
      liste_Temoin.append(j)
      liste_Pourcentage.append((negatif * 100) / cpt)
      cpt= 0
      negatif = 0
      
 plt.plot((liste_Temoin),liste_Pourcentage, marker="*")
 plt.show()

liste_Pourcentage = []
liste_Temoin = []

print("\n *******************************************************")


try :
 print("\nDonner le nombre a tester sa primalite")
 var = int(input())
 
 print("\nDonner la valeur de k  pour tester")
 nm_test = int(input())
 
 Miller_Rabin(var,nm_test)
 
 print("\ntappez 'O' si vous voulez afficher le graphe 'N' sinon")
 reponse = input()
 if reponse == 'O' or reponse =='o':
  graphe_Miller_Rabin()
 # graphe()
 else:
  print("goog bye")
except :
 print("\nvous devez donner des nombres entiers")

print("\nTest des entiers de Fermat  \ndonner la valeur de k (supieur ou egale a 2)\n")

try :
 k = int(input())
 if k >= 2:
  print("\nPour les entiers de Fermat")
  for i in range(1,k):
   Miller_Rabin((2**(2**i))+1,k)
  print("\nPour les entiers de Mersenne")

  for i in range(2,k):
   Miller_Rabin((2**i)-1,k)
 else:
  print("le k doit etre superieur ou egal a 2")
except:
 print("\nvous devez donner des nombres entiers")