from project.player.player import Player


class PlayerRepository:

    def __init__(self):
        self.players = []

    @property
    def count(self):
        return len(self.players)

    def add(self, player: Player):
        if self.find(player.username):
            raise ValueError(f"Player {player.username} already exists!")
        self.players.append(player)

    def remove(self, player: str):
        if player == "":
            raise ValueError("Player cannot be an empty string!")
        self.players.remove(self.find(player))

    def find(self, username: str):
        for p in self.players:
            if username == p.username:
                return p