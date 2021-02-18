""" Exemplo
contar('banana')
{'a': 3 , 'b' = 1, 'n' = 2}

"""
# def contar_caracter(s):
    
#     caracter_ordenados = sorted(s)
#     caracter_anterior = caracter_ordenados[0]
#     contagem = 1
#     resultado = {}     # Diferença da lista, adicionado resultado = {}

#     for caracter in caracter_ordenados[1:]:
#         if caracter == caracter_anterior:
#             contagem += 1
#         else:
#             resultado [caracter_anterior] = contagem  # Diferença da lista, retirado o print (f'{caracter_anterior} : {contagem}')
#             caracter_anterior = caracter
#             contagem = 1
#     resultado [caracter_anterior] = contagem  # Diferença da lista, retirado o print (f'{caracter_anterior} : {contagem}')
#     return resultado    # Diferença da listqa, adicionado o return

# if __name__ == "__main__":
#     print(contar_caracter('banana'))

# -------------Incrementando direto no dicionário ----------

def contar_caracter(s):
    
    resultado = {}     # Diferença da lista, adicionado resultado = {}

    for caracter in s:
        # contagem = resultado.get(caracter, 0 )   # Função .get (valor chave, valor default (caso o chave não exister retorna o default))
        # contagem += 1
        # resultado [caracter] = contagem
        resultado[caracter] = resultado.get (caracter, 0) + 1 # Sem utilizar a variavel auxiliar "contagem"
    return resultado    # Diferença da lista, adicionado o return

if __name__ == "__main__":
    print(contar_caracter(sorted('banana')))