from random import seed
import random
print ("Diz-me um tamanho para a tua árvore!")
tamanho = int(input())
print ("Deixa-me ir buscar a árvore de natal para ti! :D")
#Nº de espaços
k = tamanho - 1

#Nº de colunas
for i in range(0, tamanho):

   # loop interno para lidar com espaços numéricos
    for j in range(0, k):

      print(" ",end="")

    k = k - 1

     # loop interno para lidar com o número de colunas
    for j in range(0, i+1): 
       R = random.randint(0,10)
       if i==0:
         print("★ ", end="")
       elif R==2:
         print("º ", end="")
       elif R==3:
         print("+ ", end="")
       else:
         print("* ", end="")

          # linha final após cada linha
    print("\r")

for i in range (0, 2):
     for j in range(0, tamanho -4):

      print(" ",end="")
     print ("███")