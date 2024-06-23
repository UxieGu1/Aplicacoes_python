
# a. Comprimento da senha: mínimo de oito caracteres
# b. Caracteres numéricos: mínimo de dois números
# c. Caracteres especiais: mínimo de um caractere especial
# d. Letras maiúsculas: mínimo de uma letra maiúscula
# e. Letras minúsculas: mínimo de uma letra minúscula

def verificarTamanho(senha):
    if len(senha) >= 8:
        print(f'A senha está dentro dos conformes de tamanho!')
    else:
        print(f'A senha não está dentro dos conformes de tamanho!')

def verificarNumeros(senha):
    contador = 0
    for caractere in senha:
        if caractere.isdigit(): 
            contador += 1
    if contador >= 2:
        print(f'A senha está dentro dos conformes de numeração!')
    else:
        print(f'A senha não está dentro dos conformes de numeração!')

def verificarCaractere(senha):
    caracteres_especiais = "#@!?"
    contador_caracteres = sum(1 for caractere in senha if caractere in caracteres_especiais)
    if contador_caracteres >= 1:
        print(f'A senha está dentro dos conformes de caracteres especiais!')
    else:
        print(f'A senha não está dentro dos conformes de caracteres especiais!')

def verificarLetraMaiuscula(senha):
    if any(x.isupper() for x in senha):
        print(f'A senha está dentro dos conformes de letras maiúsculas!')
    else:
        print(f'A senha não está dentro dos conformes de letras maiúsculas!')

def verificarLetraMinuscula(senha):
    if any(x.islower() for x in senha):
        print(f'A senha está dentro dos conformes de letras minúsculas!')
    else:
        print(f'A senha não está dentro dos conformes de letras minúsculas!')

s = input('Digite sua senha: ')

verificarTamanho(s)
verificarNumeros(s)
verificarCaractere(s)
verificarLetraMaiuscula(s)
verificarLetraMinuscula(s)
