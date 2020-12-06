from abc import ABC, abstractmethod

class Point(ABC):
    @abstractmethod
    def GetArity(self):
        pass

    @abstractmethod
    def GetComponent(self, i):
        pass

    def GetName(self):
        return "point"

        
class Point3D(Point):

    def __init__(self, x, y,z):
        self.x = x
        self.y = y
        self.z = z

    def GetArity(self):
        return 3

    def GetComponent(self, i):
        if i == 0:
            return self.x
        elif i == 1: 
            return self.y
        elif i == 2:
            return self.z    
        else:
            raise IndexError("Point3D supports only three dimensions!")

    def GetName(self):
        return super().GetName() + " 3d"

    def __str__(self):
        return f"{{ X = {self.x}, Y = {self.y}, Z = {self.z}  }}"


class Point2D(Point):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def GetArity(self):
        return 2

    def GetComponent(self, i):
        if i == 0:
            return self.x
        elif i == 1: 
            return self.y
        else:
            raise IndexError("Point2D supports only two dimensions!")

    def GetName(self):
        return super().GetName() + " 2d"

    def __str__(self):
        return f"{{ X = {self.x}, Y = {self.y} }}"      
        