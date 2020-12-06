from point import Point3D, Point2D
from line import Line
from triangle import Triangle2D

t = Triangle2D(Point2D(1,3), Point2D(3,7), Point2D(6,9))
print(t.getPerimeter())
