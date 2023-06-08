#Christian Briceno Weiss

import funciones
import pytest 

def test_add():
    x = 3
    y = 2
    result = 5
    assert result == funciones.add(x,y)

def test_substract():
    x = 3
    y = 2
    result = 1
    assert result == funciones.substract(x,y)

def test_multiply():
    x = 3
    y = 2
    result = 6
    assert result == funciones.multiply(x,y)

def test_divide():
    x = 6
    y = 2
    result = 3
    assert result == funciones.divide(x,y)

def test_raised():
    x = 3
    y = 2
    result = 9
    assert result == funciones.raised(x,y)