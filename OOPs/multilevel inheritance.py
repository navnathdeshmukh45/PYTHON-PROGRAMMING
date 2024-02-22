
class Grandparent:
    def grandparent_method(self):
        print("Method from Grandparent")


class Parent(Grandparent):
    def parent_method(self):
        print("Method from Parent")


class Child(Parent):
    def child_method(self):
        print("Method from Child")


my_child_object = Child()

my_child_object.grandparent_method() 
   
