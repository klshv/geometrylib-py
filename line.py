from point import Point
import math
class Line:
    
    def __init__(self, start:Point, end:Point):
        if start.GetArity() != end.GetArity():
            raise RuntimeError("Разная размерность")
        self.start = start
        self.end = end
    
    @property
    def Start(self):
        return self.start

    @property
    def End(self):
        return self.end

    def __str__(self):
        return (f"FROM: {self.Start}\nTO: {self.End}")

    def GetLength(self):
        arity = self.start.GetArity()
        sum = 0
        for i in range(0,arity):
            sum += (self.start.GetComponent(i) - self.end.GetComponent(i))**2
        return math.sqrt(sum)    