from unittest import TestCase, main

from project.card.magic_card import MagicCard
from project.card.card_repository import CardRepository


class CardRepositoryTest(TestCase):

    def setUp(self) -> None:
        self.card_repository = CardRepository()
        self.card = MagicCard("Bobby")

    def test_attributes(self):
        self.assertEqual([], self.card_repository.cards)
        self.assertEqual(0, self.card_repository.count)

    def test_add_card_if_not_in_cards(self):
        self.card_repository.add(self.card)
        self.assertEqual([self.card], self.card_repository.cards)
        self.assertEqual(1, self.card_repository.count)

    def test_raise_error_if_in_cards(self):
        self.card_repository.add(self.card)
        with self.assertRaises(ValueError) as error:
            self.card_repository.add(self.card)
        self.assertEqual("Card Bobby already exists!", str(error.exception))

    def test_raise_error_when_remove_empty_str(self):
        with self.assertRaises(ValueError) as error:
            self.card_repository.remove("")
        self.assertEqual("Card cannot be an empty string!", str(error.exception))

    def test_remove_card_from_cards(self):
        self.card_repository.add(self.card)
        self.card_repository.remove("Bobby")
        self.assertEqual([], self.card_repository.cards)
        self.assertEqual(0, self.card_repository.count)

    def test_find_card_in_cards(self):
        self.card_repository.add(self.card)
        self.assertEqual(self.card, self.card_repository.find("Bobby"))

    def test_find_card_if_card_not_in_cards(self):
        self.card_repository.add(self.card)
        self.assertIsNone(self.card_repository.find("Bobbi"))

if __name__ == '__main__':
    main()
