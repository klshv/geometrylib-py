from point import Point3D, Point2D
from line import Line
from triangle import Triangle2D

t = Triangle2D(Point2D(1,3), Point2D(3,7), Point2D(6,9))
print(t.getPerimeter())

p1 = Point3D(5, 10, 10)
print(p1)

l = Line(p1, Point3D(1,2,34))
print(l.start)
print(l.end)
print(l.getLength())
