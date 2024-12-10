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
# class Figure:
#     unit = "cm"
#     def __init__(self):
#         pass
#     def calculate_area(self):
#         raise NotImplementedError("Метод calculate_area должен быть реализован в подклассе")
#
#     def info(self):
#         raise NotImplementedError("Метод info должен быть реализован в подклассе")
#
# class Square(Figure):
#     def __init__(self, side_length):
#         super().__init__()
#         self.__side_length = side_length
#
#     def calculate_area(self):
#         return self.__side_length ** 2
#
#     def info(self):
#         area = self.calculate_area()
#         print(f"Square side length: {self.__side_length}{self.unit}, area: {area}{self.unit}²")
#
#
# class Rectangle(Figure):
#     def __init__(self, length, width):
#         super().__init__()
#         self.__length = length
#         self.__width = width
#
#     def calculate_area(self):
#         return self.__length * self.__width
#
#     def info(self):
#         area = self.calculate_area()
#         print(f"Rectangle length: {self.__length}{self.unit}, width: {self.__width}{self.unit}, area: {area}{self.unit}²")
#
# if __name__ == "__main__":
#     figures = [
#         Square(5),
#         Square(10),
#         Rectangle(5, 8),
#         Rectangle(10, 15),
#         Rectangle(3, 7),
#     ]
#     for figure in figures:
#         figure.info()


""""homework3"""
class Computer:
    def __init__(self, cpu: int, memory: int):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value: int):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value: int):
        self.__memory = value

    def make_computations(self, operator: str):
        if operator == '+':
            return self.__cpu + self.__memory
        elif operator == '-':
            return self.__cpu - self.__memory
        elif operator == '*':
            return self.__cpu * self.__memory
        elif operator == '/':
            return self.__cpu / self.__memory if self.__memory != 0 else 'Error: Division by zero'
        else:
            return 'Invalid operator'
    def __eq__(self, other):
        return self.memory == other.memory

    def __ne__(self, other):
        return self.memory != other.memory

    def __lt__(self, other):
        return self.memory < other.memory

    def __le__(self, other):
        return self.memory <= other.memory

    def __gt__(self, other):
        return self.memory > other.memory

    def __ge__(self, other):
        return self.memory >= other.memory

    def __str__(self):
        return f"Computer(cpu={self.cpu}, memory={self.memory})"


class Phone:
    def __init__(self, sim_cards_list: list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value: list):
        self.__sim_cards_list = value

    def call(self, sim_card_number: int, call_to_number: str):
        if 1 <= sim_card_number <= len(self.__sim_cards_list):
            print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} ({self.__sim_cards_list[sim_card_number - 1]})")
        else:
            print("Неверный номер сим-карты")

    def __str__(self):
        return f"Phone(sim_cards_list={self.sim_cards_list})"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu: int, memory: int, sim_cards_list: list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location: str):
        print(f"Прокладывается маршрут до {location}...")

    def __str__(self):
        return f"SmartPhone(cpu={self.cpu}, memory={self.memory}, sim_cards_list={self.sim_cards_list})"
computer = Computer(8, 16)
phone = Phone(["Beeline", "Megacom", "O!"])
smartphone1 = SmartPhone(4, 8, ["Beeline", "Megacom"])
smartphone2 = SmartPhone(6, 32, ["O!"])
print(computer)
print(phone)
print(smartphone1)
print(smartphone2)
print("Computer Methods")
print(computer.make_computations('+'))
print(computer.make_computations('/'))
print("Phone Methods")
phone.call(1, "+996777998811")
phone.call(3, "+996555123456")
print("SmartPhone Methods")
smartphone1.call(2, "+996700654321")
smartphone1.use_gps("Бишкек")
print("Comparisons")
print(smartphone1 > smartphone2)
print(smartphone1 == smartphone2)




