from unittest import TestCase, main

from project.battle_field import BattleField
from project.card.magic_card import MagicCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class BattleFieldTest(TestCase):

    def setUp(self) -> None:
        self.beginner = Beginner("Borko")
        self.advanced = Advanced("Bobby")
        self.beginner.card_repository.add(MagicCard("Roko"))
        self.advanced.card_repository.add(MagicCard("Roko"))

    def test_attributes_beginner_after_fight(self):
        BattleField.fight(attacker=self.advanced, enemy=self.beginner)
        self.assertEqual(165, self.beginner.health)
        total_damage = 0
        for card in self.beginner.card_repository.cards:
            total_damage += card.damage_points
        self.assertEqual(35, total_damage)

    def test_attributes_advanced_after_fight(self):
        BattleField.fight(attacker=self.advanced, enemy=self.beginner)
        self.assertEqual(295, self.advanced.health)
        total_damage = 0
        for card in self.advanced.card_repository.cards:
            total_damage += card.damage_points
        self.assertEqual(5, total_damage)

    def test_if_some_of_fighters_is_dead(self):
        self.beginner.health = 0
        with self.assertRaises(ValueError) as error:
            BattleField.fight(attacker=self.advanced, enemy=self.beginner)
        self.assertEqual("Player is dead!", str(error.exception))


if __name__ == '__main__':
    main()

