#Christian Briceno Weiss

#Segunda pregunta

try:
    ruta_archivo = input("Ingrese nombre del archivo txt: ")
    archivo = open(ruta_archivo, 'r')
    print('Archivo encontrado.')
    
except FileNotFoundError:
    ruta_archivo=input("Archivo no encontrado. Ingrese la ruta del archivo txt: ")
    archivo = open(ruta_archivo, 'r')
    print("Archivo encontrado.")

except NameError:
    ruta_archivo=input("Archivo no encontrado. Ingrese la ruta del archivo txt: ")
    archivo = open(ruta_archivo, 'r')
    print("Archivo encontrado.")
    
except Exception as e:
    print("Error", e)

finally:
    print("El contenido del archivo es:")
    print(archivo.read())
    archivo.close()
    print("Programa terminado.")