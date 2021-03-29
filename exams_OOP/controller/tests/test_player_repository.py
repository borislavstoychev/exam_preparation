from unittest import TestCase, main

from project.player.advanced import Advanced
from project.player.player_repository import PlayerRepository


class PlayerRepositoryTest(TestCase):
    def setUp(self) -> None:
        self.player_repository = PlayerRepository()
        self.player = Advanced("Bobby")

    def test_attributes(self):
        self.assertEqual([], self.player_repository.players)
        self.assertEqual(0, self.player_repository.count)

    def test_add_card_if_not_in_cards(self):
        self.player_repository.add(self.player)
        self.assertEqual([self.player], self.player_repository.players)
        self.assertEqual(1, self.player_repository.count)

    def test_raise_error_if_in_cards(self):
        self.player_repository.add(self.player)
        with self.assertRaises(ValueError) as error:
            self.player_repository.add(self.player)
        self.assertEqual("Player Bobby already exists!", str(error.exception))

    def test_raise_error_when_remove_empty_str(self):
        with self.assertRaises(ValueError) as error:
            self.player_repository.remove("")
        self.assertEqual("Player cannot be an empty string!", str(error.exception))

    def test_remove_card_from_cards(self):
        self.player_repository.add(self.player)
        self.player_repository.remove("Bobby")
        self.assertEqual([], self.player_repository.players)
        self.assertEqual(0, self.player_repository.count)

    def test_find_card_in_cards(self):
        self.player_repository.add(self.player)
        self.assertEqual(self.player, self.player_repository.find("Bobby"))

    def test_find_card_if_card_not_in_cards(self):
        self.player_repository.add(self.player)
        self.assertIsNone(self.player_repository.find("Bobbi"))



if __name__ == '__main__':
    main()