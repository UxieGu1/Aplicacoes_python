import math as mt

class Calculadora():
    def __init__(self, adicao=True, subtracao=True, multiplicacao=True, divisao=True, 
    fatorial=False, raiz=False, quadrado=False, cubo=False, potencia=False):

        self.adicao = adicao
        self.subtracao = subtracao
        self.multiplicacao = multiplicacao
        self.divisao = divisao
        self.fatorial = fatorial
        self.raiz = raiz
        self.quadrado = quadrado
        self.cubo = cubo
        self.potencia = potencia

    def somar(self, n1, n2):
        if not self.adicao:
            raise ValueError("Operação de adição não está habilitada.")
        return n1 + n2

    def subtrair(self, n1, n2):
        if not self.multiplicacao:
            raise ValueError("Operação de multiplicação não está habilitada.")
        return n1 - n2

    def multiplicar(self, n1, n2):
        if not self.multiplicacao:
            raise ValueError("Operação de multiplicação não está habilitada.")
        if n1 == 0 or n2 == 0:
            return 0
        else:
            return n1 * n2
    
    def dividir(self, n1, n2):
        if not self.divisao:
            raise ValueError("Operação de divisão não está habilitada.")
        if n1 == n2:
            return 1
        if n2 == 0:
            raise ZeroDivisionError("Divisão por zero não permitida.")
        else:
            return n1 / n2

    def fatorial_n(self, n1):
        if not self.fatorial:
            raise ValueError("Operação de fatorial não está habilitada.")
        if n1 < 0:
            raise ValueError("Não é possível calcular o fatorial de um número negativo.")
        if n1 == 1:
            return 1
        else:
            return n1 * self.fatorial_n(n1 - 1)

    def raiz_quadrada(self, n1):
        if not self.raiz:
            raise ValueError("Operação de raiz quadrada não está habilitada.")
        if n1 < 0:
            raise ValueError("Não é possível calcular a raiz quadrada de um número negativo.")
        return mt.sqrt(n1)

    def quadrado_n(self, n1):
        if not self.quadrado:
            raise ValueError("Operação de quadrado não está habilitada.")
        if n1 == 1:
            return 1
        else:
            return n1 ** 2

    def cubo_n(self, n1):
        if not self.cubo:
            raise ValueError("Operação de cubo não está habilitada.")
        if n1 == 1:
            return 1
        else:
            return n1 ** 3

    def potenciacao(self, base, expoente):
        if not self.potencia:
            raise ValueError("Operação de potência não está habilitada.")
        if base ==  1:
            return 1
        if expoente == 0:
            return 1
        else:
            return base ** expoente
        
MENSAGEM_INICIO = """
Calculadora

[1] Somar
[2] Subtrair
[3] Multiplicar
[4] Dividir
[5] Fatorial
[6] Raiz Quadrada
[7] Quadrado
[8] Cubo
[9] Potência
[0] Sair
"""

def main():
    calc = Calculadora()
    calc_avancada = Calculadora(fatorial=True, raiz=True, quadrado=True, cubo=True, potencia=True)

    while True:
        try:
            print("-" * 40)
            print(MENSAGEM_INICIO)
            escolha = int(input('Digite o que você deseja fazer: '))
            print("-" * 40)
            if escolha == 1:
                print('ADIÇÃO:')
                n1 = int(input('Digite o primeiro valor: '))
                n2 = int(input('Digite o segundo valor: '))
                resultado = calc.somar(n1, n2)
                print(f"Resultado: {resultado}")

            elif escolha == 2:
                print('SUBTRAÇÃO:')
                n1 = int(input('Digite o primeiro valor: '))
                n2 = int(input('Digite o segundo valor: '))
                resultado = calc.subtrair(n1, n2)
                print(f"Resultado: {resultado}")

            elif escolha == 3:
                print('MULTIPLICAÇÃO:')
                n1 = int(input('Digite o primeiro valor: '))
                n2 = int(input('Digite o segundo valor: '))
                resultado = calc.multiplicar(n1, n2)
                print(f"Resultado: {resultado}")

            elif escolha == 4:
                print('DIVISÃO:')
                n1 = int(input('Digite o primeiro valor: '))
                n2 = int(input('Digite o segundo valor: '))
                resultado = calc.dividir(n1, n2)
                print(f"Resultado: {resultado}")

            elif escolha == 5:
                print('FATORIAL:')
                n1 = int(input('Digite o valor: '))
                resultado = calc_avancada.fatorial_n(n1)
                print(f"Resultado: {resultado}")

            elif escolha == 6:
                print('RAIZ QUADRADA:')
                n1 = int(input('Digite o valor: '))
                resultado = calc_avancada.raiz_quadrada(n1)
                print(f"Resultado: {resultado}")

            elif escolha == 7:
                print('QUADRADO:')
                n1 = int(input('Digite o valor a ser elevado ao quadrado: '))
                resultado = calc_avancada.quadrado_n(n1)
                print(f"Resultado: {resultado}")

            elif escolha ==  8:
                print('CUBO:')
                n1 = int(input('Digite o valor a ser elevado ao cubo '))
                resultado = calc_avancada.cubo_n(n1)
                print(f"Resultado: {resultado}")

            elif escolha == 9:
                print('POTENCIAÇÃO:')
                base = float(input("Digite a base: "))
                expoente = float(input("Digite o expoente: "))
                resultado = calc_avancada.potenciacao(base, expoente)
                print(f"Resultado: {resultado}")

            elif escolha == 0:
                print("Encerrando calculadora!")
                break
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

if __name__ == "__main__":
    main()
