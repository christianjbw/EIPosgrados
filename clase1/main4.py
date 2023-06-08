class ValorMinimo(Exception):
    
    def __init__(self,mensaje):
        self.mensaje=mensaje

    def __str__(self):
        return "Error de valor minimo: {}".format(self.mensaje)
    


minimo = 20

try:
    numero = int(input("Introduce un numero: "))
    if numero < minimo:
        raise ValorMinimo("Se ha introducido un valor menos a {}".format(minimo))

except ValueError as e:
    print("Introduce un valor numerico")
except ValorMinimo as e:
    print("Error: ", e)
        