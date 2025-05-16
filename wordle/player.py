
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

lista_palavras = load_words()   # carrega a lista de palavras
palavras_filtradas = lista_palavras.copy()

for i in lista_palavras:  # remove as palavras com tamanho invalido
    if len(i) != 5:
        palavras_filtradas.remove(i)
lista_palavras = palavras_filtradas.copy()


def filtro_red():  # remove as palavras que tem letras eliminadas
    placeholder = lista_palavras.copy()
    for word in placeholder:
        for letra in eliminadas:
            if letra in word:
                lista_palavras.remove(word)
                break
    return lista_palavras


def filtro_yellow(letra, posição):
    placeholder = lista_palavras.copy()
    for word in placeholder:

        if letra not in word:  # remove palavras que não possuem a letra
            lista_palavras.remove(word)

        else:
            # remove palavras onde a letra amarela está na mesma posição
            if word[posição] == letra:
                lista_palavras.remove(word)

    return lista_palavras


def filtro_green(letra, posição):
    placeholder = lista_palavras.copy()

    for word in placeholder:

        if letra not in word:
            lista_palavras.remove(word)

        elif word[posição] != letra:
            lista_palavras.remove(word)

    return lista_palavras


amarelas = []  # letras que estão na palavra correta
correta = ["", "", "", "", ""]  # resposta correta, com as letras em ordem
eliminadas = []  # letras eliminadas


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

            match sublist[1]:
                case "GREEN":

                    correta.pop(a.index(sublist))
                    correta.insert(a.index(sublist), letra)
                    lista_palavras = filtro_green(letra.upper(), a.index(sublist))

                case "RED":
                    if letra not in eliminadas:
                        eliminadas.append(letra)

                case "YELLOW":
                    if letra not in amarelas:
                        amarelas.append(letra)

                    lista_palavras = filtro_yellow(letra.upper(), a.index(sublist))

        if len("".join(correta)) != 5:
            placeholder = eliminadas.copy()

            for letra in placeholder:
                if letra in correta:
                    eliminadas.remove(letra)

                elif letra in amarelas:
                    eliminadas.remove(letra)

            lista_palavras = filtro_red()
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
