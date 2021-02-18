""" Exemplo da live PythonPro
Construir função, receber parametro n do tipo inteiro, imprimir de 1 até n.
Quando for divisivel por 2, imprimir 'fizz'
Quando for divisivel por 3, imprimir 'buzz'
Quando for divisel por 2 e 3, imprirmir 'fizz_buzz'

"""

# def fizz_buzz(n:int):

#     """
#     doctest
#     >>> fizz_buzz(6)
#     1
#     fizz
#     buzz
#     fizz
#     5
#     fizzbuzz
    
#     """
#     for 1 in range(n):
#         print(n)

# fizz_buzz('5')

n = int(input("Digite o valor: ", ))

for i in range(1,n+1): # 1...i
     print(i)          #1 ...i
        
print("---"*30)

n = int(input("Digite o valor: ", ))

for i in range(1, n +1): # i = 1; n= valor digitado
    if i%2 == 0 and i%3 == 0:
        print("fizz_buzz")
    elif i%2 == 0:
        print("fizz")
    elif i%3 == 0:
        print("buzz")
    else:
        print(i)

print("---"*30)

#----------------- Utilizando lista ------------
n = int(input("Digite o valor: ", ))

for i in n(1, n +1):
    lista = ''

    if i%2 == 0:
        lista = 'fizz'
    if i%3 == 0:
        lista = 'buzz'
    
    print(lista if lista != ''else i)