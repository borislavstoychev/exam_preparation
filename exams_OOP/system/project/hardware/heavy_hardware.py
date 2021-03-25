from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):

    def __init__(self, name, capacity, memory):
        super().__init__(name=name,
                         type="Heavy",
                         capacity=int(capacity*2),
                         memory=int(memory*0.75))
