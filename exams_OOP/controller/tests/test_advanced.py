from unittest import TestCase, main

from project.card.card_repository import CardRepository
from project.player.advanced import Advanced


class AdvancedTest(TestCase):

    def setUp(self) -> None:
        self.advanced = Advanced("Bobby")

    def test_attributes_correct_values(self):
        self.assertEqual("Bobby", self.advanced.username)
        self.assertEqual(250, self.advanced.health)
        self.assertEqual(False, self.advanced.is_dead)
        self.assertEqual("CardRepository", self.advanced.card_repository.__class__.__name__)

    def test_if_raise_error_empty_str(self):
        with self.assertRaises(ValueError) as error:
            self.advanced.username = ""
        self.assertEqual("Player's username cannot be an empty string.", str(error.exception))

    def test_if_raise_error_negative_health(self):
        with self.assertRaises(ValueError) as error:
            self.advanced.health = -2
        self.assertEqual("Player's health bonus cannot be less than zero.", str(error.exception))

    def test_take_damage_bigger_than_zro(self):
        self.advanced.take_damage(150)
        self.assertEqual(100, self.advanced.health)

    def test_raise_error_when__damage_points_less_than_zero(self):
        with self.assertRaises(ValueError) as error:
            self.advanced.take_damage(-50)
        self.assertEqual("Damage points cannot be less than zero.", str(error.exception))

    def test_is_dead_come_true(self):
        self.advanced.take_damage(250)
        self.assertEqual(True, self.advanced.is_dead)

if __name__ == '__main__':
    main()