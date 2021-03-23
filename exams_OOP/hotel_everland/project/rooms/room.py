from project.appliances.appliance import Appliance
from project.people.child import Child


class Room:

    """
    • family_name: str – passed upon initialization
    • budget: float – passed upon initialization
    • members_count: int – passed upon initialization
    • children: list – empty upon initialization"""

    family_name: str
    budget: float
    members_count: int
    children: []

    def __init__(self, family_name, budget, members_count):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.__expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError('Expenses cannot be negative')

        self.__expenses = value

    def calculate_expenses(self, *args):
        for arg in args:
            for el in arg:
                self.__expenses += el.cost * 30
        return self.__expenses

