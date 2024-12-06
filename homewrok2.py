# class person:
#     def __init__(self, full_name, age, is_married):
#         self.full_name = full_name
#         self.age = age
#         self.is_married = is_married
#
#     def introduce_myself(self):
#         marital_status = "женат" if self.is_married else "неженат"
#         print(f"Меня зовут {self.full_name}. Мне {self.age} лет. Я {marital_status}.")
#
#
# class Student(person):
#     def __init__(self, full_name, age, is_married, marks):
#         super().__init__(full_name, age, is_married)
#         self.marks = marks
#
#     def average_marks(self):
#         if self.marks:
#             return sum(self.marks.values()) / len(self.marks)
#         return 0
#
# class Teacher(person):
#     def __init__(self, full_name, age, is_married, experience, base_salary):
#         super().__init__(full_name, age, is_married)
#         self.experience = experience
#         self.base_salary = base_salary
#
#     def calculate_salary(self):
#         bonus = 0
#
#         if self.experience > 3:
#             bonus = 0.05 * self.base_salary * (self.experience - 3)
#             return self.base_salary + bonus
#         teacher = Teacher("Иван Иванов", 40, True, 5, 50000)
#         print(f"Зарплата учителя: {teacher.calculate_salary()}")
#
#     def create_students():
#         student1 = Student("Алексей Петров", 16, False, {"Математика": 5, "Русский язык": 4, "Физика": 5})
#
#         student2=("Мария Смирнова", 17, False, {"Математика": 4, "Русский язык": 5, "История": 4})
#         student3 = Student("Дмитрий Кузнецов", 16, False, {"Математика": 5, "Биология": 5, "Химия": 4})
#
#         return [student1, student2, student3]
#     students = create_students()
#
#     for student in students:
#         student.introduce_myself()
#     print(f"Средняя оценка: {student.average_marks()}")



""""homework 2"""
class Figure:
    unit = "cm"
    def __init__(self):
        pass
    def calculate_area(self):
        raise NotImplementedError("Метод calculate_area должен быть реализован в подклассе")

    def info(self):
        raise NotImplementedError("Метод info должен быть реализован в подклассе")

class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length

    def calculate_area(self):
        return self.__side_length ** 2

    def info(self):
        area = self.calculate_area()
        print(f"Square side length: {self.__side_length}{self.unit}, area: {area}{self.unit}²")


class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width

    def calculate_area(self):
        return self.__length * self.__width

    def info(self):
        area = self.calculate_area()
        print(f"Rectangle length: {self.__length}{self.unit}, width: {self.__width}{self.unit}, area: {area}{self.unit}²")

if __name__ == "__main__":
    figures = [
        Square(5),
        Square(10),
        Rectangle(5, 8),
        Rectangle(10, 15),
        Rectangle(3, 7),
    ]
    for figure in figures:
        figure.info()
