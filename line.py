from point import Point
import math
class Line:
    
    def __init__(self, start:Point, end:Point):
        if start.GetArity() != end.GetArity():
            raise RuntimeError("Разная размерность")
        self._start = start
        self._end = end
    
    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end


    def __str__(self):
        return (f"FROM: {self.start}\nTO: {self.end}")

    def getLength(self):
        arity = self.start.GetArity()
        sum = 0
        for i in range(0,arity):
            sum += (self.start.GetComponent(i) - self.end.GetComponent(i))**2
        return math.sqrt(sum)    