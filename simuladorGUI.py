#Simulador de Dado
#simular o uso de um dado gerando valor aleatorio de 1 até 6

import random
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
       #self.mensagem = 'Você gostaria de gerar um novo valor para o dado?'
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'), sg.Button('nao')]
        ]
        

    def Iniciar(self):
        #criar janela
        self.janela = sg.Window('Simulador de Dado', layout=self.layout)
        #ler valores tela
        self.eventos, self.valores = self.janela.Read()
        
        #resposta = input(self.mensagem)
        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.GerarValorDado()
            elif self.eventos == 'nao' or self.eventos == 'n':
                print('OK, obrigado pela participação!')
            else:
                print('favor digitar Sim ou Nao')
        except:
            print('Ocorreu um erro ao receber sua resposta')

    def GerarValorDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()

