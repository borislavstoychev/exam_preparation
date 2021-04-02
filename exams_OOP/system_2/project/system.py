from project.hardware.power_hardware import PowerHardware
from project.hardware.heavy_hardware import HeavyHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:

    _hardware = []
    _software = []


    @staticmethod
    def register_power_hardware(name:str, capacity:int, memory:int):
        hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(hardware)

    @staticmethod
    def register_heavy_hardware(name:str, capacity:int, memory:int):
        hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(hardware)
    @staticmethod
    def register_express_software(hardware_name: str, name:str, capacity_consumption:int, memory_consumption:int):
        hardware = [h for h in System._hardware if h.name == hardware_name]
        if not hardware:
            return "Hardware does not exist"
        try:
            software = ExpressSoftware(name, capacity_consumption, memory_consumption)
            hardware[0].install(software)
            System._software.append(software)
        except Exception as ex:
            return str(ex)

    @staticmethod
    def register_light_software(hardware_name: str, name:str, capacity_consumption:int, memory_consumption:int):
        hardware = [h for h in System._hardware if h.name == hardware_name]
        if not hardware:
            return "Hardware does not exist"
        try:
            software = LightSoftware(name, capacity_consumption, memory_consumption)
            hardware[0].install(software)
            System._software.append(software)
        except Exception as ex:
            return str(ex)

    @staticmethod
    def release_software_component(hardware_name:str, software_name:str):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = [s for s in System._software if s.name == software_name][0]
            hardware.uninstall(software)
            System._software.remove(software)

        except IndexError:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        return f"System Analysis\n" \
               f"Hardware Components: {len(System._hardware)}\n" \
               f"Software Components: {len(System._software)}\n" \
               f"Total Operational Memory: {sum(s.memory_consumption for s in System._software)} / {sum(h.memory for h in System._hardware)}\n" \
               f"Total Capacity Taken: {sum(s.capacity_consumption for s in System._software)} / {sum(h.capacity for h in System._hardware)}"

    @staticmethod
    def get_software(hardware):
        software = []
        for s in hardware.software_components:
            software.append(s.name)
        if software:
            return ", ".join(software)

    @staticmethod
    def system_split():
        result = ""
        for hardware in  System._hardware:
            result += f"Hardware Component - {hardware.name}\n" \
                      f"Express Software Components: {len([h for h in hardware.software_components if h.__class__.__name__ == 'ExpressSoftware'])}\n" \
                      f"Light Software Components: {len([h for h in hardware.software_components if h.__class__.__name__ == 'LightSoftware'])}\n" \
                      f"Memory Usage: {sum([h.memory_consumption for h in hardware.software_components])} / {hardware.memory}\n" \
                      f"Capacity Usage: {sum([h.capacity_consumption for h in hardware.software_components])} / {hardware.capacity}\n" \
                      f"Type: {hardware.type}\n" \
                      f"Software Components: {System.get_software(hardware)}"

        return result
