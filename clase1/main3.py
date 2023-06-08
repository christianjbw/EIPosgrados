#assert

# assert 1==2, "informacion del assert"

def calcular_media(lista):
    return sum(lista)/len(lista)

#assert(calcular_media([5, 5, 5]) == 6) #AssertionError
assert(calcular_media([5, 5, 5]) == 5)


def suma(a, b):
    assert(type(a) == int)
    assert(type(b) == int)
    return a + b

#suma(2, 3.0) #AssertionError
suma(2, 3)

class Mi_1:
    pass
class Mi_2:
    pass

m1 = Mi_1()
m2 = Mi_2()

#assert(isinstance(m1, Mi_2)) #AssertionError
assert(isinstance(m1, Mi_1))

#Para que se salte los assert al ejecutarse desde el Terminal: python -O main.py (o mayuscula)


#Excepcion personalizada 

class miExcepcion(Exception):
    def __init__(self, param1, param2):
        self.mensaje=param1
        self.informacion=param2

try:
    raise miExcepcion("Este es mi mensaje","y aqui la info")
except miExcepcion as ex:
    p1, p2 = ex.args
    print(p1, p2)


print("Fin")

