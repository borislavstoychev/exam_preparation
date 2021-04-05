from project.card.card import Card


class CardRepository:

    def __init__(self):
        self.cards = []

    @property
    def count(self):
        return len(self.cards)

    def add(self, card: Card):
        if self.find(card.name):
            raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)

    def remove(self, card: str):
        if card == "":
            raise ValueError("Card cannot be an empty string!")
        self.cards.remove(self.find(card))

    def find(self, name: str):
        for c in self.cards:
            if name == c.name:
                return c
