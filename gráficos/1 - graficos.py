from matplotlib import pyplot

eixo_x_grafico1 = [10, 20, 30, 40]
eixo_y_grafico1 = [5, 10, 15, 20]
fig, grafico1 = pyplot.subplots()
grafico1.plot(eixo_x_grafico1, eixo_y_grafico1)
pyplot.show()

# Dados
x = [3, 22, 7, 48]
y = [13, 4, 90, 160]

# Criar uma figura e um eixo
fig, ax = pyplot.subplots()

# Plotar os dados com as personalizações
ax.plot(x, y, color = 'green', linestyle = '--', marker = 'o', label = 'casas')

# Adicionar rótulos e título
ax.set_xlabel('Quantidade de casas')
ax.set_ylabel('Quantidade de pessoas')
ax.set_title('Censo FIT 2023')

# Incluir uma legenda
ax.legend('Ê coisinha!')

# Mostrar o gráfico
pyplot.show()
