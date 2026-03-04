from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, joining_year):
        self.name = name
        self.joining_year = joining_year

    def years_on_platform(self):
        return 2025 - self.joining_year

    def get_role(self):
        pass

    def display_info(self):
        print(
            f"Name: {self.name} | "
            f"Role: {self.get_role()} | "
            f"Years on Platform: {self.years_on_platform()}"
        )


class Customer(User):
    def get_role(self):
        return "Customer"


class Vendor(User):
    def get_role(self):
        return "Vendor"


customer1 = Customer("Alice", 2020)
vendor1 = Vendor("Bob", 2018)

customer1.display_info()
vendor1.display_info()