from abc import ABC, abstractmethod
import math


class Figure(ABC):

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_area(self):
        pass


class Triangle(Figure):

    def __init__(self, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def get_perimeter(self):
        return self.side_1 + self.side_2 + self.side_3

    def get_area(self):
        s = self.get_perimeter() / 2
        return math.sqrt(s * (s - self.side_1) * (s - self.side_2) * (s - self.side_3))


class Round(Figure):
    def __init__(self, radius):
        self.radius = radius

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def get_area(self):
        return math.pi * self.radius ** 2


figures = [Triangle(3, 4, 5), Round(2), Triangle(5, 12, 13)]

total_perimeter = sum(figure.get_perimeter() for figure in figures)
total_area = sum(figure.get_area() for figure in figures)

print("Total Perimeter:", total_perimeter)
print("Total Area:", total_area)

