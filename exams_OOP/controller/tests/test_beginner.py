from unittest import TestCase, main

from project.card.card_repository import CardRepository
from project.player.beginner import Beginner


class BeginnerTest(TestCase):

    def setUp(self) -> None:
        self.beginner = Beginner("Bobby")

    def test_attributes_correct_values(self):
        self.assertEqual("Bobby", self.beginner.username)
        self.assertEqual(50, self.beginner.health)
        self.assertEqual(False, self.beginner.is_dead)
        self.assertEqual("CardRepository", self.beginner.card_repository.__class__.__name__)

    def test_if_raise_error_empty_str(self):
        with self.assertRaises(ValueError) as error:
            self.beginner.username = ""
        self.assertEqual("Player's username cannot be an empty string.", str(error.exception))

    def test_if_raise_error_negative_health(self):
        with self.assertRaises(ValueError) as error:
            self.beginner.health = -2
        self.assertEqual("Player's health bonus cannot be less than zero.", str(error.exception))

    def test_take_damage_bigger_than_zro(self):
        self.beginner.take_damage(25)
        self.assertEqual(25, self.beginner.health)

    def test_raise_error_when__damage_points_less_than_zero(self):
        with self.assertRaises(ValueError) as error:
            self.beginner.take_damage(-50)
        self.assertEqual("Damage points cannot be less than zero.", str(error.exception))

    def test_is_dead_come_true(self):
        self.beginner.take_damage(50)
        self.assertEqual(True, self.beginner.is_dead)


if __name__ == '__main__':
    main()
