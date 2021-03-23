class Everland:

    def __init__(self, rooms=None):
        if rooms is None:
            rooms = []
        self.rooms = rooms

    def add_room(self, room: "Room"):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.expenses + room.room_cost
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        result =[]
        for room in self.rooms:
            total_cost = room.expenses + room.room_cost
            if room.budget < total_cost:
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(room)
            else:
                room.budget -= total_cost
                result.append(f"{room.family_name} paid {total_cost:.2f}$ and have {(room.budget + total_cost):.2f}$ left.")
        return "\n".join(result)

    @staticmethod
    def get_children_and_appliances(room):
        result = []
        child_cost = 0
        if room.__class__.__name__ == "YoungCoupleWithChildren":
            n = 1
            for r in room.children:
                child_cost += r.cost * 30
                result.append(f"--- Child {n} monthly cost: {(r.cost * 30):.2f}$")
                n += 1
        result.append(f"--- Appliances monthly cost: {(room.expenses - child_cost):.2f}$")
        return "\n".join(result)

    def status(self):
        room_status = []
        all_people_in_the_hotel = 0
        for room in self.rooms:
            all_people_in_the_hotel += room.members_count
            room_status.append(f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n"
                               f"{self.get_children_and_appliances(room)}")

        return f"Total population: {all_people_in_the_hotel}\n" + "\n".join(room_status)

