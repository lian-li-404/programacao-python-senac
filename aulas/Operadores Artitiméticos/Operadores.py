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

label = tk.Label(main, text="Calculadora")
label.place(x=0, y=0)

entry = tk.Entry(main)
entry.place(x=0, y=20)


main.mainloop()