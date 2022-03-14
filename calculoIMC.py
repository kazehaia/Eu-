peso = input ('Digite o seu peso em kg: ')
altura = input ('Digite sua altura em m: ')
imc = float(peso) / ( float(altura) * float (altura) )
if imc <= 17:
	print ('Muito abaixo do peso')
elif imc > 17 and imc < 18.5:
	print ('Abaixo do peso')
elif imc > 18.5 and imc < 25:
	print ('peso normal')
elif imc > 25 and imc < 30:
	print ('Acima do peso')
elif imc > 30 and imc < 35:
	print ('Obesidade I')
elif imc > 35 and imc < 40:
	print ('Obesidade II(severa)')
else:
	print ('Obesidade III(mórbida)')
