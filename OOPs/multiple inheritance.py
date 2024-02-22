
class Parent1:
    def method1(self):
        print("Method from Parent1")


class Parent2:
    def method2(self):
        print("Method from Parent2")

class Child(Parent1, Parent2):
    def child_method(self):
        print("Method in Child class")


my_child_object = Child()
my_child_object.method2()

