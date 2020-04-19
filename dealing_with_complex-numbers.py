import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.r = real
        self.i = imaginary    
        
    def __add__(self, no):
        return Complex(self.r+no.r,self.i+no.i)
    def __sub__(self, no):
        return Complex(self.r-no.r,self.i-no.i)
       
    def __mul__(self, no):
        return Complex(self.r*no.r-self.i*no.i,self.r*no.i+self.i*no.r)

    def __truediv__(self, no):
        ne=(no.r*no.r+no.i*no.i)
        re=(self.r*no.r+self.i*no.i)/ne
        im=(self.i*no.r-self.r*no.i)/ne
        return Complex(re,im)

    def mod(self):
        re= math.sqrt(self.r*self.r+self.i*self.i)
        return Complex(re,0)

    def __str__(self):
        if self.i == 0:
            result = "%.2f+0.00i" % (self.r)
        elif self.r == 0:
            if self.i >= 0:
                result = "0.00+%.2fi" % (self.i)
            else:
                result = "0.00-%.2fi" % (abs(self.i))
        elif self.i > 0:
            result = "%.2f+%.2fi" % (self.r, self.i)
        else:
            result = "%.2f-%.2fi" % (self.r, abs(self.i))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
