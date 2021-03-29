from unittest import TestCase, main

from project.card.trap_card import TrapCard


class TrapCardTest(TestCase):

    def setUp(self) -> None:
        self.card = TrapCard("Bobby")

    def test_constructor_correct_values(self):
        self.assertEqual("Bobby", self.card.name)
        self.assertEqual(120, self.card.damage_points)
        self.assertEqual(5, self.card.health_points)

    def test_raise_error_name_is_empty_str(self):
        with self.assertRaises(ValueError) as error:
            self.card.name = ""
        self.assertEqual("Card's name cannot be an empty string.", str(error.exception))

    def test_raise_error_damage_is_less_than_aero(self):
        with self.assertRaises(ValueError) as error:
            self.card.damage_points = -2
        self.assertEqual("Card's damage points cannot be less than zero.", str(error.exception))

    def test_rise_error_health_is_less_than_zero(self):
        with self.assertRaises(ValueError) as error:
            self.card.health_points = -2
        self.assertEqual("Card's HP cannot be less than zero.", str(error.exception))


if __name__ == '__main__':
    main()
