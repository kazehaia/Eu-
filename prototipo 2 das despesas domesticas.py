#prototipo 2° das despesas domesticas

'Balanço de despesas domesticas'
ana = float(input('Quanto gastou Ana? '))
bia = float(input('Quanto gastou Bia? '))
total = ana + bia
print('Total de gastos: R$ %s' % total)
media = total/2
print('Gastos por pessoa: R$ %s' % media)
if ana < media :
    diferenca = media - ana
    print('Ana deve pagar: R$ %s' % diferenca)
elif bia < media: # modificado do else para elif
    diferenca = media - bia
    print('Bia deve pagar: R$ %s' % diferenca)
else:
    print('Ana e bia gastaram a mesma quantia.') #nova linha do prototipo