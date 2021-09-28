import requests
from PySimpleGUI import  PySimpleGUI as sg
#layout
lista = []
sg.theme('Reddit')
layout = [
    [sg.Text('CEP'),sg.Input(key='cep',size=(45))],
    [sg.Button('Buscar')],
    [sg.Output(key='resposta',size=(50,15))]
]
#janela
janela = sg.Window('Busca Cep',layout)
#ler eventos
while True:
    try:
        eventos,valores = janela.read()
        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == 'Buscar':
            link = f'''https://cep.awesomeapi.com.br/json/{valores['cep']}'''
            requisicao = requests.get(link)
            resposta = requisicao.json()
            rua = resposta['address']
            cidade = resposta['city']
            estado = resposta['state']
            bairro = resposta['district']
            ddd = resposta['ddd']
            informacoes = [f'''
            cidade:{cidade}
            estado:{estado}
            bairro:{bairro}
            rua:{rua}
            ddd:{ddd} 
    ''']
            lista = informacoes
            valores['resposta'] = lista
            for item in lista:
                print(item)
    except:
        valores['resposta'] = 'erro , entre em contato com o desenvolvedor'
        print('erro , entre em contato com o desenvolvedor')
