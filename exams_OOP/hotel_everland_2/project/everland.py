from project.rooms.room import Room


class Everland:

    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.expenses + room.room_cost
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        result = []
        room_to_remove = []
        for room in self.rooms:
            consumption_per_room = room.expenses + room.room_cost
            if consumption_per_room > room.budget:
                room_to_remove.append(room)
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
            else:
                room.budget -= consumption_per_room
                result.append(f"{room.family_name} paid {consumption_per_room:.2f}$"
                              f" and have {(room.budget + consumption_per_room):.2f}$ left.")
            for r in room_to_remove:
                self.rooms.remove(r)
        return "\n".join(result)

    def status(self):
        result = [f"Total population: {sum(r.members_count for r in self.rooms)}"]
        for r in self.rooms:
            result.append(f"{r.family_name} with {r.members_count} members. Budget: {r.budget:.2f}$, Expenses: {r.expenses:.2f}$")
            if r.__class__.__name__ == "YoungCoupleWithChildren":
                result.append("\n".join([f"--- Child {i+1} monthly cost: {(r.children[i].cost*30):.2f}$" for i in range(len(r.children))]))
            result.append(f"--- Appliances monthly cost: {sum(a.get_monthly_expense() for a in r.appliances):.2f}$")
        return "\n".join(result)



