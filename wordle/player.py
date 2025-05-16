
# Nome completo do primeiro membro: Roger Honorato
# RA do primeiro membro: 247617
# Nome completo do segundo membro: Leonardo Paillo da Silva
# RA do segundo membro: 198218

"""
Implemente aqui o seu código para adivinhar a palavra.

Seu principal objetivo é implementar a função `player`, que deve retornar uma palavra (string) como seu próximo palpite.
Caso sua função não retorne uma string, a automatização não irá ocorrer tanto em game.py quanto em tournament.py.
Caso sua função retorne a string vazia, você poderá jogar manualmente (teclado).

Observações:
- Você pode implementar outras funções para auxiliar a função `player`.
- Você pode salvar informações entre os palpites usando variáveis globais (fora de qualquer função).
- A função recebe duas listas como argumento:
    - guess_hist: lista de palavras que foram chutadas anteriormente
    - res_hist: lista de respostas dos chutes anteriores
- A função deve retornar uma string como palpite

Lembretes:
- Segue a coloração possíveis dos caracteres:
    - Correto: verde ("GREEN")
    - Presente mas na posição errada: amarelo ("YELLOW")
    - Ausente: vermelho ("RED")

Para mais informações, reveja o README.md
"""

import random
from utils import load_words, ALL_COLORS

palavras_possiveis = load_words()   # Carrega a lista de palavras
palavras_filtradas = palavras_possiveis.copy()

for i in palavras_possiveis:  # remove todas as palavras com tamanho invalido
    if len(i) != 5:
        palavras_filtradas.remove(i)
lista_palavras = palavras_filtradas.copy()


def filtro_red():  # filtra a lista de lista_palavras possíveis, removendo todas as que tem letras eliminadas
    placeholder = lista_palavras.copy()
    for word in placeholder:
        for char in word:
            if char in eliminadas:
                lista_palavras.remove(word)
                break
    eliminadas.clear()
    return lista_palavras


def filtro_yellow(letra, posição):
    placeholder = lista_palavras.copy()
    for word in placeholder:
        if word[posição] == letra:
            lista_palavras.remove(word)
    return lista_palavras


def filtro_green():
    placeholder = lista_palavras.copy()
    for index, letra in enumerate(correta):
        if letra != "":
            for word in placeholder:
                if word[index] != letra and word in lista_palavras:
                    lista_palavras.remove(word)
    return lista_palavras


amarelas = []  # Letras que estão na palavra correta mas na posição errada
eliminadas = []  # Letras que não estão na palavra correta
correta = ["", "", "", "", ""]  # resposta correta, com as letras em ordem


def player(guess_hist, res_hist):
    global lista_palavras

    if guess_hist != [] and res_hist != []:
        ultima_tentativa = guess_hist[-1]
        correção = res_hist[-1]
        # relaciona as letras com a resposta
        a = [
            [ultima_tentativa[0], correção[0]],
            [ultima_tentativa[1], correção[1]],
            [ultima_tentativa[2], correção[2]],
            [ultima_tentativa[3], correção[3]],
            [ultima_tentativa[4], correção[4]],
            ]
        for sublist in a:
            letra = sublist[0]

            match sublist[1]:   # verifica qual a resposta
                case "GREEN":
                    if letra in eliminadas:
                        eliminadas.remove(letra)
                    # adiciona o caractere na posição correta
                    correta.pop(a.index(sublist))
                    correta.insert(a.index(sublist), letra)

                case "RED":
                    if letra not in eliminadas and letra not in amarelas:
                        eliminadas.append(letra)
                        lista_palavras = filtro_red()

                case "YELLOW":
                    lista_palavras = filtro_yellow(letra, a.index(sublist))

        if len("".join(correta)) != 5:

            lista_palavras = filtro_green()
            guess = random.choice(lista_palavras)
        else:
            guess = "".join(correta)
    else:
        if 'TRACE' in lista_palavras:
            guess = 'trace'
        elif 'CLASE' in lista_palavras:
            guess = 'clase'
        elif 'METAL' in lista_palavras:
            guess = 'metal'
        elif 'ELICA' in lista_palavras:
            guess = 'elica'
    return guess
