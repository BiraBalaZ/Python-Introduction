# Setar Tuplas, Listas e Dicionários vazios
tupla_vazia = ()
lista_vazia = []
dicionario_vazio = {}

# Tupla: uma coleção ordenada e imutável de elementos
tupla_valores = (10, 20, 30)  # Exemplo de tupla de valores

# As tuplas são úteis quando você precisa de uma coleção de valores que não deve ser modificada.
# Por serem imutáveis, as tuplas são mais eficientes em termos de memória e podem ser usadas como chaves em dicionários, por exemplo.

# Lista: uma coleção ordenada e mutável de elementos
lista_numeros = [1, 2, 3, 4, 5]  # Exemplo de lista de números
lista_nomes = ["João", "Maria", "José"]  # Exemplo de lista de nomes

# As listas são extremamente versáteis e podem ser usadas para armazenar uma coleção de elementos mutáveis.
# Você pode adicionar, remover e modificar elementos em uma lista conforme necessário, tornando-as ideais para situações onde os dados precisam ser alterados.

# Dicionário: uma coleção não ordenada de pares chave-valor
dicionario_pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}  # Exemplo de dicionário representando uma pessoa

# Os dicionários são úteis quando você precisa armazenar dados que estão relacionados uns aos outros em pares chave-valor.
# Eles fornecem acesso rápido aos valores por meio de chaves únicas e podem ser facilmente modificados, expandidos e manipulados.
# Os dicionários são eficientes para pesquisas de dados por chave.

# Adicionando e removendo itens da tupla
# As tuplas são imutáveis, então não é possível adicionar ou remover itens diretamente.
# No entanto, você pode criar uma nova tupla combinando duas ou mais tuplas.
nova_tupla_valores = tupla_valores + (40,)  # Adicionando um novo valor à tupla
print("Nova tupla de valores:", nova_tupla_valores)

# Removendo um item específico da lista
lista_numeros.remove(3)  # Removendo o valor 3 da lista de números
print("Lista de números após remoção:", lista_numeros)

# Adicionando um novo item à lista usando .append()
lista_nomes.append("Ana")  # Adicionando o nome "Ana" à lista de nomes
print("Lista de nomes após adição:", lista_nomes)

# Adicionando e removendo itens do dicionário
dicionario_pessoa["profissão"] = "Engenheiro"  # Adicionando um novo item ao dicionário
print(f"Dicionário de pessoa após adição: {dicionario_pessoa}")

del dicionario_pessoa["cidade"]  # Removendo um item do dicionário
print("Dicionário de pessoa após remoção: {}".format(dicionario_pessoa))

# Printando itens em uma Tupla
print(f"Itens na tupla: {tupla_valores}")

# Printando itens em uma Lista
print("Itens na lista de números: {}".format(lista_numeros))
print(f"Itens na lista de nomes: {lista_nomes}")

# Printando itens em um Dicionário
print("Itens no dicionário de pessoa: {}".format(dicionario_pessoa))
