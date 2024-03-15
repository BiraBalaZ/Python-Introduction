# Mas também podemos colocar tudo no mesmo print
nome = "João"   # str
idade = 30      # int
altura = 1.75   # float
vivo = True     # bool

# Utilizando vírgula para separar variáveis
print("Nome:", nome, "Idade:", idade, "Altura:", altura, "Vivo:", vivo)

# Utilizando .format()
print("Nome: {} Idade: {} Altura: {} Vivo: {}".format(nome, idade, altura, vivo))

# Utilizando f-string (print(f""))
print(f"Nome: {nome} Idade: {idade} Altura: {altura} Vivo: {vivo}")


# Para pular uma linha, basta inserir um "\n"
print(f'Nome: {nome}\nIdade: {idade}\nAltura: {altura}\nVivo: {vivo}')

# Outro tipo de print, "Extenso (?)" que você pode escrever em mais de uma linha
print(f'''
      Nome: {nome}
      Idade: {idade}
      Altura: {altura}
      Vivo: {vivo}
''')

# Ou também:
print(f'Nome: {nome}', end='')      # Esse "end" faz com que ele junte em uma linha o próximo print
print(f'Idade: {idade}', end='')
print(f'Altura: {altura}', end='')
print(f'Vivo: {vivo}')
