from matplotlib import pyplot

# Dados em uma lista

rotulos = ['Maçãs', 'Laranjas', 'Bananas', 'Uvas', 'Figos']
valores = [9, 2, 6, 8, 14]

#XCriar uma figura e os eixos
fig, ax = pyplot.subplots()

# Criar o gráfico de barras
ax.bar(rotulos, valores)

#Inserir rótulos de dados e título do gráfico
ax.set_xlabel('Frutas')
ax.set_ylabel('Preço')
ax.set_title('Média de preços das frutas')

# Exibir a gráfico

pyplot.show()