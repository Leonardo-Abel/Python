from random import choice

p = str(input('Primeiro aluno: '))
s = str(input('Segundo aluno: '))
t = str(input('Terceiro aluno: '))
q = str(input('Quarto aluno: '))
l = [p, s, t, q]
r = choice(l)
print('O aluno escolhido foi {}.'.format(r))
