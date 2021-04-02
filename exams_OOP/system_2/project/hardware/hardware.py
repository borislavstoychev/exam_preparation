from project.software.software import Software


class Hardware:
    """• name - string
    • type - string ("Heavy" or "Power")
    • capacity - int
    • memory - int
    • software_components - empty list upon initialization"""

    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def is_possible_to_install(self, software):
        total_memory_use = 0
        total_capacity_use = 0
        for s in self.software_components:
            total_memory_use += s.memory_consumption
            total_capacity_use += s.capacity_consumption
        total_memory_use += software.memory_consumption
        total_capacity_use += software.capacity_consumption
        if total_memory_use <= self.memory and total_capacity_use <= self.capacity:
            return True
        else:
            return False

    def install(self, software: Software):
        if not self.is_possible_to_install(software):
            raise Exception("Software cannot be installed")
        self.software_components.append(software)

    def uninstall(self, software: Software):
        self.software_components.remove(software)