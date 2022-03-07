import unittest

from tire.octoprime_tire import OctoprimeTire


class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service(self):
        worn_status = [1]*3 + [0]
        tire = OctoprimeTire(worn_status)
        self.assertTrue(tire.needs_service())

        worn_status = [3/4]*4
        tire = OctoprimeTire(worn_status)
        self.assertTrue(tire.needs_service())

        worn_status = [3/4]*3 + [1]
        tire = OctoprimeTire(worn_status)
        self.assertTrue(tire.needs_service())

    def test_does_not_need_service(self):
        worn_status = [0]*4
        tire = OctoprimeTire(worn_status)
        self.assertFalse(tire.needs_service())

        worn_status = [3/4]*3 + [0]
        tire = OctoprimeTire(worn_status)
        self.assertFalse(tire.needs_service())
