from abc import ABC, abstractmethod

class Polygon(ABC):

    @abstractmethod
    def sides(self):
        pass

class Triangle(Polygon):
    def sides(self):
        print('3 sided')

p = Triangle()
print(p.sides())