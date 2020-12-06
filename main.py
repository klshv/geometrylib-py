from point import Point3D
from line import Line

p1 = Point3D(5, 10, 10)
print(p1)

l = Line(p1, Point3D(1,2,34))
print(l.Start)
print(l.End)
print(l.GetLength())
