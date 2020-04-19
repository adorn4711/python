class Points(object):
    def __init__(self, x, y, z):
        self.x =x;
        self.y =y;
        self.z =z;

    def __sub__(self, no):
        result = Points(self.x-no.x,self.y-no.y,self.z-no.z)
        return result

    def dot(self, no):
        #print("dot called")
        dot = self.x*no.x+self.y*no.y+self.z*no.z
        return dot

    def cross(self, no):
        #print("cross called")
        x = self.y*no.z-self.z*no.y
        y = self.z*no.x-self.x*no.z
        z = self.x*no.y-self.y*no.x
        return Points(x,y,z)

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

    def print(self):
        print("Point({0:5f},{1:5f},{2:5f})".format(self.x,self.y,self.z))
