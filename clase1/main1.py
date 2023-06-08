a=5
b=1 #antes 0
try:
    a/b
    d = 2 + "Hola"
except ZeroDivisionError as e:
    print("Division entre 0")
except TypeError:
    print("Error en el tipo de dato")
except Exception as e:
    print("Error", e)
else:
    print("No ha ocurrido ninguna excepcion")

finally:
    print("Fin (bloque se ejecuta siempre)")


#Tambien se puede
# except(ZeroDivisionError, TypeError):