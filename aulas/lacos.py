
import streamlit as st

print('-----------------------While---------------------------------')

## While
a = 1
while a <=5:
    print('Hello World!')
    a = a+1

print('-----------------------For---------------------------------')

## For

for l in range(10):
    print('Hello World!')

print('-----------------------While True---------------------------------')

## While
password = 'elian123'
entrada = input('Digite sua senha: ')
while True:
    if entrada != password.strip():
        print('Senha Incorreta!')
        entrada = input('Digite sua senha: ')
    else:
        print('Login Realizado Com Sucesso!')
        break


print('-----------------------Exemplo com interface---------------------------------')

password = 'elian123'
password_input = st.text_input("Digite sua Senha: ")
while True:
    if password_input != password.strip():
        st.warning('Senha Incorreta! Tente Novamente')
        password_input = st.text_input("Digite sua Senha: ")
    else:
        st.success('Login Realizado Com Sucesso!')
        break