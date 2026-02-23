class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
class Trainer(Employee):
    def __init__(self, name, role, specialization):
        super().__init__(name, role)
        self.specialization = specialization

    def display(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Specialization: {self.specialization}")
class YogaInstructor(Employee):
    def __init__(self, name, role, yoga_style):
        super().__init__(name, role)
        self.yoga_style = yoga_style

    def display(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Yoga Style: {self.yoga_style}")
class MultiTrainer(Trainer, YogaInstructor):
    def __init__(self, name, role, specialization, yoga_style):
        Employee.__init__(self, name, role)
        self.specialization = specialization
        self.yoga_style = yoga_style

    def display(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Specialization: {self.specialization}")
        print(f"Yoga Style: {self.yoga_style}")

employee = Employee("Pranav", "Staff")
trainer = Trainer("Jean", "Trainer", "Strength Training")
yoga_instructor = YogaInstructor("Meera", "Yoga Instructor", "Hatha Yoga")
multi_trainer = MultiTrainer("Abdulla", "Multi Trainer", "Cardio", "Vinyasa Yoga")

print("Employee Details:")
employee.display()

print("\nTrainer Details:")
trainer.display()

print("\nYoga Instructor Details:")
yoga_instructor.display()

print("\nMulti Trainer Details:")
multi_trainer.display()