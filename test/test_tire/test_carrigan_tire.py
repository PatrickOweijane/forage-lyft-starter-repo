import unittest

from tire.carrigan_tire import CarriganTire


class TestCarriganTire(unittest.TestCase):
    def test_needs_service(self):
        worn_status = [0, 0.9, 0.2, 0.5]
        tire = CarriganTire(worn_status)
        self.assertTrue(tire.needs_service())

        worn_status = [1, 1, 1, 1]
        tire = CarriganTire(worn_status)
        self.assertTrue(tire.needs_service())

    def test_does_not_need_service(self):
        worn_status = [0, 0.3, 0.7, 0]
        tire = CarriganTire(worn_status)
        self.assertFalse(tire.needs_service())
