# Variáveis numéricas
numero_inteiro = int(input("Digite um número inteiro: "))
numero_decimal = float(input("Digite um número decimal: "))

# Variáveis de texto (strings)
nome = str(input("Digite seu nome: "))

# Variáveis booleanas
input_booleano = bool(input("Digite True ou False para a variável verdadeiro: "))

# Exibir os valores inseridos
print("Valores inseridos:")
print("Número inteiro:", numero_inteiro)
print("Número decimal:", numero_decimal)
print("Nome:", nome)
print("Booleano:", input_booleano)

# Ou podemos inserir prints FORMATADOS da seguinte forma:
print(f"Valores inseridos:")
print(f"Número inteiro: {numero_inteiro}")
print(f"Número decimal: {numero_decimal}")
print(f"Nome: {nome}")
print(f"Booleano: {input_booleano}")