from project.player.player_repository import PlayerRepository
from project.card.card_repository import CardRepository
from project.player.beginner import Beginner
from project.player.advanced import Advanced
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.battle_field import BattleField


class Controller:

    def __init__(self):
        self.player_repository: PlayerRepository = PlayerRepository()
        self.card_repository: CardRepository = CardRepository()

    def add_player(self, type: str, username: str):
        if type == "Beginner":
            player = Beginner(username)
            self.player_repository.add(player)
        elif type == "Advanced":
            player = Advanced(username)
            self.player_repository.add(player)
        return f"Successfully added player of type {type} with username: {username}"

    def add_card(self, type: str, name: str):
        if type == "Magic":
            card = MagicCard(name)
            self.card_repository.add(card)
        elif type == "Trap":
            card = TrapCard(name)
            self.card_repository.add(card)

        return f"Successfully added card of type {type}Card with name: {name}"

    def add_player_card(self, username: str, card_name: str):
        player = self.player_repository.find(username)
        card = self.card_repository.find(card_name)
        player.card_repository.add(card)
        return f"Successfully added card: {card_name} to user: {username}"

    def fight(self, attack_name: str, enemy_name: str):
        attacker = self.player_repository.find(attack_name)
        enemy = self.player_repository.find(enemy_name)
        BattleField.fight(attacker, enemy)
        return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"

    @staticmethod
    def get_cards(player):
        cards = ""
        for card in player.card_repository.cards:
            cards += f"### Card: {card.name} - Damage: {card.damage_points}\n"
        return cards

    def report(self):
        result = ""
        for user in self.player_repository.players:
            username1 = user.username
            health1 = user.health
            cards = Controller.get_cards(user)
            result += f"Username: {username1} - Health: {health1} - Cards {user.card_repository.count}\n" \
                      f"{cards}"

        return result


