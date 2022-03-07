import unittest

from engine.willoughby_engine import WilloughbyEngine


class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service(self):
        last_service_mileage = 0
        current_mileage = 60001
        
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())

    def test_does_not_need_service(self):
        last_service_mileage = 0
        current_mileage = 59999
        
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()
