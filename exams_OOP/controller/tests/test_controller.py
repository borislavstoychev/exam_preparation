from unittest import TestCase, main

from project.card.card_repository import CardRepository
from project.card.trap_card import TrapCard
from project.card.magic_card import MagicCard
from project.controller import Controller
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class ControllerTest(TestCase):

    def setUp(self) -> None:
        self.controller = Controller()

    def test_init(self):
        self.assertEqual("PlayerRepository", Controller().player_repository.__class__.__name__)
        self.assertEqual("CardRepository", Controller().card_repository.__class__.__name__)

    def test_add_beginner_successfully(self):
        result = Controller()
        r = result.add_player(type="Beginner", username="Bobby")
        self.assertEqual("Successfully added player of type Beginner with username: Bobby", r)
        self.assertEqual("Beginner", result.player_repository.players[0].__class__.__name__)
        self.assertEqual("Bobby", result.player_repository.players[0].username)
        self.assertEqual(1, result.player_repository.count)

    def test_add_advanced_successfully(self):
        r = Controller()
        result = r.add_player(type="Advanced", username="Bobby")
        self.assertEqual("Successfully added player of type Advanced with username: Bobby", result)
        self.assertEqual("Advanced", r.player_repository.players[0].__class__.__name__)
        self.assertEqual("Bobby", r.player_repository.players[0].username)
        self.assertEqual(1, r.player_repository.count)

    def test_add_magic_card_successfully(self):
        result = self.controller.add_card(type="Magic", name="Roko")
        self.assertEqual("Successfully added card of type MagicCard with name: Roko", result)
        self.assertEqual("MagicCard", self.controller.card_repository.cards[0].__class__.__name__)
        self.assertEqual("Roko", self.controller.card_repository.cards[0].name)
        self.assertEqual(1, self.controller.card_repository.count)

    def test_add_trap_card_successfully(self):
        result = self.controller.add_card(type="Trap", name="Roky")
        self.assertEqual("Successfully added card of type TrapCard with name: Roky", result)
        self.assertEqual("TrapCard", self.controller.card_repository.cards[0].__class__.__name__)
        self.assertEqual("Roky", self.controller.card_repository.cards[0].name)
        self.assertEqual(1, self.controller.card_repository.count)

    def test_adding_player_card(self):
        self.controller.add_player(type="Advanced", username="Bobby")
        self.controller.add_card(type="Magic", name="Roko")
        result = self.controller.add_player_card("Bobby", "Roko")
        self.assertEqual("Successfully added card: Roko to user: Bobby", result)

    def test_fight(self):
        self.controller.add_player(type="Advanced", username="Bobby")
        self.controller.add_card(type="Magic", name="Roko")
        self.controller.add_player_card("Bobby", "Roko")
        self.controller.add_player(type="Advanced", username="Bobbi")
        self.controller.add_player_card("Bobbi", "Roko")
        result = self.controller.fight("Bobby", "Bobbi")
        self.assertEqual("Attack user health 325 - Enemy user health 325", result)

    def test_report(self):
        self.controller.add_player(type="Beginner", username="Bobby")
        self.controller.add_card(type="Magic", name="Roko")
        self.controller.add_player_card("Bobby", "Roko")
        self.controller.add_player(type="Advanced", username="Bobbi")
        self.controller.add_player_card("Bobbi", "Roko")
        expect = "Username: Bobby - Health: 50 - Cards 1\n" \
                 "### Card: Roko - Damage: 5\n" \
                 "Username: Bobbi - Health: 250 - Cards 1\n" \
                 "### Card: Roko - Damage: 5\n"
        result = self.controller.report()
        self.assertEqual(expect, result)


if __name__ == '__main__':
    main()