# Programa que calcula funções de grau 2
# Uma função do segundo grau é dada por f(x) = ax² + bx + c

import math

while True:
    a = int(input('Digite o valor de a: '))

    while a == 0:
        print('Para uma função de segundo grau, o valor de a deve ser diferente de zero.\n')
        a = int(input('Digite novamente o valor de a: '))

    b = int(input('Digite o valor de b: '))
    c = int(input('Digite o valor de c: '))

    x = 0
    lista_y = []

    def calculaFuncao(a, b, c, x):
        for x in range(-5, 5 + 1, 1):
            y = (a * (x * x)) + (b * x) + c
            lista_y.append(y)

        delta = (b * b) - (4 * a * c)

        return y, delta

    def calculaRaizes(a, b, delta):
        if delta >= 0:
            raiz_1 = (-b + math.sqrt(delta)) / (2 * a)

            raiz_2 = (-b - math.sqrt(delta)) / (2 * a)

            return raiz_1, raiz_2
        
        if delta < 0:
            return None, None

    def maximo_minimo(a, b, delta):
        x_vertice = -b / (2 * a)
        y_vertice = -delta / (4 * a)

        return x_vertice, y_vertice

    y, delta = calculaFuncao(a, b, c, x)
    raiz_1, raiz_2 = calculaRaizes(a, b, delta)
    x_vertice, y_vertice = maximo_minimo(a, b, delta)

    print('DADOS DA FUNÇÃO\n')
    print('Valor de a: ', a, '\n')
    print('Valor de b: ', b, '\n')
    print('Valor de c: ', c, '\n')
    print('Para x igual a: ', x, 'a função resulta em: ', y, '\n')

    if a > 0:
        print('A concavidade desta parábola aponta para cima')
        print('O ponto de mínimo desta parábola é dado por x igual a', x_vertice, 'e y igual a', y_vertice)

    if a < 0:
        print('A concavidade desta parábola aponta para baixo')
        print('O ponto de máximo desta parábola é dado por x igual a', x_vertice, 'e y igual a', y_vertice)

    print('\n')

    if delta > 0:
        print('Esta função possui duas raízes reais distintas, sendo elas: ', raiz_1, 'e', raiz_2)

    if delta == 0:
        print('Esta função possui duas raízes reais idênticas, sendo elas', raiz_1, 'e', raiz_2)

    if delta < 0:
        print('Esta função não possui raízes reais, as duas raízes são complexas. Este programa não tem capacidade para calcular raízes complexas')

    print(lista_y)
    print('Valores de y para x variando de -5 a 5.\n\n\n')