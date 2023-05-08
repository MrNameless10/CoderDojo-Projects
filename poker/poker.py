
import unittest

import tkinter as tk
from tkinter import messagebox

def valor_carta(carta):
    valor = carta[:-1]
    if valor == 'A':
        return 14
    elif valor == 'K':
        return 13
    elif valor == 'Q':
        return 12
    elif valor == 'J':
        return 11
    else:
        return int(valor)
    
def valor_para_string(valor):
    if valor == 14:
        return "A"
    elif valor == 13:
        return "K"
    elif valor == 12:
        return "Q"
    elif valor == 11:
        return "J"
    else:
        return str(valor)
    

def naipe_carta(carta):
    return carta[-1]

def carta_valida(carta):
    valores_validos = [str(i) for i in range(2, 11)] + ["J", "Q", "K", "A"]
    naipes_validos = ["c", "e", "o", "p"]
    valor, naipe = carta[:-1], carta[-1]

    return valor in valores_validos and naipe in naipes_validos

def sequencia(valores):
    valores_ordenados = sorted(valores)

    if valores_ordenados == list(range(min(valores), max(valores) + 1)):
        return True

    sequencia_baixa = [14, 2, 3, 4, 5]
    if set(valores_ordenados) == set(sequencia_baixa):
        return True

    return False


def mao_poker(mao):
    if len(mao) != 5:
        return "Erro: A mão deve ter exatamente 5 cartas"
    
    for carta in mao:
        if not carta_valida(carta):
            return f"Erro: Carta inválida '{carta}'"

    valores = [valor_carta(carta) for carta in mao]
    naipes = [naipe_carta(carta) for carta in mao]

    contador_valores = {valor: valores.count(valor) for valor in set(valores)}
    contador_naipes = {naipe: naipes.count(naipe) for naipe in set(naipes)}

    tem_sequencia = sequencia(valores)
    tem_flush = max(contador_naipes.values()) == 5

    if tem_sequencia:
        if set(valores) == {14, 2, 3, 4, 5}:
            inicio_sequencia = 1
        else:
            inicio_sequencia = min(valores)
        
        if tem_flush:
            if inicio_sequencia == 10:
                return "Royal Flush"
            else:
                return f"Straight Flush de {inicio_sequencia} a {valor_para_string(inicio_sequencia + 4)}"
        else:
            return f"Sequencia de {inicio_sequencia} a {valor_para_string(inicio_sequencia + 4)}"
    
    

    if 4 in contador_valores.values():
        valor_poker = [valor for valor, count in contador_valores.items() if count == 4][0]
        return f"Poker de {valor_para_string(valor_poker)}"

    if 3 in contador_valores.values() and 2 in contador_valores.values():
        trio_valor = [valor for valor, count in contador_valores.items() if count == 3][0]
        par_valor = [valor for valor, count in contador_valores.items() if count == 2][0]
        return f"Full House de {valor_para_string(trio_valor)} por {valor_para_string(par_valor)}"

    if tem_flush:
        return "Flush"

    if tem_sequencia:
        inicio_sequencia = min(valores) if 14 not in valores else 1
        return f"Sequência de {inicio_sequencia} a {inicio_sequencia + 4}"

    if 3 in contador_valores.values():
        trio_valor = [valor for valor, count in contador_valores.items() if count == 3][0]
        return f"Trio de {valor_para_string(trio_valor)}"

    if len([valor for valor, count in contador_valores.items() if count == 2]) == 2:
        pares_valores = [valor for valor, count in contador_valores.items() if count == 2]
        return f"Dois Pares de {valor_para_string(pares_valores[0])} e {valor_para_string(pares_valores[1])}"

    if 2 in contador_valores.values():
        par_valor = [valor for valor, count in contador_valores.items() if count == 2][0]
        return f"Par de {valor_para_string(par_valor)}"

    carta_alta = max(valores)
    return f"Carta Alta {valor_para_string(carta_alta)}"




def verificar_mao():
    mao = entry.get().split()
    if len(mao) != 5:
        messagebox.showerror("Erro", "A mão deve ter exatamente 5 cartas")
        return

    for carta in mao:
        if not carta_valida(carta):
            messagebox.showerror("Erro", f"Carta inválida '{carta}'")
            return

    resultado = mao_poker(mao)
    messagebox.showinfo("Resultado", resultado)

app = tk.Tk()
app.title("Pôquer")

# Configuração do estilo
app.configure(bg="#F5F5F5")  # Cor de fundo do aplicativo

# Carrega a imagem de fundo
background_image = tk.PhotoImage(file="poker_background.png")

# Configuração do frame
frame = tk.Frame(app, padx=20, pady=20, bg="#F5F5F5")  # Cor de fundo do frame
frame.pack()

