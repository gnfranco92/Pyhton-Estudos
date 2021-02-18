args=(1,2,3)
Kwargs={'nome':'Gui', 'sobrenome':'Neto'}
print("Exemplo de justa posição e nomeado")
print(args,"\n",Kwargs)
print("--"*30)

somar=[]
import time

print("Exemplo de função (soma)\n Digite 0 para sair!")
while args !=0:
    args=int(input("Digite o Valor: "))
    if args != 0:
        somar.append(args)
print(somar)
soma=0  #IMPORTANTE! DECLARAR A VARIAVEL
for args in somar:       #NÃO CONSEGUI FAZER FUNÇÃO DEF
    soma += args
print(soma)

print("--"*30)
# #NÃO CONSIGO CRIAR FUNÇÃO

# print ("Estudar função")
# def somatoria (*argsoma)
#     aux=0
#    for valor in argsoma:
#         aux += valor
#         return aux

# somatoria(2,4) 

print("--"*30)