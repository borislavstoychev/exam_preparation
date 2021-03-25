from project.hardware.hardware import Hardware
from project.software.express_software import ExpressSoftware
import unittest


class HardwareTest(unittest.TestCase):

    def setUp(self) -> None:
        self.hardware = Hardware("HDD", "Heavy", 100, 8)

    def test_constructor(self):
        self.assertEqual("HDD", self.hardware.name)
        self.assertEqual("Heavy", self.hardware.type)
        self.assertEqual(100, self.hardware.capacity)
        self.assertEqual(8, self.hardware.memory)
        self.assertEqual([], self.hardware.software_components)

    def test_installing_software(self):
        software = ExpressSoftware("linux", 20, 4)
        self.hardware.install(software)
        self.assertEqual([software], self.hardware.software_components)

    def test_rise_exception_installing_software(self):
        software = ExpressSoftware("Linux", 120, 4)
        software_1 = ExpressSoftware("Windows", 20, 16)
        with self.assertRaises(Exception) as ex:
            self.hardware.install(software)
            self.hardware.install(software_1)
        self.assertEqual("Software cannot be installed", ex.exception.args[0])

    def test_uninstall_software(self):
        software = ExpressSoftware("Linux", 1, 2)
        software_1 = ExpressSoftware("Windows", 5, 2)
        self.hardware.install(software)
        self.hardware.install(software_1)
        self.hardware.uninstall(software)
        self.hardware.uninstall(software_1)


if __name__ == "__main__":
    unittest.main()
