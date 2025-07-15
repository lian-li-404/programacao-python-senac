import tkinter as tk

### Operadores Aritiméticos 

adicao = 2 + 2
print('Adição =>', adicao)

subtracao = 2 - 2
print('Subtração =>', subtracao)

multiplicacao = 2*2
print("Multiplicação =>", multiplicacao)

divisao = 10 / 3
print("Divisão =>", divisao)

divisao_inteira = 10 // 3
print("Divisão Inteira =>", divisao_inteira)

exponeciacao = 2 ** 2
print("Exponenciação =>", exponeciacao)

modulo = 55 % 2
print("Resto da divisão =>", modulo)

precedencia = (180 + 20)  / 2
print(precedencia)

sem_parenteses = 180 + 20 / 2
print(sem_parenteses)


""" 
-----------------------------------------------------
Ordem de precedencia das operações matemáticas:
1. () -- As operações dentro dos parenteses
2. **
3. / // * %
4. + - 
-----------------------------------------------------

"""

main = tk.Tk()

def somar(n1, n2):
    n1 = int(n1)
    n2 = int(n2)
    resultado = tk.Label(main, text= f'O Resultado é : {n1 + n2}')
    resultado.place(x=10, y=100)

label_primeiro = tk.Label(main, text="Primeiro Número:")
label_primeiro.place(x=10, y=0)

entry_primeiro = tk.Entry(main)
entry_primeiro.place(x=10, y=20)

label_segundo = tk.Label(main, text="Segundo Número:")
label_segundo.place(x=150, y=0)

entry_segundo = tk.Entry(main)
entry_segundo.place(x=150, y=20)


bt_soma = tk.Button(main, width=10, text= "Somar", command=lambda: somar(int(entry_primeiro.get()),int(entry_segundo.get()) ))
bt_soma.place(x=10, y=50)


main.mainloop()