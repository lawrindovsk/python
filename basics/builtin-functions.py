#abs() -> retornar o valor absoluto do número
abs(-9)
#resposta: 9.

#min() -> retorna o valor minimo de uma saequencia
min(5,6,7,4,8,9,10)
#resposta: 4.

#max() -> retorna o valor máximo de uma sequencia
max(10,2,4,6,8,21,5)
#resposta: 21.

#sum() -> faz a soma dos valores de uma sequencia
somaTotal=sum([5,6,7,8,10,25,5])
print(somaTotal) #print: 66

#pow() -> exponenciação
print(2**3)
#ou
pow(2,3)
#resultado: 8

#print() -> output de alguma coisa 
print("alguma coisa")

#input() -> lê um valor digitado no teclado pelo usuário
nome=input("Qual o seu nome?:") # Cria uma váriavel, e da input com o dado que o user informar.
print(nome) #exibe o dado digitado pelo user.

#help() -> descreve a s funcionalidades de uma determinada função.
help(sum)
#reposta:
# # Help on built-in function sum in module builtins:
# #sum(iterable, /, start=0)
#     Return the sum of a 'start' value (default: 0) plus an iterable of numbers

#     When the iterable is empty, return the start value.
#     This function is intended specifically for use with numeric values and may
#     reject non-numeric types.
