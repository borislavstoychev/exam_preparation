from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
# from project.people.child import Child
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        super().__init__(family_name=family_name, budget=salary_two + salary_one, members_count=2 + len(children))
        self.room_cost = 30
        self.appliances = [TV(), Fridge(), Laptop(), TV(), Fridge(), Laptop()]
        for _ in children:
            self.appliances += [TV(), Fridge(), Laptop()]
        self.children = list(children)
        self.expenses = self.calculate_expenses(self.children, self.appliances)


# child_one = Child(5, 1, 2, 1)
# child_two = Child(3, 2)
# young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child_one, child_two)
# print(young_couple_with_children.expenses)
