"""
This is the class of interval. A real interval is a pair [low,high] of numbers 
representing the set of all numbers in that range {x in R| low<=x<=hi}
It also contains methods  of  addition, subtraction,  multiplication, division,
intersection, and union.
"""

class Interval():
    """
    This is the main body of the interval. 
    """

    def __init__(self, low, high):
        """
        initializing a new interval objects with its lower and higher bonds
        """
        if low > high:
            raise Exception("the lower bond cannot be larger than the upper bond")
        else:
            self.low = low
            self.high = high

    def __repr__(self):
        """
        This is the tostring method of the interval object
        """
        return f"[{self.low}, {self.high}]"

    def __add__(self, b):
        """
        return the new interval from addition of both intervals
        """
        return Interval(self.low + b.low, self.high + b.high)
        

    def __sub__(self, b):
        """
        return the new interval from subtracting two intervals
        """
        return Interval(self.low - b.high,  self.high - b.low)
       
    
    def __mul__(self, b):
        """
        multiplying another interval to the existing one
        """
        a = self.low * b.low
        bb = self.high * b.high
        c = self.high * b.low
        d = self.low * b.high

        return Interval(min(a, bb, c, d), max(a, bb, c, d))
    

    def __truediv__(self, b):
        """
        dividing another interval to the existing one
        """
        if b.low <= 0 and b.high >= 0:
            raise Exception("interval containing zero")
        else:   
            a = self.low / b.low
            bb = self.low / b.high
            c = self.high / b.low
            d = self.high / b.high
           
            return Interval(min(a, bb, c, d), max(a, bb, c, d))
        

    def intersect(self, b):
        """
        find the intersection of the two intervals
        """
        if self.high < b.low or self.low > b.high:
            raise Exception("the intersection is empty")
        return Interval(max(self.low, b.low), min(self.high, b.high))
    

    def intersects(self, b):
        """
        test if there is intersection in two intervals
        """
        if self.high < b.low or self.low > b.high:
            return False
        else:
            return True

    def union(self, b):
        """
        find the union of two intervals
        """
        return Interval(min(self.low, b.low), max(self.high, b.high))
    
    def __eq__(self, b):
        """
        test if two intervals are the same
        """
        return self.low == b.low and self.high == b.high




