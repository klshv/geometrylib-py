from point import Point
from line import Line

from functools import reduce

class MultiVertexShape:
    def __init__(self, vertices: tuple[Point]):
        self._vertices = vertices

    @property
    def vertices(self):
        return self._vertices

    def getEdges(self):
        getVertexIndex = lambda i: i + 1 if i + 1 < self.vertices.__len__() else 0
        
        return map(
            lambda x: Line(x[1], self.vertices[getVertexIndex(x[0])]),
            enumerate(self.vertices)
        )

    def getPerimeter(self):
        return reduce(
            lambda cur, acc: cur + acc,
            map(lambda x: x.getLength(), self.getEdges())
        )