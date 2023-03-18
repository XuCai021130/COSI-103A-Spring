from Interval import Interval
import pytest


"""
This program tests all the methods and exception
in the Interval.py file 
"""
def test_add():
    """
    test the __add__() method
    """
    x1 = Interval(0.9,1.1)
    x2 = Interval(1.999,2.001)
    
    assert x1 + x2==Interval(2.899,3.101)

def test_mul():
    """
    test the __mul__() method
    """
    x2 = Interval(1.999,2.001)
    x3 = Interval(-1,1)
    assert x2*x3 == Interval(-2.001,2.001)

def test_division():
    """
    test the __truediv__() method
    """
    x3 = Interval(-1,1)
    x4 = Interval(10,10)
    assert x3/x4 == Interval(-0.1,0.1)

def test_all_arithmetic_operations():
    """
    test all the arithmetic operations
    """
    x1 = Interval(0.9,1.1)
    x2 = Interval(1.999,2.001)
    x3 = Interval(-1,1)
    x4 = Interval(10,10)
    assert x4-x1*x2/(x4+x3)-(x1+x2) == Interval(6.6544333333333325,6.937445454545455)

def test_intersect():
    """
    test the intersect() method
    """
    x1 = Interval(0.9,1.1)
    x3 = Interval(-1,1)
    assert x1.intersect(x3) == Interval(0.9,1)

def test_intersects():
    """
    test the intersects() methood
    """
    x1 = Interval(0.9,1.1)
    x2 = Interval(1.999,2.001)
    x3 = Interval(-1,1)
    assert x1.intersects(x3) == True
    assert x1.intersects(x2) == False

def test_Exception1():
    """
    test interval division by zero exception
    """
    x3 = Interval(-1,1)
    x4 = Interval(10,10)
    with pytest.raises(Exception):
        x = x4/x3

def test_Exception2():
    """
    test empty interval exception
    """
    with pytest.raises(Exception):
        a=Interval(2,-2)



