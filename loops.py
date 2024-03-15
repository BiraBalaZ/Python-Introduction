# Lista de frutas
frutas = ["maçã", "banana", "laranja", "uva", "morango"]
texto = 'Hello World'
contador = 0

# Loop while para imprimir os números de 1 a 5
while contador <= 5:
    print(contador)
    contador += 1  # Incrementando o contador para evitar um loop infinito

# Loop for para imprimir cada fruta na lista
for fruta in frutas:
    print(fruta)

# Imprimindo cada letra separadamente usando um loop for
for letra in texto:
    print(letra)

for letra in texto:
    print(letra, end=' ')

# Novo loop while que aumenta o contador dentro do número de caracteres da variável texto
while contador < len(texto):
    print(contador)
    contador += 1  # Incrementando o contador até o número de caracteres do texto
