from project.medicine.medicine import Medicine
from project.medicine.painkiller import Painkiller
from project.medicine.salve import Salve
from project.supply.supply import Supply
from project.supply.water_supply import WaterSupply
from project.survivor import Survivor
from project.supply.food_supply import FoodSupply


class Bunker:

    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        foods = [supply for supply in self.supplies if supply.__class__.__name__ == "FoodSupply"]
        if not foods:
            raise IndexError("There are no food supplies left!")
        return foods

    @property
    def water(self):
        waters = [w for w in self.supplies if w.__class__.__name__ == "WaterSupply"]
        if not waters:
            raise IndexError("There are no water supplies left!")
        return waters

    @property
    def painkillers(self):
        painkillers_list = [p for p in self.medicine if p.__class__.__name__ == "Painkiller"]
        if not painkillers_list:
            raise IndexError("There are no painkillers left!")
        return painkillers_list

    @property
    def salves(self):
        salves_list = [s for s in self.medicine if s.__class__.__name__ == "Salve"]
        if not salves_list:
            raise IndexError("There are no salves left!")
        return salves_list

    def add_survivor(self, survivor: Survivor):
        try:
            survivor_name = [s.name for s in self.survivors if s.name == survivor.name][0]
            raise IndexError(f"Survivor with name {survivor_name} already exists.")
        except IndexError:
            self.survivors.append(survivor)

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type: str):
        healing_medicine = self.painkillers.pop() if medicine_type == "Painkiller" else self.salves.pop()
        if survivor.needs_healing:
            healing_medicine.apply(survivor)
            self.medicine.remove(healing_medicine)
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor: Survivor, sustenance_type: str):
        food = self.food.pop() if sustenance_type == "FoodSupply" else self.water.pop()
        if survivor.needs_sustenance:
            food.apply(survivor)
            self.supplies.remove(food)
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for s in self.survivors:
            s.needs -= s.age*2
            self.sustain(s, "FoodSupply")
            self.sustain(s, "WaterSupply")


# s = Survivor("Bobby", 20)
# s.health = 20
# s.needs = 20
# b = Bunker()
# b.add_survivor(s)
# f = FoodSupply()
# w = WaterSupply()
# b.add_supply(f)
# b.add_supply(f)
# b.add_supply(w)
# b.add_supply(w)
# p = Painkiller()
# salve = Salve()
# b.add_medicine(p)
# b.add_medicine(p)
# b.add_medicine(p)
# b.add_medicine(salve)
# b.add_medicine(salve)
# b.add_medicine(salve)
# b.add_medicine(salve)
# b.heal(s, "Painkiller")

