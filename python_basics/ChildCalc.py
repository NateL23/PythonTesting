# child class inherits Calculator class as parent
from python_basics.OopsDemo import Calculator


class ChildCalc(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 10)
        # must manually set up the required parameters in parent constructor (Calculator(num_1,num_2))

    def get_complete_data(self):
        return self.num2 + self.num + self.add_func()


obj = ChildCalc()
print(obj.get_complete_data())
