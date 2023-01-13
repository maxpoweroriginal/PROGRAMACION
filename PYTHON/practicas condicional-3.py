print("Asignaturas optativas 2023")
print("Asignaturas Optativas: Informatica Grafica - Pruebas de Software - Usabilidad y Accesibilidad")
opcion=input("Escriba la asignatura escogida: ")

asignatura=opcion.lower()

if asignatura in ("Informatica Grafica", "Pruebas de Software", "Usabilidad y Accesibilidad"):

	print("Asignatura elegida " + asignatura)

else:
	
	print("La asignatura elegida no esta listada")		 