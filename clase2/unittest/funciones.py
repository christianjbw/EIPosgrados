#Christian Briceno Weiss

def add(x, y):
    #Add function
    return x + y

def substract(x, y):
    #Substract function
    return x - y

def multiply(x, y):
    #Multiply function
    return x * y

def divide(x, y):
    #Divide function
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y

def raised(x, y):
    #Power function
    return x ** y