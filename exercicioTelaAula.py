#Criar tela com as operações matemáticas 
from operacoesMatematicas import *
from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
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
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Calculadora")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.valorLabel1 = Label(self.segundoContainer,text="Digite o 1º valor", font=self.fontePadrao)
        self.valorLabel1.pack(side=LEFT)

        self.valor1 = Entry(self.segundoContainer)
        self.valor1["width"] = 5
        self.valor1["font"] = self.fontePadrao
        self.valor1.pack(side=LEFT)

        self.valorLabel2 = Label(self.terceiroContainer, text="Digite o 2º valor", font=self.fontePadrao)
        self.valorLabel2.pack(side=LEFT)

        self.valor2 = Entry(self.terceiroContainer)
        self.valor2["width"] = 5
        self.valor2["font"] = self.fontePadrao
        #self.senha["show"] = "*"
        self.valor2.pack(side=LEFT)

        self.soma = Button(self.quartoContainer)
        self.soma["text"] = "Somar"
        self.soma["font"] = ("Calibri", "8")
        self.soma["width"] = 12
        self.soma["command"] = self.somar
        self.soma.pack()

        self.subtrai = Button(self.quartoContainer)
        self.subtrai["text"] = "Subtrair"
        self.subtrai["font"] = ("Calibri", "8")
        self.subtrai["width"] = 12
        self.subtrai["command"] = self.subtrair
        self.subtrai.pack()
        
        self.multiplica = Button(self.quartoContainer)
        self.multiplica["text"] = "Multiplicar"
        self.multiplica["font"] = ("Calibri", "8")
        self.multiplica["width"] = 12
        self.multiplica["command"] = self.multiplicar
        self.multiplica.pack()
        
        self.divide = Button(self.quartoContainer)
        self.divide["text"] = "Dividir"
        self.divide["font"] = ("Calibri", "8")
        self.divide["width"] = 12
        self.divide["command"] = self.dividir
        self.divide.pack()

        #AQUI VEM A LINHA DE TEXTO QUE MOSTRARÁ O RESULTADO
        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
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