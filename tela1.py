from tkinter import *                       # importa todos os componentes do módulo Tkinter
class Application:
    def __init__(self, master=None):        #INICIALIZA
     self.widget1 = Frame(master)           # cria o primeiro container chamado widget1 e passamos como referência o container pai (chamado widget1).
     self.widget1.pack()                    # informa o gerenciador de geometria pack
     self.msg1 = Label(self.widget1, text=" Texto 1 - Primeiro widget :D ") # cria um widget label para imprimir na tela e informa que o container pai é o widget1 (chamado msg1)/
     self.msg1["font"] = ("Verdana", "10", "italic", "bold")  # altera a fonte do texto da msg1
     self.msg1.pack()                       # informa o gerenciador de geometria pack

     self.btsair = Button(self.widget1)     # cria um widget button (chamado btsair)
     self.btsair["text"] = "Sair"           # altera o texto do botão para Sair
     self.btsair["font"] = ("Calibri", "10") # altera a fonte do texto do botão
     self.btsair["width"] = 5               # altera o tamanho do botão
     self.btsair["command"] = self.widget1.quit # adiciona um comando a ser executado quando o botão for clicado
     self.btsair.pack()                     # informa o gerenciador de geometria pack

     self.msg2 = Label(self.widget1,text="Texto 2 - Primeiro widget")  # cria um widget label para imprimir na tela e informa que o container pai é o widget1 (chamado msg2)
     self.msg2["font"] = ("Arial", "10", "italic")  # altera a fonte do texto da msg1
     self.msg2.pack()  # informamos o gerenciador de geometria pack

     self.btmudar = Button(self.widget1)    # cria um widget button (chamado btmudar)
     self.btmudar["text"] = "Mudar Texto"   # altera o texto do botão para Mudar Texto
     self.btmudar["font"] = ("Arial", "10") # altera a fonte do texto do botão
     self.btmudar["command"] = self.mudarTexto # adiciona um comando a ser executado quando o botão for clicado, chamando a função mudarTexto
     self.btmudar.pack()

    def mudarTexto(self):
        if self.msg2["text"] == "Primeiro widget":  # verifica se o texto do msg2 está escrito "Primeiro widget"
            self.msg2["text"] = "O botão recebeu um clique"  # altera o texto do msg2
        else:
            self.msg2["text"] = "Primeiro widget" # altera o texto do msg2

root = Tk()                                 # instanciamos a classe TK() através da variável root
Application(root)                           # passamos a variável root como parâmetro do método construtor da classe Application
root.mainloop()                             # chamamos o método root.mainloop() para exibirmos a tela