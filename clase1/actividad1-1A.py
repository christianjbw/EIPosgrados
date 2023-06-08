#Christian Briceno Weiss

#Primera pregunta
#A
try:
    numero = int(input("Introduce un numero: "))

except ValueError:
    print("Error en el tipo de dato. Debe ser un numero entero.")
    numero = int(input("Introduce un numero: "))

except Exception as e:
    print("Error", e)
    numero = int(input("Introduce un numero entero: "))
    
else:
    print("No ha ocurrido ninguna excepcion")

finally:
    print(f"El numero introducido es {numero}.")