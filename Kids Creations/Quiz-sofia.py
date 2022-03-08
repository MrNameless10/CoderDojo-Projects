def jogo_adivinha(input_u, respostacerta):
  global pontos
  ainda_joga = True
  tentativa = 0
  while ainda_joga and tentativa < 2:
    if input_u == respostacerta:
      print('\x1b[6;30;42m' + '\nEstá certo!\n' + '\x1b[0m')
      ainda_joga = False
      pontos = pontos+1
    else :
      if tentativa < 2:
        print("\nResposta errada, tenta outra vez")
        input_u = input()
      tentativa = tentativa+1 
  if tentativa == 2:
    print('\033[31m'+ "\nErraste!" + '\x1b[0m')
    print("a tua resposta deveria ser:")
    print(respostacerta,"\n")
    










pontos = 0
print("Jogo do advinha")
pergunta1 = input("\nQual é a minha cor favorita?\n")
jogo_adivinha(pergunta1, "Amarelo")
pergunta2 = input("Quem é a melhor pessoa do mundo?\n")
jogo_adivinha(pergunta2, "Sofia")
print("Acabaste com:", pontos, "pontos")