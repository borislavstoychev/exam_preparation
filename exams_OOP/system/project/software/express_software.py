from project.software.software import Software


class ExpressSoftware(Software):

    def __init__(self,  name, capacity_consumption, memory_consumption):

        super().__init__(name=name,
                         type="Express",
                         capacity_consumption=int(capacity_consumption),
                         memory_consumption=int(memory_consumption*2))

