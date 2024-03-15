# Função sem parâmetros e sem retorno:
def saudacao():
    print("Olá! Bem-vindo ao mundo das funções.")

# Chamando a função
saudacao()

# Função com parâmetros e retorno:
def soma(a, b):
    return a + b

# Chamando a função e armazenando o resultado em uma variável
resultado = soma(3, 5)
print("Resultado da soma:", resultado)

# Função com parâmetros padrão:
def saudacao(nome="Usuário"):
    print("Olá,", nome, "! Bem-vindo ao mundo das funções.")

# Chamando a função sem especificar um nome
saudacao()

# Chamando a função especificando um nome
saudacao("Maria")

# Função com parâmetros variáveis (args):
def detalhes_pessoa(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

# Chamando a função com diferentes pares chave-valor
detalhes_pessoa(nome="João", idade=30, cidade="São Paulo")
detalhes_pessoa(nome="Maria", idade=25)

# Esses são apenas alguns exemplos simples de funções em Python. 
# Elas podem ser usadas para encapsular blocos de código que executam
# tarefas específicas e podem aceitar diferentes tipos de argumentos e
# retornar valores, conforme necessário.
