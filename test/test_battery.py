import unittest
from datetime import date

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


class TestNubbinBattery(unittest.TestCase):
    def test_needs_service(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 5)
        
        battery = NubbinBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_does_not_need_service(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 3)
        
        battery = NubbinBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 3)
        
        battery = SpindlerBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_does_not_need_service(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 1)
        
        battery = SpindlerBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()
