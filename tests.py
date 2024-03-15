# O comando assert em Python é usado para verificar se uma determinada expressão é verdadeira.
# Se a expressão for avaliada como falsa, o programa levantará uma exceção do tipo AssertionError, 
# indicando que algo está errado.

# A finalidade principal do comando assert é auxiliar na depuração e teste de código. Ele é frequentemente
# usado para verificar as suposições durante o desenvolvimento de software. Por exemplo, você pode usá-lo
# para garantir que os dados que você está manipulando estão nos formatos corretos, ou que os resultados de
# uma função estão dentro de um intervalo específico.

from time import sleep
from os import system

# Cleaning Terminal
system('cls')

# Declarating initial variables
var1 = 1
var2 = 2
var3 = 3

# Tests
try:
    assert var3 - var2 == var1
except AssertionError as error:
    print(f"var1 = {var1}")
    raise error
sleep(1)
print(f'Primeira variável = {var1}', end=' ')
sleep(1)
print("✓")

try:
    assert var3 - var1 == var2
except AssertionError as error:
    print(f"var2 = {var2}")
    raise error
sleep(1)
print(f'Segunda  variável = {var2}', end=' ')
sleep(1)
print("✓")

try:
    assert var1 + var2 == var3
except AssertionError as error:
    print(f"var3 = {var3}")
    raise error
sleep(1)
print(f'Terceira variável = {var3}', end=' ')
sleep(1)
print("✓")

# End of the tests
sleep(1)
print('The code passed in all tests =D')
sleep(.5)
print('Congratulations!')
