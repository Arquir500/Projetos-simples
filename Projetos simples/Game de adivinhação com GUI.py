from tkinter import *


def inicio():
    global primeiraPergunta1
    global primeiraResposta
    global botaoEnviar
    global comeco

    comeco = Label(janela, text="Vamos começar! :)")
    comeco.pack()

    primeiraPergunta1 = Label(janela, text="Qual a Segunda moeda mais valorizada do mundo?")
    primeiraPergunta1.pack()

    primeiraResposta = Entry()
    primeiraResposta.pack()

    botaoEnviar = Button(janela, text="enviar", command=checar_resposta1)
    botaoEnviar.pack()

    primeiro_resultado = Label(janela, text='')
    primeiro_resultado.place(x=2000, y=1000)

    botaoSim.destroy()


def saindo():
    quit()


def checar_resposta1(janela):
    global segundaResposta
    global segundaPergunta
    global botaoEnviar2

    resposta = primeiraResposta.get()
    if resposta == "euro":
        resposta_certa1 = Label(janela, text="Correto!")
        resposta_certa1.pack()

    else:
        resposta_errada1 = Label(janela, text="Errou")
        resposta_errada1.pack()

    primeiraPergunta1.destroy()
    primeiraResposta.destroy()
    botaoEnviar.destroy()
    comeco.destroy()

    segundaPergunta = Label(janela, text="Qual é o maior planeta do sistema solar?")
    segundaPergunta.pack()

    segundaResposta = Entry(janela)
    segundaResposta.pack()

    botaoEnviar2 = Button(janela, text="enviar", command=checar_resposta2)
    botaoEnviar2.pack()


def checar_resposta2():
    resposta2 = segundaResposta.get()
    if resposta2 == "júpiter":
        resposta_certa2 = Label(janela, text="Correto!")
        resposta_certa2.pack()

    else:
        resposta_errada2 = Label(janela, text="Errou!")
        resposta_errada2.pack()

    prosseguirbotao2 = Button(janela, text="GO!", command=fimdo_jogo)
    prosseguirbotao2.pack()

    fim = Label(janela, text="Obrigado por jogar!")
    fim.pack()

    segundaPergunta.destroy()
    segundaResposta.destroy()
    botaoEnviar2.destroy()

def fimdo_jogo():

    fimf = Button(janela, text="fim!", command=quit())
    fimf.pack()


janela = Tk()
janela.geometry('360x360')
janela.title("Jogo de Adivinhação")
janela.config(background="#2e1230")

boasVindas = Label(janela, text="Bem vindo ao Jogo de Adivinhação!", font=('Arial', 12, 'bold'), fg='green', bg='black')
boasVindas.pack()


startGame = Label(janela, text="Quer jogar?", font=('Arial', 12, 'bold'), fg='green', bg='black')
startGame.pack()
botaoSim = Button(janela, text="Sim", command=inicio,)
botaoSim.place(x=160, y=55)
botaoNao = Button(janela, text="Sair", command=saindo,)
botaoNao.place(x=300, y=280)


janela.mainloop()
