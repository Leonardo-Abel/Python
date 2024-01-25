m = float(input('Distância em metros: '))
mm = m * 1000
cm = m * 100
dm = m * 10
dam = m / 10
hm = m / 100
km = m / 1000
print('{:.0f}mm.'.format(mm))
print('{:.0f}cm.'.format(cm))
print('{:.0f}dm.'.format(dm))
print('{:.0f}m.'.format(m))
print('{}dam.'.format(dam))
print('{}hm.'.format(hm))
print('{}km.'.format(km))
