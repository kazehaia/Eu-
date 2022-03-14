idade = int (input ('Digite sua idade: '))
if idade >= 0 and idade <= 10:
    print ('Você é criança') 
elif idade >= 10 and idade < 18:
	print ('Você é adolescente')
elif idade >= 18 and idade < 30:
	print ('Você é jovem')
elif idade >= 30 and idade < 40:
	print ('Você é adulto')
elif idade >= 40 and idade <= 100:
	print ('idoso')
else:
	print ('Valor não encontrado!')