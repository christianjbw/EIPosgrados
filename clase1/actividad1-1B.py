#Christian Briceno Weiss

#Primera pregunta
#B

class miExcepcion(Exception):
    pass

class ValorPequenhoError(miExcepcion):
    pass

while(True):
    try:
        numero = int(input("Introduce un numero: "))
        if numero > 10:
            raise ValorPequenhoError
        break
    
    except ValorPequenhoError:
        print("El numero es mayor a 10, intente nuevamente.")

    except ValueError:
        print("Error en el tipo de dato. Debe ser un numero entero.")

    except Exception as e:
        print("Error", e)
    
print("No ha ocurrido ninguna excepcion")
print(f"El numero introducido es {numero}.")