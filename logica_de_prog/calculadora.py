#Calculadora
def soma (n1, n2):
    soma = (n1 + n2)
    return soma
def subtracao (n1, n2):
    subtracao = (n1 - n2)
    return subtracao
def multiplicacao (n1, n2):
    multiplicacao = (n1 * n2)
    return multiplicacao
def divisao (n1, n2):
    divisao = (n1 / n2)
    return divisao

print('''\n******************* Calculadora *******************
\nSelecione o número da opção desejada:
1- Soma
2- Subtração
3- Multiplicação
4- Divisão''')
op = int(input("\nDigite sua opção: "))
n1 = float(input("\nDigite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
if (op == 1):
    print("\nResultado:",soma(n1,n2))
elif (op == 2):
    print("\nResultado:",subtracao(n1,n2))
elif (op == 3):
    print("\nResultado:",multiplicacao(n1,n2))
elif (op == 4):
    print("\nResultado:",divisao(n1,n2))
else:
    print("\nOperação Invalida!\nResultado: 0")