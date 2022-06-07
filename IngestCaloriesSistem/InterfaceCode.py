from typing import Union, Any

from PySimpleGUI import PySimpleGUI as sg
class TelaCalculadora:
    def __init__(self):
        sg.change_look_and_feel('DarkTeal7')
        #Layout
        layout = [
             [sg.Text('Nome',size=(5,0)),sg.Input(size=(15,0),key='nome')],
             [sg.Text('Idade',size=(5,0)),sg.Input(size=(15,0),key='idade')],
             [sg.Text('Sexo: '),sg.Radio('Masculino','sexo',key='masculino'),sg.Radio('Feminino','sexo',key='feminino')],
             [sg.Text('Altura'), sg.Input(key='altura')],
             [sg.Text('Peso '), sg.Input(key='peso')],
             [sg.Output(30, 20)],
             [sg.Button('Calcular')]
        ]
        #Janela
        self.janela = sg.Window("Calculadora de Caloria").layout(layout)


    def Iniciar(self):
        while True:
            # extrair os dados da tela
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            masculino = self.values['masculino']
            feminino = self.values['feminino']
            altura = self.values['altura']
            peso = self.values['peso']



            if sg.Radio.key == 'masculino':
                calculomasc = 66.5 + (13.75 * peso) + (5.003 * altura) + (6.77 * idade)
                print(f'O resultado diante das opções desejadas é {calculomasc}')

            else:
                calculoFem = 655.1 + (9.56 * peso) + (1.85 * altura) + (4.68 * idade)
                print(calculoFem)


          
tela = TelaCalculadora()
tela.Iniciar()
