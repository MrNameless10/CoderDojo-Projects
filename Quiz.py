from time import sleep

def jogo_adivinha(pergunta, hipoteses,respostacerta):
  global pontos
  global p_tentativas
  p_tentativas = 0
  ainda_joga = True
  tentativa = 0
  sleep(1)
  print(pergunta)
  sleep(1)
  for hipotese in hipoteses:
    print(hipotese)
    sleep(1)
  input_u = input().upper()
  while ainda_joga or tentativa < 2:
    if input_u == respostacerta:
      print('\x1b[6;30;42m' + '\nEstá certo!\n' + '\x1b[0m')
      ainda_joga = False
      pontos = pontos+1
      
    else :
      if tentativa < 2:
        print("\nResposta errada, tenta outra vez")
        input_u = input()
        p_tentativas =  1
      tentativa = tentativa+1

    if tentativa == 2:
      print('\033[31m'+ "\nErraste!" + '\x1b[0m')
      print("a tua resposta deveria ser:")
      print(f"{respostacerta})\n")
      ainda_joga= False
      p_tentativas =  2

    

def print_frases(tentativas, nome):
  if tentativas == 0:
    print(f"Boa {nome} logo de primeira!\n")
  else:
    print(f"Cuidado {nome} pensa melhor antes de responder!\n")







pontos = 0
p_tentativas = 0
print("Jogo do advinha")
nome = input("Desculpe, esqueci seu nome. Qual é o seu nome? (digite seu nome) ")
print("Claro que é esse o teu nome \n")
sleep(2)
print("Vamos começar o jogo")

pergunta1 = ("\nQual é a minha cor favorita?\n")
hipoteses1 = ["A) Amarelo", "B) Branco", "C) Preto", "D) Outra"]
jogo_adivinha(pergunta1, hipoteses1, "A")
print_frases(p_tentativas, nome)

pergunta2 = ("Quem é a melhor pessoa do mundo?\n")
hipoteses2 = ["A) Amarelo", "B) Branco", "C) Preto", "D) Outra"]
jogo_adivinha(pergunta2,hipoteses2, "C")
print_frases(p_tentativas, nome)

sleep(1)
print(f"Muito bem {nome}, o jogo acabou!")
print("Acabaste com:", pontos, "pontos")