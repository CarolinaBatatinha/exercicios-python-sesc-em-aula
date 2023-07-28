from matplotlib import pyplot

# Dados em uma lista
rotulos = ['Maçãs', 'Laranjas', 'Bananas', 'Uvas', 'Figos']
tamanho = [25, 30, 20, 25, 27]
cores = ['red', 'orange', 'yellow', 'purple', 'green']

# Criar uma figura e os eixos
fig, ax = pyplot.subplots()

# Criar o gráfico de barras
ax.pie(tamanho, labels = rotulos, colors = cores, autopct='%1.1f%%')

# Adicionar título 
ax.set_title('Distribuição das frutas')

# Exibir a gráfico
pyplot.show()
