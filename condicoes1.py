from random import randint

num = randint(0, 5)
print('-=-' * 25)
u = int(input('Descubra o número sorteado entre 0 e 5: '))
print('-=-' * 25)
if u == num:
    print('Você acertou! O número sorteado foi: {}.'.format(num))
else:
    print('Você errou! O número sorteado foi: {}.'.format(num))
