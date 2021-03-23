from project.rooms.room import Room
# from project.people.child import Child
# from project.appliances.tv import TV
# from project.appliances.laptop import Laptop
# from project.appliances.fridge import Fridge
# from project.appliances.stove import Stove
import unittest


class RoomTests(unittest.TestCase):

    def setUp(self) -> None:
        self.room = Room("Stoychevi", 1000, 2)

    def test_constructor(self):
        self.assertEqual("Stoychevi", self.room.family_name)
        self.assertEqual(1000, self.room.budget)
        self.assertEqual(2, self.room.members_count)
        self.assertEqual([], self.room.children)
        self.assertEqual(0, self.room.expenses)

    def test_if_setter_expenses(self):
        self.room.expenses = 25
        self.assertEqual(25, self.room.expenses)

    def test_if_raise_error(self):
        with self.assertRaises(ValueError):
            self.room.expenses = -25


    def test_calculate_expenses(self):
        child_1 = Child(1, 1)
        child_2 = Child(2, 2)
        children = [child_1, child_2]
        appliance_1 = TV()
        appliance_2 = Laptop()
        appliance_3 = Fridge()
        appliance_4 = Stove()
        appliances = [appliance_4, appliance_3, appliance_2, appliance_1]
        self.room.calculate_expenses(children, appliances)
        self.assertEqual(312.0, self.room.expenses)



if __name__ == "__main__":
    unittest.main()