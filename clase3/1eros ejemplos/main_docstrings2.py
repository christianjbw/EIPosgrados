class ComplexNumber:
    """
    This is a class for mathematical operations on complex numbers.
    
    Attributes:
        real (int): The real part of complex number. 
        imag (int): The imaginary part of complex number.    
    
    """

def __init__(self, real, imag):
    """
    The constructor for CompleXNumber class. 
    
    Parameters:
        real (int): The real part of complex number. 
        imag (int): The imaginary part of complex number. 
    
    """

    def add(self, num):
        """ 
        The function to add two Complex Numbers. 
        
        Parameters:
            num (CompleNumber): The complex number to be added.
        
        Returns:
            ComplexNumber: A complex number which contains the sum. 
        
        """
        
        re = self.real + num.real 
        im = self.imag + num.imag
        
        return ComplexNumber(re, im)

#help(ComplexNumber)

help(ComplexNumber.add) #misma consulta por un solo metodo

#USO de sphinxs, escribir en Terminal> sphinx-quickstart (en la carpeta docs)
#usar en la carpeta clase3> sphinx-apidoc -o docs proyecto1