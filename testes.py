
try:
    numero_01 = int(input("insira um número inteiro: "))
    numero_02 = int(input("insira outro número inteiro: "))
    numero_03 = int(input("insira mais um número inteiro: "))
    resultado = numero_01 // numero_02 + numero_03
    print(resultado)
except:
    print("integer division or modulo by zero")

else:
    print("tudo ocorreu bem")

finally:
    print("o importante é participar")
    
    







