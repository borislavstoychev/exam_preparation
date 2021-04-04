from unittest import TestCase, main

from project.factory.factory import Factory
from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):

    def setUp(self) -> None:
        self.paint_factory = PaintFactory("Bobby", 20)

    def test_constructor(self):
        self.assertEqual("Bobby", self.paint_factory.name)
        self.assertEqual(20, self.paint_factory.capacity)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.paint_factory.valid_ingredients)
        self.assertEqual({}, self.paint_factory.ingredients)
        self.assertEqual(self.paint_factory.ingredients, self.paint_factory.products)

    def test_inherits_from_factory(self):
        self.assertTrue(issubclass(PaintFactory, Factory))

    def test_add_ingredient_if_raise_type_error(self):
        with self.assertRaises(TypeError) as error:
            self.paint_factory.add_ingredient("bebmbeno", 5)
        # self.assertEqual("Ingredient of type bebmbeno not allowed in PaintFactory", str(error.exception))

    def test_add_ingredient_if_raise_value_error(self):
        with self.assertRaises(ValueError) as error:
            self.paint_factory.add_ingredient("white", 25)
        # self.assertEqual("Not enough space in factory", str(error.exception))

    def test_add_ingredient_if_not_in_ingredients(self):
        self.paint_factory.add_ingredient("white", 5)
        self.assertEqual({"white": 5}, self.paint_factory.ingredients)

    def test_add_ingredient(self):
        self.paint_factory.add_ingredient("white", 5)
        self.paint_factory.add_ingredient("white", 5)
        self.assertEqual({"white": 10}, self.paint_factory.ingredients)

    def test_remove_ingredient_if_raise_key_error(self):
        self.paint_factory.add_ingredient("white", 5)
        with self.assertRaises(KeyError) as error:
            self.paint_factory.remove_ingredient("blue", 5)
        # self.assertEqual('No such product in the factory', error.exception.args[0])

    def test_remove_ingredient_if_quantity_greater_then_ingredient_type_quantity(self):
        self.paint_factory.add_ingredient("white", 5)
        with self.assertRaises(ValueError) as error:
            self.paint_factory.remove_ingredient("white", 6)
        # self.assertEqual("Ingredient quantity cannot be less than zero", str(error.exception))

    def test_remove_ingredient_quantity(self):
        self.paint_factory.add_ingredient("white", 5)
        self.paint_factory.remove_ingredient("white", 4)
        self.assertEqual({"white": 1}, self.paint_factory.ingredients)

    def test_property_products(self):
        self.assertEqual({}, self.paint_factory.products)

    def test_can_add(self):
        self.paint_factory.add_ingredient("white", 5)
        self.paint_factory.can_add(5)
        self.assertTrue(self.paint_factory.can_add(5))


if __name__ == '__main__':
    main()