# Adiciona a imagem de fundo ao frame
background_label = tk.Label(frame, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

label = tk.Label(frame, text="Digite sua mão (Exemplo: 10c Jc Qc Ac Kc):", bg="#F5F5F5")
label.pack()

entry = tk.Entry(frame, width=30)
entry.pack()

button = tk.Button(frame, text="Verificar mão", command=verificar_mao, bg="#4CAF50", fg="white", relief="raised")
button.pack(pady=10)

app.mainloop()


# Exemplos de uso:

print(mao_poker(["10c", "Jc", "Qc", "Ac", "Kc"])) # "Royal Flush"
print(mao_poker(["3c", "5c", "Qe", "9c", "Ao"])) # "Carta Alta"
print(mao_poker(["10e", "10p", "8o", "10o", "10c"])) # "Poker"
print(mao_poker(["4c", "9e", "2e", "2o", "Ao"])) # "Par"
print(mao_poker(["10e", "9e", "8e", "6e", "7e"])) # "Straight Flush"
print(mao_poker(["10p", "9p", "9e", "10e", "9c"])) # "Full House"
print(mao_poker(["8c", "2c", "8e", "3e", "3p"])) # "Dois Pares"
print(mao_poker(["Jc", "9c", "7c", "5c", "2c"])) # "Flush"
print(mao_poker(["Ap", "Qp", "Ae", "Ac", "2o"])) # "Trio"
print(mao_poker(["Ao", "Ko", "Qo", "Jo", "9o"])) # "Flush"
print(mao_poker(["10c", "Jc", "Qe", "Ke", "Ap"])) # "Sequência"
print(mao_poker(["3c", "8c", "2e", "3e", "3o"])) # "Trio"
print(mao_poker(["4c", "Ap", "4e", "4o", "4p"])) # "Poker"
print(mao_poker(["3c", "8c", "2e", "3e", "2o"])) # "Dois Pares"
print(mao_poker(["8c", "8e", "Ae", "Qc", "Kc"])) # "Par"



class TestPoker(unittest.TestCase):

    def test_royal_flush(self):
        mao = ["10c", "Jc", "Qc", "Ac", "Kc"]
        resultado = mao_poker(mao)
        self.assertEqual(resultado, "Royal Flush")

    def test_carta_alta(self):
        mao = ["3c", "5c", "Qe", "9c", "Ao"]
        resultado = mao_poker(mao)
        self.assertEqual(resultado, "Carta Alta A")

    def test_poker(self):
        mao = ["10e", "10p", "8o", "10o", "10c"]
        resultado = mao_poker(mao)
        self.assertEqual(resultado, "Poker de 10")

    def test_par(self):
        mao = ["4c", "9e", "2e", "2o", "Ao"]
        resultado = mao_poker(mao)
        self.assertEqual(resultado, "Par de 2")

    def test_straight_flush(self):
        mao = ["10e", "9e", "8e", "6e", "7e"]
        resultado = mao_poker(mao)
        self.assertEqual(resultado, "Straight Flush de 6 a 10")

    def test_full_house(self):
        mao = ["10p", "9p", "9e", "10e", "9c"]
        resultado = mao_poker(mao)
        self.assertEqual(resultado, "Full House de 9 por 10")
    
    def test_dois_pares(self):
        mao = ["8c", "2c", "8e", "3e", "3p"]
        resultado = mao_poker(mao)
        self.assertEqual(resultado, "Dois Pares de 3 e 8")
    
    def test_flush(self):
        mao = ["Jc", "9c", "7c", "5c", "2c"]
        resultado = mao_poker(mao)
        self.assertEqual(resultado, "Flush")

    def test_trio(self):
        mao = ["Ap", "Qp", "Ae", "Ac", "2o"]
        resultado = mao_poker(mao)
        self.assertEqual(resultado, "Trio de A")

    def test_flush(self):
        mao = ["Ao", "Ko", "Qo", "Jo", "9o"]
        resultado = mao_poker(mao)
        self.assertEqual(resultado, "Flush")

    def test_sequencia(self):
        mao = ["10c", "Jc", "Qe", "Ke", "Ap"]
        resultado = mao_poker(mao)
        self.assertEqual(resultado, "Sequencia de 10 a A")
    
    def test_trio(self):
        mao = ["3c", "8c", "2e", "3e", "3o"]
        resultado = mao_poker(mao)
        self.assertEqual(resultado, "Trio de 3")

    def test_poker(self):
        mao = ["4c", "Ap", "4e", "4o", "4p"]
        resultado = mao_poker(mao)
        self.assertEqual(resultado, "Poker de 4")

    def test_dois_pares(self):
        mao = ["3c", "8c", "2e", "3e", "2o"]
        resultado = mao_poker(mao)
        self.assertEqual(resultado, "Dois Pares de 2 e 3")

    def test_par(self):
        mao = ["8c", "8e", "Ae", "Qc", "Kc"]
        resultado = mao_poker(mao)
        self.assertEqual(resultado, "Par de 8")

if __name__ == "__main__":
    unittest.main()