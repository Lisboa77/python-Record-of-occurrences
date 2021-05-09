from datetime import datetime
from random import randint
from PySimpleGUI import PySimpleGUI as sg

amostras = []
data = datetime.now().strftime('\nDATA : %d - %m -  %Y - HORARIO %H : %M : %S ')
idc = ('\nID DA OCORRÊNCIA : {}'.format(randint(1515151,511581516)))
esp = ('\n.'*2)

# Layout
sg.theme('Black')
layout =[
    [sg.Text('Nome do Solicitante : ',size=(15,1)),sg.Input(key='solicitante',size=(30,1))],
    [sg.Text('Cidade da ocorrência : ',size=(15,1)),sg.Input(key='cidade',size=(30,1))],
    [sg.Text('Endereço : ',size=(15,1)),sg.Input(key='endereço',size=(30,1))],
    [sg.Text('Sobre a ocorrência : ',size=(15,1)),sg.Input(key='ocorrencia',size=(30,1))],
    [sg.Button('ENVIAR')],
]
# Janela
janela = sg.Window('Cadastrar Ocorrência',layout)

# Ler Eventos 
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break

    if eventos == 'ENVIAR':
        with open('ocorrencias cadastradas.txt','a') as arquivo:
            for valor in amostras:
                print(valor)  
            arquivo.write(
f"\nNome do Solicitante: {valores['solicitante']} \nCidade : {valores['cidade']} \nEndereço : {valores['endereço']} \nSobre a Ocorrencia : {valores['ocorrencia']}")
            arquivo.write(f'{idc}{data}{esp}')
            break 
