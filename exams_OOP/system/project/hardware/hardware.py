from project.software.software import Software


class Hardware:

    """
     • name - string
    • type - string ("Heavy" or "Power")
    • capacity - int
    • memory - int
    • software_components - empty list upon initialization
    """
    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def is_valid(self, new_memory, new_capacity):
        total_consumption_memory = sum(m.memory_consumption for m in self.software_components) + new_memory
        total_consumption_capacity = sum(c.capacity_consumption for c in self.software_components) + new_capacity
        if total_consumption_capacity > self.capacity or total_consumption_memory > self.memory:
            return False
        else:
            return True

    def install(self, software: Software):
        if not self.is_valid(software.memory_consumption, software.capacity_consumption):
            raise Exception("Software cannot be installed")
        self.software_components.append(software)

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)

