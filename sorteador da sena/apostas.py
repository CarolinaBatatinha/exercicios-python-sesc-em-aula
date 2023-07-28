from tkinter import *
import random

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "20", "bold")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer.pack()
        self.texto = Label(self.primeiroContainer, text="Faça sua aposta: ", font=self.fontePadrao)
        self.texto.pack()

        self.aposta1 = Entry(self.primeiroContainer)
        self.aposta1.pack(side=LEFT)
        self.aposta1["width"] = 10
        self.aposta1["font"] = 30
        self.aposta2 = Entry(self.primeiroContainer)
        self.aposta2["width"] = 10
        self.aposta2["font"] = 30
        self.aposta2.pack(side=LEFT)
        self.aposta3 = Entry(self.primeiroContainer)
        self.aposta3["width"] = 10
        self.aposta3["font"] = 30
        self.aposta3.pack(side=LEFT)
        self.aposta4 = Entry(self.primeiroContainer)
        self.aposta4["width"] = 10
        self.aposta4["font"] = 30
        self.aposta4.pack(side=LEFT)
        self.aposta5 = Entry(self.primeiroContainer)
        self.aposta5["width"] = 10
        self.aposta5["font"] = 30
        self.aposta5.pack(side=LEFT)
        self.aposta6 = Entry(self.primeiroContainer)
        self.aposta6["width"] = 10
        self.aposta6["font"] = 30
        self.aposta6.pack(side=LEFT)

        self.jogar = Button(self.primeiroContainer)  # , text="Autenticar", font="Calibri", width = "12")
        self.jogar["text"] = "Apostar"
        self.jogar["font"] = "Calibri"
        self.jogar["width"] = "12"
        self.jogar["command"] = self.verificarJogada
        self.jogar.pack(side=LEFT)

        self.segundoContainer = Frame(master)
        self.segundoContainer.pack()
        self.sorteio1 = Label(self.segundoContainer, text="1", font="self.fontePadrao", width="4")
        self.sorteio1.pack(side=LEFT)
        self.sorteio2 = Label(self.segundoContainer, text="34", font="self.fontePadrao", width="4")
        self.sorteio2.pack(side=LEFT)
        self.sorteio3 = Label(self.segundoContainer, text="34", font="self.fontePadrao", width="4")
        self.sorteio3.pack(side=LEFT)
        self.sorteio4 = Label(self.segundoContainer, text="34", font="self.fontePadrao", width="4")
        self.sorteio4.pack(side=LEFT)
        self.sorteio5 = Label(self.segundoContainer, text="34", font="self.fontePadrao", width="4")
        self.sorteio5.pack(side=LEFT)
        self.sorteio6 = Label(self.segundoContainer, text="34", font="self.fontePadrao", width="4")
        self.sorteio6.pack(side=LEFT)

    def verificarJogada(self):
        num1 = random.randint(1, 60)
        num2 = random.randint(1, 60)
        num3 = random.randint(1, 60)
        num4 = random.randint(1, 60)
        num5 = random.randint(1, 60)
        num6 = random.randint(1, 60)

        self.sorteio1["text"] = num1
        self.sorteio2["text"] = num2
        self.sorteio3["text"] = num3
        self.sorteio4["text"] = num4
        self.sorteio5["text"] = num5    
        self.sorteio6["text"] = num6

        numeroApostado1 = int(self.aposta1.get())
        numeroApostado2 = int(self.aposta2.get())
        numeroApostado3 = int(self.aposta3.get())
        numeroApostado4 = int(self.aposta4.get())
        numeroApostado5 = int(self.aposta5.get())
        numeroApostado6 = int(self.aposta6.get())

        if numeroApostado1 == num1 or numeroApostado1 == num2 or numeroApostado1 == num3 or numeroApostado1 == num4 or numeroApostado1 == num5 or numeroApostado1 == num6:
            self.aposta1["foreground"] = "blue"
        else:
            self.aposta1["foreground"] = "black"

        if numeroApostado2 == num1 or numeroApostado2 == num2 or numeroApostado2 == num3 or numeroApostado2 == num4 or numeroApostado2 == num5 or numeroApostado2 == num6:
            self.aposta2["foreground"] = "blue"
        else:
            self.aposta2["foreground"] = "black"

        if numeroApostado3 == num1 or numeroApostado3 == num2 or numeroApostado3 == num3 or numeroApostado3 == num4 or numeroApostado3 == num5 or numeroApostado3 == num6:
            self.aposta3["foreground"] = "blue"
        else:
            self.aposta3["foreground"] = "black"

        if numeroApostado4 == num1 or numeroApostado4 == num2 or numeroApostado4 == num3 or numeroApostado4 == num4 or numeroApostado4 == num5 or numeroApostado4 == num6:
            self.aposta4["foreground"] = "blue"
        else:
            self.aposta4["foreground"] = "black"

        if numeroApostado5 == num1 or numeroApostado5== num2 or numeroApostado5 == num3 or numeroApostado5 == num4 or numeroApostado5 == num5 or numeroApostado5 == num6:
            self.aposta5["foreground"] = "blue"
        else:
            self.aposta5["foreground"] = "black"

        if numeroApostado6 == num1 or numeroApostado6 == num2 or numeroApostado6 == num3 or numeroApostado6 == num4 or numeroApostado6 == num5 or numeroApostado6 == num6:
            self.aposta6["foreground"] = "blue"
        else:
            self.aposta6["foreground"] = "black"

root = Tk()  # instanciamos a classe TK() através da variável root
root.title("MEGA SENA")
Application(root)  # passamos a variável root como parâmetro do método construtor da classe Application
root.mainloop()  # chamamos o método root.mainloop() para exibirmos a tela
