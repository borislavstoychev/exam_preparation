from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.stove import Stove


class OldCouple(Room):
    room_cost = 15
    appliances = [TV(), Fridge(), Stove()]

    def __init__(self, family_name: str, pension_one: float, pension_two: float):
        budget = pension_one + pension_two
        members_count = 2
        super().__init__(family_name, budget, members_count)
        self.appliances = OldCouple.appliances * members_count
        self.room_cost = OldCouple.room_cost
        self.__expenses = self.calculate_expenses(self.appliances)

    @property
    def expenses(self):
        return self.__expenses
