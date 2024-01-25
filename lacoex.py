# n = int(input('Digite um número para saber o fatorial: '))
# f = 1
# for i in range(1, n + 1):
#     f *= i
# print(f'O resultado de {n}! é {f}')

n = int(input('Digite um número para saber seu fatorial: '))
f = 1
for c in range(n, 1, -1):
    f *= c
print('{}! = {}'.format(n, f))
