from project.medicine.medicine import Medicine
from project.supply.supply import Supply
from project.survivor import Survivor


class Bunker:

    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        foods = [f for f in self.supplies if f.__class__.__name__ == "FoodSupply"]
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
        if survivor.name in [s.name for s in self.survivors]:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def searching_medicine(self, medicine):
        if medicine == "Painkiller":
            return self.painkillers
        return self.salves

    def heal(self, survivor: "Survivor", medicine_type: str):
        if survivor.needs_healing:
            medicine = self.searching_medicine(medicine_type).pop()
            medicine.apply(survivor)
            self.medicine.remove(medicine)
            return f"{survivor.name} healed successfully with {medicine_type}"

    def searching_sustenance(self, sustenance):
        if sustenance == "WaterSupply":
            return self.water
        return self.food

    def sustain(self, survivor: "Survivor", sustenance_type: str):
        if survivor.needs_sustenance:
            sustenance = self.searching_sustenance(sustenance_type).pop()
            sustenance.apply(survivor)
            self.supplies.remove(sustenance)
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2
            self.sustain(survivor, "WaterSupply")
            self.sustain(survivor, "FoodSupply")




