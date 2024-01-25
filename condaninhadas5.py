n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m < 5.0:
    print('A nota final foi de {:.1f}. REPROVADO'.format(m))
elif m <= 6.9:
    print('A nota final foi de {:.1f}. RECUPERAÇÃO'.format(m))
elif m >= 7.0:
    print('A nota final foi de {:.1f}. APROVADO'.format(m))
