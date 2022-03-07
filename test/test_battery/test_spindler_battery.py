import unittest
from datetime import date

from battery.spindler_battery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 4)
        
        battery = SpindlerBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_does_not_need_service(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 2)
        
        battery = SpindlerBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()
