from point import Point3D, Point2D
from line import Line
from triangle import Triangle2D
from multivertexshape import MultiVertexShape

t = Triangle2D(Point2D(1,3), Point2D(3,7), Point2D(6,9))
print(t.getPerimeter())

multi = MultiVertexShape((Point2D(1,3), Point2D(3,7), Point2D(6,9)))
print(multi.getPerimeter())

square = MultiVertexShape((Point2D(0, 0), Point2D(0, 2), Point2D(2, 2), Point2D(2, 0)))
print(square.getPerimeter())
