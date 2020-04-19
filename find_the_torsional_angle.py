import math

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

if __name__ == '__main1__':
    points = list()
    #for i in range(4):
    #    a = list(map(float, input().split()))
    #    points.append(a)

    #a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    a = Points(0,4,5)
    b = Points(1 ,7, 6)
    c= Points(0, 5, 9)
    d =Points(1, 7, 2)
    
    a.print()
    b.print()
    c.print()
    d.print()
    e = a-b
    e.print()
    print("Dot a,b:",a.dot(b))
    f = a.cross(b)
    print("Cross a,b")
    f.print()


if __name__ == '__main__':
    points = list()
       #for i in range(4):
    #    a = list(map(float, input().split()))
    #    points.append(a)

    #a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    a = Points(0,4,5)
    b = Points(1 ,7, 6)
    c= Points(0, 5, 9)
    d =Points(1, 7, 2)
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
