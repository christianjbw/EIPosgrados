#raise

edad=17
a=1
b=0
try:
    if type(b) != int:
        raise Exception
    else:
        a/b
except Exception:
    print("No es mayor de edad")
    
