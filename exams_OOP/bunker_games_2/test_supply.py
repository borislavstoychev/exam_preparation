from unittest import TestCase, main

from project.medicine.painkiller import Painkiller
from project.medicine.salve import Salve
from project.supply.food_supply import FoodSupply
from project.supply.water_supply import WaterSupply


class TestSupply(TestCase):
    def setUp(self) -> None:
        self.painkiller = Painkiller()
        self.water_supply = WaterSupply()
        self.food_supply = FoodSupply()
        self.salve = Salve()

    def test_needs_increase(self):
        self.assertEqual(20, self.painkiller.health_increase)
        self.assertEqual(50, self.salve.health_increase)
        self.assertEqual(20, self.food_supply.needs_increase)
        self.assertEqual(40, self.water_supply.needs_increase)

    def test_needs_increase_raise_error(self):
        self.painkiller.health_increase = - 5
        # self.salve.health_increase = -20
        self.food_supply.needs_increase = -10
        self.water_supply.needs_increase = -10
        self.assertEqual(-5, self.painkiller.health_increase)
        self.assertEqual(-20, self.salve.health_increase)
        self.assertEqual(-10, self.food_supply.needs_increase)
        self.assertEqual(-10, self.water_supply.needs_increase)
    #
    # def test_apply(self):
    #     self.fail()
