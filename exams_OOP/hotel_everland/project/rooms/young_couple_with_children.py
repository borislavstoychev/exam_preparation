from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.people.child import Child


class YoungCoupleWithChildren(Room):

    room_cost = 30
    appliances = [TV(), Fridge(), Laptop()]

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        budget = salary_two + salary_one
        members_count = 2 + len(children)
        super().__init__(family_name, budget, members_count)
        self.room_cost = YoungCoupleWithChildren.room_cost
        self.appliances = YoungCoupleWithChildren.appliances * members_count
        self.children = list(children)
        self.__expenses = self.calculate_expenses(self.appliances, self.children)

    @property
    def expenses(self):
        return self.__expenses


# child_one = Child(5, 1, 2, 1)
# child_two = Child(3, 2)
# young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child_one, child_two)
# print(young_couple_with_children.expenses)
