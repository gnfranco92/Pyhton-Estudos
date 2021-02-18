# Exemplo de sortes
# s = ["Guilherme", "Banana"]
# nome_ordenado = sorted(s)

#s = ["Guilherme", "Banana"]
# s = "Guilherme"
# # print(s)
# print ("Quantidade de caracteres = ", len(s))

# Relembrando
# i=0 

# while i <  len(s):
#     print(s[i])
#     i += 1

#---------------FUNCIONANDO SEM A FUNÇÃO ---------------------------------
s = "banana"
caracter_ordenados = sorted(s)
print ("Ordenando os caracteres =  ", caracter_ordenados)
caracter_anterior = caracter_ordenados[0]
print ("Caracter anterior = ", caracter_anterior)
contagem = 1

for caracter in caracter_ordenados[1:]:
    if caracter == caracter_anterior:
        contagem += 1
    else:
        print(f"{caracter_anterior} : {contagem}")
        caracter_anterior = caracter
        contagem = 1
    
print(f"{caracter_anterior} : {contagem}")

#-------------------------------------------------------------------------------------
# print("----"*30)

# def ordenar(s):
#     ord = sorted(s)
#     ant = ord [0]
#     cont = 1
#     return ord

# print(ordenar("banana"))

# print("----"*30)

#-------------------------------------------------------------------------------------

# from collections import Counter

# s = 'banana'

# contar = Counter(s)

# print(contar)

#---------------UTILIZANDO A FUNÇÃO ---------------------------------

def contar (s):
    ordenar = sorted(set(s))
    for letras in ordenar:
        print(f'{letras} : {s.count(letras)}')

contar('banana')

def contar_caracter(s):
    
    caracter_ordenados = sorted(s)
    caracter_anterior = caracter_ordenados[0]
    contagem = 1

    for caracter in caracter_ordenados[1:]:
        if caracter == caracter_anterior:
            contagem += 1
        else:
            print (f'{caracter_anterior} : {contagem}')
            caracter_anterior = caracter
            contagem = 1
    print (f'{caracter_anterior} : {contagem}')

contar_caracter('banana')