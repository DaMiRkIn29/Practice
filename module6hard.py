import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = list(color) if self.__is_valid_color(color) else [0, 0, 0]
        self.filled = False
        self.__sides = list(sides) if len(sides) == self.sides_count and self.__is_valid_sides(*sides) else [
                                                                                                                1] * self.sides_count

    def __is_valid_color(self, color):
        return len(color) == 3 and all(isinstance(c, int) and 0 <= c <= 255 for c in color)

    def set_color(self, r, g, b):
        if self.__is_valid_color((r, g, b)):
            self.__color = [r, g, b]

    def get_color(self):
        return self.__color

    def __is_valid_sides(self, *sides):
        return all(isinstance(side, int) and side > 0 for side in sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count and self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi) if self.get_sides()[0] > 0 else 1

    def get_square(self):
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *(sides * 12) if len(sides) == 1 else sides)

    def get_volume(self):
        edge_length = self.get_sides()[0]
        return edge_length ** 3


if __name__ == "__main__":
    circle1 = Circle((200, 200, 100), 10)
    cube1 = Cube((222, 35, 130), 6)

    circle1.set_color(55, 66, 77)
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)
    print(cube1.get_color())

    cube1.set_sides(5, 3, 12, 4, 5)
    print(cube1.get_sides())
    circle1.set_sides(15)
    print(circle1.get_sides())

    print(len(circle1))
    print(cube1.get_volume())