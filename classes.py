class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def emitir_som(self):
        pass  # Método não implementado ainda

class Cachorro(Animal):
    def emitir_som(self):
        return "Au Au"
    
# Criando um objeto da classe Animal
animal_generico = Animal("Genérico")

# Criando um objeto da subclasse Cachorro
meu_cachorro = Cachorro("Rex")

# Acessando atributos e métodos dos objetos
print("Nome do animal genérico:", animal_generico.nome)
print("Nome do meu cachorro:", meu_cachorro.nome)
print("Som do meu cachorro:", meu_cachorro.emitir_som())

# __init__ é um método especial em Python usado para inicializar objetos quando
# uma instância de uma classe é criada. É conhecido como o "construtor" da classe.
# O método __init__ é chamado automaticamente quando você cria um novo objeto dessa classe.

# Ele é usado para definir os atributos iniciais do objeto.
# O nome __init__ é uma convenção em Python para indicar que este é o método de inicialização.
# Ele pode aceitar parâmetros que são usados para configurar o objeto no momento da inicialização.

# Por exemplo, na classe Animal do exemplo anterior, o método __init__ é usado para inicializar
# o atributo nome do objeto Animal.

######################################################################################################################################

# self é uma referência ao próprio objeto sendo manipulado. É usado dentro da classe para se referir aos atributos e métodos do próprio objeto.

# Em Python, os métodos de instância devem sempre ter self como seu primeiro parâmetro.
# self não é uma palavra-chave, você pode usar qualquer nome em seu lugar, mas é uma convenção amplamente adotada em Python.

# Por exemplo, na classe Animal, o parâmetro self no método __init__ é usado para referenciar o próprio objeto sendo inicializado.
# Isso permite que você defina e acesse os atributos do objeto dentro do método.