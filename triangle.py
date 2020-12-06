from point import Point2D
from line import Line

class Triangle2D:
    def __init__(self, vertex1: Point2D, vertex2: Point2D, vertex3: Point2D):
        self.Vertex1 = vertex1
        self.Vertex2 = vertex2
        self.Vertex3 = vertex3

    @property
    def vertex1(self):
        return self.Vertex1

    @property   
    def vertex2(self):
        return self.Vertex2   

    @property   
    def vertex3(self):
        return self.Vertex3   

    def getPerimeter(self):
        edge1 = Line(self.vertex1, self.vertex2)
        edge2 = Line(self.vertex2, self.vertex3)
        edge3 = Line(self.vertex3, self.vertex1)
        return edge1.getLength() + edge2.getLength() + edge3.getLength()