from math import pi

class Rectangle:
    """직사각형 클래스"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """직사각형의 넓이를 리턴한다"""
        return self.width * self.height

    def perimeter(self):
        """직사각형의 둘레를 리턴한다"""
        return 2 * (self.width + self.height)

    def __str__(self):
        """직사각형의 정보를 문자열로 리턴한다"""
        return f"밑변 {self.width}, 높이 {self.height}인 직사각형"


class Circle:
    """원 클래스"""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """원의 넓이를 리턴한다"""
        return pi * self.radius * self.radius

    def perimeter(self):
        """원의 둘레를 리턴한다"""
        return 2 * pi * self.radius

    def __str__(self):
        """원의 정보를 문자열로 리턴한다"""
        return f"반지름 {self.radius}인 원"


class Cylinder:
    """원통 클래스"""
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def __str__(self):
        """원통의 정보를 문자열로 리턴하는 메소드"""
        return f"밑면 반지름 {self.radius}, 높이 {self.height}인 원기둥"


class Paint:
    """그림판 프로그램 클래스"""
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        """그림판에 도형을 추가한다"""
        if isinstance(shape, Circle) or isinstance(shape, Rectangle):
            self.shapes.append(shape)
        else:
            print("넓이, 둘레를 구하는 메소드가 없는 도형은 추가할 수 없습니다!")    

    def total_area_of_shapes(self):
        """그림판에 있는 모든 도형의 넓이의 합을 구한다"""
        return sum([shape.area() for shape in self.shapes])

    def total_perimeter_of_shapes(self):
        """그림판에 있는 모든 도형의 둘레의 합을 구한다"""
        return sum([shape.perimeter() for shape in self.shapes])

    def __str__(self):
        """그림판에 있는 각 도형들의 정보를 출력한다"""
        res_str = "그림판 안에 있는 도형들:\n\n"
        for shape in self.shapes:
            res_str += str(shape) + "\n"
        return res_str


paint_program = Paint()
cylinder = Cylinder(7, 4)
rectangle = Rectangle(3, 7)
circle = Circle(4)

paint_program.add_shape(cylinder)
paint_program.add_shape(circle)
paint_program.add_shape(rectangle)

print(paint_program.total_area_of_shapes())
print(paint_program.total_perimeter_of_shapes())    # 에러