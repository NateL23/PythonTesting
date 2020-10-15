# Object Oriented Programing - oop
# Classes are user defined blueprints/prototypes
# Classes have methods, class variables, instance variables, constructor, etc
# self keyword is mandatory for calling variable names inside menthod
# instance and class variables have different purpose
# constructor name should bne __init__


class Calculator:
    num = 100
    # class variables

    def __init__(self, a, b):
        self.num_1 = a
        self.num_2 = b
        print('The default constructor is called automatically when object is created')
        # default constructor

    @staticmethod
    def get_data():
        print('I am now executing as method in class')

    def add_func(self):
        return self.num_1 + self.num_2 + Calculator.num

    def sub_func(self):
        return Calculator.num - self.num_1 - self.num_2


obj = Calculator(2, 3)
# parameters need to be included in constructor
obj.get_data()
print(obj.num)
print('Addition(2+3+100): ', obj.add_func())
print('Subtraction(100-2-3): ', obj.sub_func())
