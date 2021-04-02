# from project.people.child import Child
# from project.appliances.tv import TV
# from project.appliances.stove import Stove

class Room:

    def __init__(self, family_name: str, budget: float, members_count: int):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        for arg in args:
            for a in arg:
                self.__expenses += a.cost * 30
        return self.__expenses




# ch = [Child(2, 2,3,4), Child(1, 1,2,3)]
# ap = [TV(), Stove()]
# r = Room("Bobbi", 250, 2)
# r.calculate_expenses(ch, ap)
# print(r.expenses)