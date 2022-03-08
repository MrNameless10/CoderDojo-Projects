import random

def constroi_arvore(tamanho):
  
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
          print("# ", end="")

        # linha final após cada linha
        print("\r")


def constroi_arvore2(tamanho):
  
    k = tamanho - 1
  
    for i in range(0, tamanho):
      
        for j in range(0, k):
        
          print(" ",end="")

        k = k - 1

        # loop interno para lidar com o número de colunas
        for j in range(0, i+1):
          
          print("# ", end="")
        # linha final após cada linha
        print("\r")
      
    for i in range(0, 2):
      
        for j in range(0, k):
        
          print(" ",end="")

        k = k - 1
      
        for j in range(0, tamanho-2):
          print(" ", end="")
          
        print("███")



def constroi_arvore3(tamanho):
  
    k = tamanho - 1
  
    for i in range(0, tamanho):
      
        for j in range(0, k):
        
          print(" ",end="")

        k = k - 1
      
        for j in range(0, i+1):
          r = random.randint(0, 10)
          if i == 0:
            print("★ ", end="")
            continue
          if r==1:
            print("* ", end="")
          else:
            print("# ", end="")
    
        print("\r")
      
    for i in range(0, 2):
      
        for j in range(0, k):
        
          print(" ",end="")

        k = k - 1
      
        for j in range(0, tamanho-2):
          print(" ", end="")
          
        print("███")





tamanho = 13
constroi_arvore(tamanho)
print ()
constroi_arvore2(tamanho)
print ()
constroi_arvore3(tamanho)
print ()
