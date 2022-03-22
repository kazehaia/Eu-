#jogo teste

from math import sqrt

x = 500. #altitude
v = -50. #velocidade/s
g = -5. #aceleracao gravitacional
t = 1. #tempo por partida
gasolina = 120. #combustivel

print(' ')
print('simulacao teste')
print(' ')
print(input('digite a quantidade de gasolina: '))

fmt = 'Alt: %6.2f Vel: %6.2f gasolina: %3d'
while x > 0:    #enquanto nao encosta no chao
    msg = fmt % (x, v, gasolina) #mensagem
    if gasolina > 0:    #ainda temos gasolina
        resp = input(msg + 'queima = ')
        try:    #convert a resposta em numero
            queima = float(resp)
        except:     #a resposta nao era um numero
            queima = 0
        if queima > gasolina:   #queimou mais do que tinha
            queima = gasolina   #entao queima o que tem
        gasolina = gasolina - queima    #subtrai queimado
        a = g + queima  #acel = gravidade + queima da gasolina
    else:
        print ("msg")   #mensagem vazia
        a = g   #aceleracao = gravidade
    x0 = x      #armazenar posicao inicial
    v0 = v      #armazenar valocidade inicial
    x = x0 + v0*t + a*t*t/2     #calc. nova posicao
    x = v0 + a*t        #calc. nova velocidade

    #se o loop acabou, tocara o solo (x <= 0)
    vf = sqrt(v0*v0 + 2*-a*x0)      #calcular vel. final
    print('>>>CONTATO! Velocidade final: %6.2f' % (-vf))

    #avaliar o pouso de acordo com a velocidade
if vf == 0:
    msg = 'Perfeito!'
elif vf <= 2:
    msg ='dentro do padrao'
elif vf <= 10:
    msg = 'avarias leves'
elif vf <= 20:
    msg = 'avarias fortes'
else:
    msg = 'modulo lunar destruido no impacto'
    print('>>>' + msg)