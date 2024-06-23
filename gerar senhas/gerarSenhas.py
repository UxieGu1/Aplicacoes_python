import secrets as sc
import string as st
import random as rd

letras = st.ascii_letters
numeros = st.digits
caracteres = st.punctuation[0:5]
lista_caracteres = letras + numeros + caracteres

tamanho_senha = int(input(f'Digite o tamanho da senha que você deseja: '))

senha_segura = ''
for i in range(tamanho_senha):
    senha_segura += ''.join(sc.choice(lista_caracteres))

print(f'A senha gerada aleatoriamente é: {senha_segura}')
