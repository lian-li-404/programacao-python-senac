#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = str(input('Digite seu Turno:\nM-Matutino\nV-Vespertino\nN- Noturno: ')).strip().upper()

if turno == 'M':
    print("Bom dia!")
elif turno == 'V':
    print("Boa tarde!")
elif turno == 'N':
    print("Boa Noite!")
else:
    print("Você digitou uma opção inválida!")
