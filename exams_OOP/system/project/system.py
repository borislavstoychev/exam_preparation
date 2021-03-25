from project.hardware.power_hardware import PowerHardware
from project.hardware.heavy_hardware import HeavyHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware_names = [name for name in System._hardware if name.name == hardware_name]
        if not hardware_names:
            return "Hardware does not exist"
        try:
            software = ExpressSoftware(name, capacity_consumption, memory_consumption)
            hardware_names[0].install(software)
            System._software.append(software)
        except Exception as error:
            return str(error)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware_names = [name for name in System._hardware if name.name == hardware_name]
        if not hardware_names:
            return "Hardware does not exist"
        try:
            software = LightSoftware(name, capacity_consumption, memory_consumption)
            hardware_names[0].install(software)
            System._software.append(software)
        except Exception as error:
            return str(error)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        try:
            hardware = [hardware for hardware in System._hardware if hardware.name == hardware_name][0]
            software = [software for software in System._software if software.name == software_name][0]
            if software not in hardware.software_components:
                return "Some of the components do not exist"
            hardware.uninstall(software)
            System._software.remove(software)
        except IndexError:
            return 'Some of the components do not exist'

    @staticmethod
    def analyze():
        hard_components = len(System._hardware)
        soft_components = len(System._software)
        used_memory = sum(soft.memory_consumption for soft in System._software)
        total_memory = sum(c.memory for c in System._hardware)
        used_capacity = sum(soft.capacity_consumption for soft in System._software)
        total_capacity = sum(c.capacity for c in System._hardware)
        return f"System Analysis\n" \
               f"Hardware Components: {hard_components}\n" \
               f"Software Components: {soft_components}\n" \
               f"Total Operational Memory: {used_memory} / {total_memory}\n" \
               f"Total Capacity Taken: {used_capacity} / {total_capacity}"

    @staticmethod
    def get_count_hard_components(hardware):
        light = [h for h in hardware.software_components if h.type == "Light"]
        express = [h for h in hardware.software_components if h.type == "Express"]
        result = f"Express Software Components: {len(express)}\nLight Software Components: {len(light)}"
        return result

    @staticmethod
    def get_memory_usage(hardware):
        memory_usage = sum(m.memory_consumption for m in hardware.software_components)
        return int(memory_usage)

    @staticmethod
    def get_capacity_usage(hardware):
        capacity_usage = sum(c.capacity_consumption for c in hardware.software_components)
        return int(capacity_usage)

    @staticmethod
    def get_software_components(hardware):
        result = []
        for s in hardware.software_components:
            result.append(s.name)
        if result:
            return ", ".join(result)

    @staticmethod
    def system_split():
        result = ""
        for hard in System._hardware:
            result += f"Hardware Component - {hard.name}\n"\
                      f"{System.get_count_hard_components(hard)}\n"\
                      f"Memory Usage: {System.get_memory_usage(hard)} / {int(hard.memory)}\n"\
                      f"Capacity Usage: {System.get_capacity_usage(hard)} / {int(hard.capacity)}\n"\
                      f"Type: {hard.type}\n"\
                      f"Software Components: {System.get_software_components(hard)}"
        return result
