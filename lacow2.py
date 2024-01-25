'''
from random import randint

palpite = 0
num = randint(0, 11)
u = ''

while num != u:
    print('-=-' * 25)
    u = int(input('Descubra o número sorteado entre 0 e 10: '))
    print('-=-' * 25)
    palpite += 1
    if u == num:
        print('Você acertou! O número sorteado foi: {}.'.format(num))
    else:
        print('Você errou! O número sorteado foi: {}.'.format(num))
print('Até a sua vitória, você teve {} palpites.'.format(palpite))
'''

from random import randint

computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} palpites. Parabéns!'.format(palpites))
