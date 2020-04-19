#point test
from points import Points
import math

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
