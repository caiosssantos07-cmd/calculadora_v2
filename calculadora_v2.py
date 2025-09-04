# Variável de controle de saída
saida = ''

# Funções matemáticas
def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    return a / b

# Função principal da calculadora
def calculadora(num1, num2, operacao):
    resultado = None
    
    if operacao in ['+', 'adicao', 'adição']:
        resultado = adicao(num1, num2)
    elif operacao in ['-', 'subtracao', 'subtração']:
        resultado = subtracao(num1, num2)
    elif operacao in ['*', 'multiplicacao', 'multiplicação']:
        resultado = multiplicacao(num1, num2)
    elif operacao in ['/', 'divisao', 'divisão']:
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida"
    
    return resultado

# Loop principal
while saida.lower() != 'n':
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação desejada (+, -, *, / ou nome): ").lower()
        
        resultado = calculadora(num1, num2, operacao)
        print("Resultado da operação:", resultado)
    except ValueError:
        print("Entrada inválida. Digite apenas números válidos.")
    
    saida = input("Deseja continuar? (S/N): ")

print("Programa encerrado.") 
