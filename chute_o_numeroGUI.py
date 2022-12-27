import random
import PySimpleGUI as sg    

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_maximo = 100
        self.valor_minimo = 1  
        self.tentar_novamente = True
    
    def Iniciar(self):
        self.layout = [
            [sg.Text('Seu chute', size=(20,0))],
            [sg.Input(size=(18,0), key='ValorChute')],
            [sg.Button('Chutar!')],
            [sg.Output(size=(39,10))]
        ]
        self.janela = sg.Window('Chute o numero', layout=self.layout)

        self.GerarNumeroAleatorio()
        
        try:
            while True:
                self.evento, self.valores = self.janela.Read()
                self.valor_do_chute = self.valores['ValorChute']
                if self.evento == 'Chutar!':
                    while self.tentar_novamente == True:
                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            print('Chute um valor mais baixo')  
                            
                            break   
                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print('chute um valor mais alto')
                            
                            break
                        if int(self.valor_do_chute) == self.valor_aleatorio:
                            self.tentar_novamente = False
                            print('Parabens voce acertou!')
                            break
        except:
            print("Valor digitado não é valido")
            self.Iniciar()
            

    



    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)

chute = ChuteONumero()
chute.Iniciar()