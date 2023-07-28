import random
from tkinter import *
import time

class Application:
    def __init__(self, master=None):
     self.fontePadrao = ("Arial", "15")
     self.primeiroContainer = Frame(master)
     self.primeiroContainer["pady"] = 10
     self.primeiroContainer.pack()

     self.segundoContainer = Frame(master)
     self.segundoContainer["padx"] = 20
     self.segundoContainer.pack()
     
     self.terceiroContainer = Frame(master)
     self.terceiroContainer["padx"] = 20
     self.terceiroContainer.pack()
     
     self.quartoContainer = Frame(master)
     self.quartoContainer["pady"] = 30
     self.quartoContainer.pack()


     self.lblNumeroMaximo =Label(self.primeiroContainer, text="Digite o número de pessoas a serem sorteadas")
     self.lblNumeroMaximo["font"] = ("Arial ", "15", "bold")
     self.lblNumeroMaximo.pack()
 
     self.numeroMaximo = Entry(self.segundoContainer)
     self.numeroMaximo["width"] = 30
     self.numeroMaximo["font"] = self.fontePadrao
     self.numeroMaximo.pack(side=LEFT) 
 
     self.resultado = Label(self.terceiroContainer, text='Resultado:')
     self.resultado["width"] = 40
     self.resultado["font"] = self.fontePadrao
     self.resultado.pack(side=LEFT) 
    
     self.botao = Button(self.quartoContainer, text='ok')  
     self.botao["width"] = 20
     self.botao["font"] = self.fontePadrao
     self.botao["command"] = self.mudarTexto
     self.botao.pack(side=LEFT) 

    def mudarTexto(self):

        ValorNumeroMaximo = int(self.numeroMaximo.get())
        nomes = ['Fernando', 'Emerson', 'Vanderlei', 'Gabriela', 'João', 'Carol', 'Fefê', 'Flávia', 'Paulo', 'Adriano']
        if(ValorNumeroMaximo>len(nomes)):
            self.resultado["text"]="Digite uma quantidade menor"
        else:
            self.resultado["background"] = "red"
            nomes_sorteados = ""
            for p in range(0, ValorNumeroMaximo):
                self.resultado["background"] = "red"
                for c in range(0,10):
                    self.resultado["text"] = nomes[random.randint(0, len(nomes) -1)]
                    self.terceiroContainer.update()
                    time.sleep(0.2)
                self.resultado["background"] = "blue"
                nomes_sorteados += self.resultado["text"] +"\n"
                nomes.remove(self.resultado["text"])
                self.terceiroContainer.update()
                time.sleep(1)
            self.resultado["background"] = "gold"
            self.resultado["text"] = nomes_sorteados
            self.terceiroContainer.update()

root = Tk()
Application(root)
root.mainloop()
