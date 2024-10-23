# Crie um programa que o usuário digita o seu nome e retorna no número de caracteres
# nome = input('Qual seu nome? ')
# tamanho = len(nome)
# print(tamanho)

# Crie um programa que o usuário digita dois valores e retorna a soma deles
# valor1 = int(input('Qual o primeito valor? '))
# valor2 = int(input('Qual o segundo valor? '))

# soma = valor1 + valor2
# print(soma)

#  Faça um programa que peça o nome, salário e porcentagem de bônus de um funcionário
#  e depois calcula 1000 + (salário * porcentagem de bônus)/ 100

nome = input('Qual seu nome? ')
salario = float(input('Qual o seu salário? '))
porcentagem = float(input('Qual a porcentagem de bônus? '))

bonus = 1000 + (salario * porcentagem)/100

print("Nome: ", nome, "\nSalário: ", salario, "\nPorcentagem: ", porcentagem, "\nBônus: ", bonus)