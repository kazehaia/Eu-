class Empregado:
    'Classe base para empregados'
    contador = 0

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        Empregado.contador += 1
    
    def mostra_contador (self):
        print ("Numero de empregado: %d" % Empregado.contador)
    
    def mostra_empregado (self):
        print ("Nome: ", self.nome, "Salario: ", self.salario)
