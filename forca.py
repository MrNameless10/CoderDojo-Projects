import random, sys

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

    letrasFalhadas= []
    letrasCorretas= []
    palavraCorreta = random.choice(PALAVRAS)

    while True: #Loop do jogo principal
        desenharforca(letrasFalhadas, letrasCorretas, palavraCorreta)
        palpite = palpitedojogador(letrasFalhadas + letrasCorretas)
        
        if palpite in palavraCorreta:
            letrasCorretas.append(palpite)

            venceu = True
            for letrapalavraCorreta in palavraCorreta:
                if letrapalavraCorreta not in letrasCorretas:
                    venceu = False
                    break
            if venceu:
                print('Boa a palvra é', palavraCorreta)
                print('Ganhaste')
        else:
            letrasFalhadas.append(palpite)

            if len(letrasFalhadas) == len(figuras) - 1:
                desenharforca(letrasFalhadas, letrasCorretas, palavraCorreta)
                print('ficaste sem palpites')
                print('A palvra era:', palavraCorreta)
                break


def desenharforca(letrasFalhadas, letrasCorretas, palavraCorreta):
    print(figuras[len(letrasFalhadas)])
    print('A categoria é:', CATEGORIA)
    print()

    print('letrasFalhadas:', end='')
    for letra in letrasFalhadas:
        print(letra, end=' ')
    if len(letrasFalhadas)==0:
        print('sem letras falhadas')
    print()

    espaços = ['_'] * len(palavraCorreta)

    for i in range(len(palavraCorreta)):
        if palavraCorreta[i] in letrasCorretas:
            espaços[i] = palavraCorreta[i]

    print(' '.join(espaços))

def palpitedojogador(palpitepreenchido):
    while True:
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
        