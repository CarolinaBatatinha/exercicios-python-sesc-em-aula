#Criar calculadora com as operações matemáticas básicas: 
from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["pady"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["pady"] = 20
        self.quintoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Calculadora")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.limpa = Button(self.segundoContainer)
        self.limpa["text"] = "C"
        self.limpa["font"] = ("Calibri", "8")
        self.limpa["width"] = 5
        self.limpa["height"] = 2
        self.limpa["command"] = self.dividir #########
        self.limpa.pack(side=LEFT)
        
        self.soma = Button(self.segundoContainer, text="")
        self.soma["text"] = "+"
        self.soma["font"] = ("Calibri", "8")
        self.soma["width"] = 5
        self.soma["height"] = 2
        self.soma["command"] = self.somar
        self.soma.pack(side=LEFT)

        self.subtrai = Button(self.segundoContainer)
        self.subtrai["text"] = "-"
        self.subtrai["font"] = ("Calibri", "8")
        self.subtrai["width"] = 5
        self.subtrai["height"] = 2
        self.subtrai["command"] = self.subtrair
        self.subtrai.pack(side=LEFT)
        
        self.multiplica = Button(self.segundoContainer)
        self.multiplica["text"] = "x"
        self.multiplica["font"] = ("Calibri", "8")
        self.multiplica["width"] = 5
        self.multiplica["height"] = 2
        self.multiplica["command"] = self.multiplicar
        self.multiplica.pack(side=LEFT)
        
        self.divide = Button(self.segundoContainer)
        self.divide["text"] = "÷"
        self.divide["font"] = ("Calibri", "8")
        self.divide["width"] = 5
        self.divide["height"] = 2
        self.divide["command"] = self.dividir
        self.divide.pack(side=LEFT)

        self.iguala = Button(self.segundoContainer)
        self.iguala["text"] = "="
        self.iguala["font"] = ("Calibri", "8")
        self.iguala["width"] = 5
        self.iguala["height"] = 2
        self.iguala["command"] = self.dividir #############
        self.iguala.pack(side=LEFT)

        self.um = Button(self.terceiroContainer)
        self.um["text"] = "1"
        self.um["font"] = ("Calibri", "8")
        self.um["width"] = 5
        self.um["height"] = 2
        self.um["command"] = self.dividir ################
        self.um.pack(side=LEFT)

        self.dois = Button(self.terceiroContainer)
        self.dois["text"] = "2"
        self.dois["font"] = ("Calibri", "8")
        self.dois["width"] = 5
        self.dois["height"] = 2
        self.dois["command"] = self.dividir
        self.dois.pack(side=LEFT)

        self.tres = Button(self.terceiroContainer)
        self.tres["text"] = "3"
        self.tres["font"] = ("Calibri", "8")
        self.tres["width"] = 5
        self.tres["height"] = 2
        self.tres["command"] = self.dividir
        self.tres.pack(side=LEFT)

        self.quatro = Button(self.terceiroContainer)
        self.quatro["text"] = "4"
        self.quatro["font"] = ("Calibri", "8")
        self.quatro["width"] = 5
        self.quatro["height"] = 2
        self.quatro["command"] = self.dividir
        self.quatro.pack(side=LEFT)

        self.cinco = Button(self.terceiroContainer)
        self.cinco["text"] = "5"
        self.cinco["font"] = ("Calibri", "8")
        self.cinco["width"] = 5
        self.cinco["height"] = 2
        self.cinco["command"] = self.dividir
        self.cinco.pack(side=LEFT)
        
        self.seis = Button(self.quartoContainer)
        self.seis["text"] = "6"
        self.seis["font"] = ("Calibri", "8")
        self.seis["width"] = 5
        self.seis["height"] = 2
        self.seis["command"] = self.dividir
        self.seis.pack(side=LEFT)

        self.sete = Button(self.quartoContainer)
        self.sete["text"] = "7"
        self.sete["font"] = ("Calibri", "8")
        self.sete["width"] = 5
        self.sete["height"] = 2
        self.sete["command"] = self.dividir
        self.sete.pack(side=LEFT)

        self.oito = Button(self.quartoContainer)
        self.oito["text"] = "8"
        self.oito["font"] = ("Calibri", "8")
        self.oito["width"] = 5
        self.oito["height"] = 2
        self.oito["command"] = self.dividir
        self.oito.pack(side=LEFT)

        self.nove = Button(self.quartoContainer)
        self.nove["text"] = "9"
        self.nove["font"] = ("Calibri", "8")
        self.nove["width"] = 5
        self.nove["height"] = 2
        self.nove["command"] = self.dividir
        self.nove.pack(side=LEFT)

        self.zero = Button(self.quartoContainer)
        self.zero["text"] = "0"
        self.zero["font"] = ("Calibri", "8")
        self.zero["width"] = 5
        self.zero["height"] = 2
        self.zero["command"] = self.dividir
        self.zero.pack(side=LEFT)

        #AQUI VEM A LINHA DE TEXTO QUE MOSTRARÁ O RESULTADO
        self.mensagem = Label(self.quintoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    #Método verificar senha
    # def verificaSenha(self):
    #     usuario = self.nome.get()
    #     senha = self.senha.get()
    #     if usuario == "123" and senha == "123":
    #         self.mensagem["text"] = "Autenticado"
    #     else:
    #         self.mensagem["text"] = "Erro na autenticação"

    def somar(self):
        n1=int(self.valor1.get()) # pega o primeiro valor
        n2=int(self.valor2.get()) # pega o segundo valor
        self.mensagem["text"] = n1 + n2 # operação realizada

    def subtrair(self):
        n1=int(self.valor1.get())
        n2=int(self.valor2.get())
        self.mensagem["text"] = n1 - n2
    
    def multiplicar(self):
        n1=int(self.valor1.get())
        n2=int(self.valor2.get())
        self.mensagem["text"] = n1 * n2
        
    def dividir(self):
        n1=int(self.valor1.get())
        n2=int(self.valor2.get())
        self.mensagem["text"] = n1 / n2

root = Tk()
Application(root)
root.mainloop()