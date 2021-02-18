"Módulo para executar as funções matemáticas"

#from matematica import mat
#import matematica.mat
#from matematica.mat import soma
from mat import soma as s           # Chama a função soma com S

print(__name__) # Informa qual o módulo obteve
print (s(4,5))