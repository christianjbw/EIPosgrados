#Uso para documentacion interna de Python

def my_function():
    '''Demonstrates triple double quotes
    docstrings and does nothing really.'''
    
    return None

#Empezar con letra mayuscula y terminar con punto

print(my_function.__doc__)

help(my_function)