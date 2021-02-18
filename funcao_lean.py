import time
print("Digite 0 para sair!")
lista=[]
num=1
while num!= 0:
    num=int(input("Digite o número: ", ))
    if num != 0:
        lista.append(num)
print(lista)
soma=0
for num in lista:
    soma += num
media=soma/len(lista)
print("Quantade de números digistados:", len(lista), "Soma:",soma, "Média:",media)    
input()