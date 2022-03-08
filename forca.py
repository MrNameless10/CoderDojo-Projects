import random, sys
# A version of this game is featured in the book "Invent Your Own Computer Games with Python"

figuras = [r"""
  +--+
  |  |
     |
     |
     |
     |
 =====""",
 r"""
  +--+
  |  |
  O  |
     |
     |
     |
 =====""",
 r"""
  +--+
  |  |
  O  |
  |  |
     |
     |
 =====""",
 r"""
  +--+
  |  |
  O  |
 /|  |
     |
     |
 =====""",
 r"""
  +--+
  |  |
  O  |
 /|\ |
     |
     |
 =====""",
 r"""
  +--+
  |  |
  O  |
 /|\ |
 /   |
     |
 =====""",
 r"""
  +--+
  |  |
  O  |
 /|\ |
 / \ |
     |
 ====="""]

CATEGORIA = 'nome'
PALAVRAS = 'MIKE RUI IVO CARRIÇO'.split()

def main():
    print('Enforcado do Nome_do_Ninja')
    
    #Variaveis para um novo jogo
    letrasFalhadas= [] #lista de letras incorretas
    letrasCorretas= [] #lista de letras corretas
    palavraCorreta = random.choice(PALAVRAS) # Palavra que o jogador tem que adivinhar

    while True: #Loop do jogo principal
        desenharforca(letrasFalhadas, letrasCorretas, palavraCorreta)
        #Deixar o jogador fazer um palpite
        palpite = palpitedojogador(letrasFalhadas + letrasCorretas)
        
        if palpite in palavraCorreta:
            #adicionar o palpite às letras corretas
            letrasCorretas.append(palpite)
            #verificar se o jogador ganhou:
            venceu = True # Vamos assumir que começa por ganhar o jogador

            for letrapalavraCorreta in palavraCorreta:
                # Há uma letra na palavra secreta que não é
                # ainda em letras corretas, então o jogador não ganhou:
                if letrapalavraCorreta not in letrasCorretas:
                    venceu = False
                    break
            if venceu:
                print('Boa a palvra é', palavraCorreta)
                print('Ganhaste')
                break # Acaba o jogo (volta ao loop principal)
        else:
            # O palpite do jogador é errado:
            letrasFalhadas.append(palpite)
            # Verificar se o jogador adivinhou muitas vezes e perdeu.
            # O "- 1" é porque não contamos a forca vazia em figuras
    
            if len(letrasFalhadas) == len(figuras) - 1:
                desenharforca(letrasFalhadas, letrasCorretas, palavraCorreta)
                print('ficaste sem palpites')
                print('A palvra era "{}"'.format(palavraCorreta))
                break


def desenharforca(letrasFalhadas, letrasCorretas, palavraCorreta):
    print(figuras[len(letrasFalhadas)])
    print('A categoria é:', CATEGORIA)
    print()

    # Mostra as letras adivinhadas incorretamente:
    print('letrasFalhadas:', end='')
    for letra in letrasFalhadas:
        print(letra, end=' ')
    if len(letrasFalhadas)==0:
        print('sem letras falhadas')
    print()

    # Exibe os espaços em branco para a palavra secreta (um espaço em branco por letra):
    espaços = ['_'] * len(palavraCorreta)

    # Substitui os espaços em branco por letras adivinhadas corretamente:
    for i in range(len(palavraCorreta)):
        if palavraCorreta[i] in letrasCorretas:
            espaços[i] = palavraCorreta[i]

    # Mostra a palavra secreta com espaços entre cada letra:
    print(' '.join(espaços))

def palpitedojogador(palpitepreenchido):
    while True: # Continua a perguntar até que o jogador digite uma letra válida.
        print('Dá um palpite.')
        palpite = input('> ').upper()
        if len(palpite) != 1:
            print('Só uma letra.')
        elif palpite in palpitepreenchido:
            print('Já está essa letra.')
        elif not palpite.isalpha():
            print('Dá um palpite2')
        else:
            return palpite

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
        