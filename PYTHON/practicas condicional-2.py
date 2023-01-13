print("Programa de Becas 2023")
distancia_escuela=int(input("Ingrese la distancia a la escuela en km "))
print(distancia_escuela)

numero_hermanos=(int(input("Ingrese el numero de hermanos ")))
print(numero_hermanos)

salario_familiar=int(input("Ingrese salario familiar "))
print(salario_familiar)

if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000:

		print("Tienes derecho a Beca")

else:

		print("No obtienes Beca")		