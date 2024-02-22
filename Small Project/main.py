class student:
    def __init__(self,roll_Number,Name ,class_name): 
        self.roll_Number = roll_Number
        self.Name = Name
        self.class_name = class_name
        self.marks ={}

    def add_mark(self,subject,marks):
        if subject in self.marks:
            print(f"{self.marks} already has mark of {subject}")
        else:
            self.marks[subject] = marks
    def calculate_average_mark(self):
        if not self.marks :
            print("there are no mark available marks")
        total_mark = sum(self.marks.values())
        average_mark = total_mark/len(self.marks)
        return average_mark
    
    def display_student_info(self):
        print(f"Student information")
        print(f"roll number :{self.roll_Number}")
        print(f"name:{self.Name}")
        print(f"class:{self.class_name}")
        print(f"marks : {self.marks}")
        print(f"average mark are : {self.calculate_average_mark()}")

student1 = student(28,"Priya","3 year")
student2 = student(78,"Navnath","3 year")

student2.add_mark("CP",80)
student2.add_mark("Math",80)

student1.add_mark("CP",80)
student1.add_mark("Math",80)

student1.display_student_info()
student2.display_student_info()