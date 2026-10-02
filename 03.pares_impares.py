quantidade = int(input("Qual a quantidade:"))
par_impar = input("O número é par/impar:")

contador = 1

while (contador <= quantidade):
     resultado = quantidade * par_impar
     print(f"{quantidade} X {par_impar} = {resultado}")
     break