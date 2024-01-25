'''continuar = 'S'
maioridade = homens = mulhermin20 = 0
while continuar == 'S':
    print('-'*30)
    print('    CADASTRE UMA PESSOA')
    print('-'*30)
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).upper().strip()
    while s != 'M' and s != 'F':
        s = str(input('Sexo [M/F]: ')).upper().strip()
    print('-'*30)
    if i >= 18:
        maioridade += 1
    if s == 'M':
        homens += 1
    if s == 'F' and i < 20:
        mulhermin20 += 1
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if continuar == 'N':
        print('-'*30)
        print(f'A quantidade de pessoas com MAIS DE 18 anos é: {maioridade}')
        print(f'A quantidade de HOMENS cadastrados foi de: {homens}')
        print(
            f'A quantidade de MULHERES com menos de 20 anos é de: {mulhermin20}')
        break
'''

# GUANABARA
tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')
