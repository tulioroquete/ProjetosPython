#Simulador de Dado
#simular o uso de um dado gerando valor aleatorio de 1 até 6

import random

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado?'
    
    def Iniciar(self):
        resposta = input(self.mensagem)
        try:
            if resposta == 'sim' or resposta == 's':
                self.GerarValorDado()
            elif resposta == 'nao' or resposta == 'n':
                print('OK, obrigado pela participação!')
            else:
                print('favor digitar Sim ou Nao')
        except:
            print('Ocorreu um erro ao receber sua resposta')

    def GerarValorDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()

