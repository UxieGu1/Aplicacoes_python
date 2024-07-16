import random as rd
import time

opcoes = ['pedra', 'papel', 'tesoura']
def jogada():
    jogada = str(input("Escolha entre: Pedra, Papel ou Tesoura: \n")).lower()
    jogadaMaquina = rd.choice(opcoes)
    print('.')
    time.sleep(2)
    print('.')
    time.sleep(2)
    print('.')
    time.sleep(2)
    if jogada == 'pedra' and jogadaMaquina == 'papel':
        print('A máquina ganhou!')
    elif jogada == 'pedra' and jogadaMaquina == 'tesoura':
        print('Você ganhou!')
    elif jogada == 'pedra' and jogadaMaquina == 'pedra':
        print('Deu empate!')

    elif jogada == 'papel' and jogadaMaquina == 'tesoura':
        print('A máquina ganhou!')
    elif jogada == 'papel' and jogadaMaquina == 'pedra':
        print('Você ganhou!')
    elif jogada == 'papel' and jogadaMaquina == 'papel':
        print('Deu empate!')

    elif jogada == 'tesoura' and jogadaMaquina == 'pedra':
        print('A máquina ganhou!')
    elif jogada == 'tesoura' and jogadaMaquina == 'papel':
        print('Você ganhou!')
    elif jogada == 'tesoura' and jogadaMaquina == 'tesoura':
        print('Deu empate!')

    else:
        print('Jogada inválida. Por favor, escolha entre "pedra", "papel" ou "tesoura".')


MENSAGEM_INICIO = """
Pedra papel tesoura

[1] - Começar
[0] - Sair
"""

def main():
    while True:
        print(MENSAGEM_INICIO)
        escolha = int(input())
        if escolha == 1:
            jogada()
        elif escolha == 0:
            break
        else:

            break
if __name__ == "__main__":
    main()
