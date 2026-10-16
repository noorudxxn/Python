from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, account_year):
        self.name = name
        self.account_year = account_year

    def account_age(self):
        return 2025 - self.account_year

    @abstractmethod
    def get_role(self):
        pass


class Admin(User):
    def get_role(self):
        return "Admin"

    def __str__(self):
        return f"Name: {self.name}, Role: {self.get_role()}"


class Guest(User):
    def get_role(self):
        return "Guest"

    def __str__(self):
        return f"Name: {self.name}, Role: {self.get_role()}"


admin = Admin("Arun", 2020)
guest = Guest("Rahul", 2023)

print("Admin Role:", admin.get_role())
print("Admin Account Age:", admin.account_age())
print(admin)

print()

print("Guest Role:", guest.get_role())
print("Guest Account Age:", guest.account_age())
print(guest)