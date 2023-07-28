from matplotlib import pyplot

# Dados (cotações diárias das ações)
dias = list(range(1, 13)) # criando um vetor com 12 elementos
vale5 = [82.5, 79.8, 54.8, 77.9, 91.6, 83.1, 79.2, 48.8, 54.8, 56.5, 87.5, 94.5]
unip6 = [81.5, 71.8, 91.8, 78.9, 91.2, 85.1, 79.1, 45.8, 64.8, 51.5, 67.5, 91.5]
bbas3 = [72.5, 79.2, 77.8, 65.9, 80.6, 93.1, 85.2, 75.8, 54.8, 76.5, 77.5, 64.5]

# Criar figura e eixos 
fig, ax = pyplot.subplots()

#Plotar os dados
ax.plot(dias, vale5, label = 'VALE5')
ax.plot(dias, unip6, label = 'UNIP6')
ax.plot(dias, bbas3, label = 'BBAS3')

# Mostrar os rótulos dos eixos e a legenda do gráfico
ax.set_xlabel('Dia')
ax.set_ylabel('Preço (R$)')
ax.legend()

# Exibir o gráfico pronto
pyplot.show()
