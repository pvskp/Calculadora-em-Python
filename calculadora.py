from tkinter import *
from tkinter import ttk

LARGURA, ALTURA = 320, 300 

BUTTON_WIDTH = 2 # default = 2
BUTTON_HEIGHT = 2 # default = 2
BUTTON_DISTANCE = 55 # default = 55

DISPLAY_WIDTH = 210 # default = 210
DISPLAY_HEIGHT = 40 # default = 40

SECOND_COLOR = '#b70000'

num = str() # inicializa o calculo

def operar(event, display, botao):
    """
    Realiza a operação desejada e mostra ao usuário a operação
    que está sendo realizada.

    Recebe: o 'event' gerado pelo clique no botão, o display da janela principal e a
    banco de dados dos botões.
    Devolve: nada.
    """
    global num
    operacao_atual = botao[event.widget]

    vazio = str()

    if operacao_atual == 'C':
        num = vazio
        display['text'] = vazio

    elif operacao_atual == '=':
        if operacao_atual == vazio:
            display['text'] = vazio
        else:
            display['text'] = eval(num)
            num = vazio
    else:
        num += operacao_atual
        display['text'] = num

def criar_botoes(window, operacoes, botoes, display):
    """
    Cria os botões da calculadora.

    Recebe: a janela principal, a lista de digitos e operações, o banco de dados de botões
    e o objeto 'display' da janela principal.
    Devolve: nada. 
    """

    contador = -1

    for i in range(1,5): # 4 linhas
        for j in range(1,5): # 4 colunas 
            contador += 1
            if contador < len(operacoes):
                b_operacao = Button(window, text=f'{operacoes[contador]}', bg=SECOND_COLOR, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
                b_operacao.place(x=j*BUTTON_DISTANCE, y=i*BUTTON_DISTANCE)
                botoes[b_operacao] = operacoes[contador]
                b_operacao.bind('<Button-1>', lambda event, d = display, b = botoes: operar(event, d, b))
            else:
                break

def banco_de_botoes():
    """
    Inicializa uma pequena base de dados onde ficarão armazenadas as informações de todos
    os botões da calculadora

    Recebe: nada.
    Devolve: um dicionário vazio.
    """

    botoes = {} # dicionario que contém todas as operações da calculadora 

    return botoes

def definir_operandos():
    """
    Define os numeros e operadores que serão utilizados na calculadora.
    
    Recebe: nada.
    Devolve: uma lista com todos os digitos e operações a serem utilizados.
    """
    numeros = [str (x) for x in range(10)] # lista com os numeros de 0 a 9
    operandos = ['+', '-', '*', '/', '=', 'C'] # lista de operações
    operacoes = numeros + operandos # concatena listas de string
    return operacoes

def criar_janela():
    """
    Cria uma janela com um pequeno display.

    Recebe: nada.
    Devolve: o objeto janela e o objeto display.
    """
    janela = Tk()
    janela.title('Calculadora')
    janela.minsize(LARGURA, ALTURA) # minsize = maxsize
    janela.maxsize(LARGURA, ALTURA)

    display = Label(janela, text='', background=SECOND_COLOR, foreground='#fff')
    display.place(x=BUTTON_DISTANCE, y= 10, width=DISPLAY_WIDTH, height=DISPLAY_HEIGHT) 

    return janela, display

def main():
    janela, display = criar_janela()
    operacoes = definir_operandos()
    botoes = banco_de_botoes()
    criar_botoes(janela, operacoes, botoes, display)
    janela.mainloop()

if __name__ == '__main__':
    main()
