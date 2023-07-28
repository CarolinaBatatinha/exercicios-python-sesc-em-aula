from operacoesMatematicas import *

### execução da entrada de dados ###

valor1 = int(input('Digite o primeiro número: '))
valor2 = int(input('Digite o segundo número: '))

print('\nA soma dos números é {0}.'.format(somar(valor1, valor2)))
print('A subtração dos números é {0}.'.format(subtrair(valor1, valor2)))
print('A multiplicação dos números é {0}.'.format(multiplicar(valor1, valor2)))
print('A divisão dos números é {0}.'.format(dividir(valor1, valor2)))

### ((valor1 + valor2)* 4/2)
result1 = somar(valor1, valor2)
result2 = multiplicar(result1, 4)
result3 = dividir(result2, 2)

print('O resultado da operação ((valor1 + valor2)* 4/2) é igual a {0}.'.format(result3))
continha = dividir(multiplicar(somar(valor1, valor2), 4), 2)
print(continha)

### (valor1 * valor1) + (valor2 * valor2)
res = somar(multiplicar(valor1, valor1), multiplicar(valor2, valor2))
print('O resultado da operação é igual a {0}.'.format(res))
print(f'O resultado da operação é igual a {res}.')
