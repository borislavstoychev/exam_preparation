from project.player.beginner import Beginner
from project.player.player import Player


class BattleField:

    @staticmethod
    def check_for_beginners(player):
        if isinstance(player, Beginner):
            player.health += 40
            for c in player.card_repository.cards:
                c.damage_points += 30
        return player

    @staticmethod
    def get_bonus(player):
        bonus_health = sum(c.health_points for c in player.card_repository.cards)
        return bonus_health

    @staticmethod
    def get_damage_points(player):
        damage = 0
        for c in player.card_repository.cards:
            damage += c.damage_points
        return damage

    @staticmethod
    def fight(attacker: Player, enemy: Player):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")

        BattleField.check_for_beginners(attacker)
        BattleField.check_for_beginners(enemy)
        attacker.health += BattleField.get_bonus(attacker)
        enemy.health += BattleField.get_bonus(enemy)
        enemy.take_damage(BattleField.get_damage_points(attacker))
        attacker.take_damage(BattleField.get_damage_points(enemy))

