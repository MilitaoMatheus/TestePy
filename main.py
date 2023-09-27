'''
print ("Digite seu nome")

# sempre algo vier do teclado, o input será utilizado, já que ele recebe o que esá sendo escrito
nome = input(">> ")
print ("Olá, "+nome+"!")
print ("Bemm vindo ao pyCharm")

#Função de adição

def soma():
    try:
        num1 = float(input(">> Digite o primeiro número:"))
        num2 = float(input(">> Digite o segundo número:"))
        result = num1 + num2
        print("A soma é: ", result)
    except ValueError:
        print("Certifique que digitou números válidos")
        
soma()
'''

#calculadora
# Função para adição
def soma(x, y):
    return x + y

# Função para subtração
def subtracao(x, y):
    return x - y

# Função para multiplicação
def multiplicacao(x, y):
    return x * y

# Função para divisão
def divisao(x, y):
    if y == 0:
        return "Erro: Divisão por zero"
    return x / y

# Função principal
def calculadora():
    while True:
        print("Opções de operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        escolha = input("Escolha a operação desejada (1/2/3/4/5): ")

        if escolha == '5':
            print("Encerrando a calculadora.")
            break

        if escolha in ('1', '2', '3', '4'):
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                print("Resultado:", soma(num1, num2))

            elif escolha == '2':
                print("Resultado:", subtracao(num1, num2))

            elif escolha == '3':
                print("Resultado:", multiplicacao(num1, num2))

            elif escolha == '4':
                print("Resultado:", divisao(num1, num2))
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

calculadora()
