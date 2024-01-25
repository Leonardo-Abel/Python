from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
sexo = str(input('''Sexo:
[ M ]
[ F ]
Sua resposta: ''').upper())
if sexo == 'M':
    print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento.'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento será em {}.'.format(ano))
    else:
        saldo = idade - 18
        print('Você já deveria ter se alistado há {} anos.'.format(saldo))
        ano = atual - saldo
        print('Seu alistamento foi em {}.'.format(ano))
elif sexo == 'F':
    print('Você é do sexo feminino, não é necessário se alistar.')
else:
    print('Opção inválida. Tente novamente.')
