from project.player.player import Player
from project.player.beginner import Beginner


class BattleField:

    @staticmethod
    def check_for_beginners(player: Player):
        if isinstance(player, Beginner):
            player.health += 40
            for c in player.card_repository.cards:
                c.damage_points += 30
        return player

    @staticmethod
    def get_bonus(player: Player):
        player.health += sum(c.health_points for c in player.card_repository.cards)
        return player

    @staticmethod
    def damage_points(player: Player):
        total_damage = sum(c.damage_points for c in player.card_repository.cards)
        return total_damage

    @staticmethod
    def fight(attacker: Player, enemy: Player):
        if enemy.is_dead or attacker.is_dead:
            raise ValueError("Player is dead!")
        BattleField.check_for_beginners(attacker)
        BattleField.check_for_beginners(enemy)
        BattleField.get_bonus(attacker)
        BattleField.get_bonus(enemy)
        enemy.health -= BattleField.damage_points(attacker)
        attacker.health -= BattleField.damage_points(enemy)

