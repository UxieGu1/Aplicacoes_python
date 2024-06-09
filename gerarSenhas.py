#aqui importo as bibliotecas do python
import secrets as sc
import string as st
import random as rd

#aqui seleciono os caracteres em suas respectivas variáveis 
letras = st.ascii_letters
numeros = st.digits
caracteres = st.punctuation[0:5]
lista_caracteres = letras + numeros + caracteres

#aqui o usuário digita o tamanho da fonte
tamanho_senha = int(input(f'Digite o tamanho da senha que você deseja: '))

#aqui criamos a senha aleatoriamente 
senha_segura = ''
for i in range(tamanho_senha):
    senha_segura += ''.join(sc.choice(lista_caracteres))

#printamos a senha final(totalmente segura)
print(f'A senha gerada aleatoriamente é: {senha_segura}')
