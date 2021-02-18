'''
Exercíco receber string e contar.

>>> contar_letras('guilherme')  # se tiver letra maiuscula considera-la
g: 1
u: 1
i: 1
l: 1
h: 1
e: 2
r: 1
m: 1

and

{'g': 1 , 'u': 1 , 'i': 1 , 'l': 1 , 'h': 1 , 'e': 2 , 'r': 1 , 'm': 1}


'''


#---------Utilizando o Counter-----------
print("---"*15, "Utilizando Counter" , "---"*15)
from collections import Counter

print(Counter('guilherme'))

#-------------------------------------------

#--------Utilizando lista ------------------

print("---"*15, "Utilizando lista" , "---"*15)

def contar_caracter(s:str):

    resultado = {}

    for caracter in s:
        resultado[caracter] = resultado.get (caracter, 0)+1  # Executo primeiro o lado direito, adiciona a letra na lista ou soma se ja existir 
    
    return resultado

if __name__ == "__main__":
    print(contar_caracter(sorted('banana'))) 
