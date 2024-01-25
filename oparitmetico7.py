w = float(input('Digite a largura da parede: '))
h = float(input('Digite a altura parede: '))
a = w * h
t = a / 2
print('Sua parede tem dimensão de {}x{}. A área da parede é {}m², e você precisará de {}L de tinta.'.format(w, h, a, t))
