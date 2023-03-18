"""
a class of Gaussian intger that contains both real and imaginary part
"""

class Gaussian_Integer():
    """
    this repersents Gaussian integer class with lots of methods
    """
    def __init__(self, a, b):
        """
        constructor for gaussian integer class
        """
        self.a = a
        self.b = b

    def __str__(self):
        """
        to string method for gaussian integer object
        """
        return f'{self.a} + {self.b}i'
    
    def __add__(self, x):
        """
        adding another gaussian integer to the existing one
        and return it
        """
    
        return Gaussian_Integer(self.a + x.a, self.b + x.b)

    def __mul__(self, x):
        """
        multiplying another gaussian integer to the existing one
        and return it
        """
        a = self.a
        b = self.b
        c = x.a
        d = x.b 
        return Gaussian_Integer(self.a + a*c - b*d, self.b + a*d + b*c)
        
def main():
    a = Gaussian_Integer(3, 5)
    b = Gaussian_Integer(2, 4)
    print("a + b = ", a+b)
    print("a * b = ", a*b)
    

main()
