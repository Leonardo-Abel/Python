n = int(input('Digite um valor: '))
# d = n * 2
# t = n * 3
# r = n ** (1/2)    Outra maneira de fazer raiz: pow(x, y)
# print('Sobre {}, seu dobro é {}, seu triplo é {}, e sua raiz quadrada é {:.3f}.'
# .format(n, d, t, r))
print('Sobre {}, seu dobro é {}, seu triplo é {}, e sua raiz quadrada é {:.2f}.'.format(
    n, (n*2), (n*3), (n**(1/2))))
