import unittest
from datetime import date

from car_factory import CarFactory


class TestCalliope(unittest.TestCase):
    def test_needs_service(self):
        # Case 1 (10): Battery needs service, engine does not need service

        today = date.today()
        last_service_date = today.replace(year=today.year - 3)        
        last_service_mileage = 0
        current_mileage = 29999

        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service() and car.battery.needs_service() and not car.engine.needs_service())

        # Case 2 (01): Battery does not need service, engine needs service

        today = date.today()
        last_service_date = today.replace(year=today.year - 1)        
        last_service_mileage = 0
        current_mileage = 30001

        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service() and not car.battery.needs_service() and car.engine.needs_service())

        # Case 3 (11): Battery needs service, engine needs service

        today = date.today()
        last_service_date = today.replace(year=today.year - 3)        
        last_service_mileage = 0
        current_mileage = 30001

        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service() and car.battery.needs_service() and car.engine.needs_service())

    def test_does_not_need_service(self):
        # Case 4 (00): Battery does not need service, engine does not need service
        today = date.today()
        last_service_date = today.replace(year=today.year - 1)        
        last_service_mileage = 0
        current_mileage = 29999

        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service() or car.battery.needs_service() or car.engine.needs_service())


class TestGlissade(unittest.TestCase):
    def test_needs_service(self):
        # Case 1 (10): Battery needs service, engine does not need service

        today = date.today()
        last_service_date = today.replace(year=today.year - 3)        
        last_service_mileage = 0
        current_mileage = 59999

        car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service() and car.battery.needs_service() and not car.engine.needs_service())

        # Case 2 (01): Battery does not need service, engine needs service

        today = date.today()
        last_service_date = today.replace(year=today.year - 1)        
        last_service_mileage = 0
        current_mileage = 60001

        car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service() and not car.battery.needs_service() and car.engine.needs_service())

        # Case 3 (11): Battery needs service, engine needs service

        today = date.today()
        last_service_date = today.replace(year=today.year - 3)        
        last_service_mileage = 0
        current_mileage = 60001

        car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service() and car.battery.needs_service() and car.engine.needs_service())

    def test_does_not_need_service(self):
        # Case 4 (00): Battery does not need service, engine does not need service
        today = date.today()
        last_service_date = today.replace(year=today.year - 1)        
        last_service_mileage = 0
        current_mileage = 59999

        car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service() or car.battery.needs_service() or car.engine.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_needs_service(self):
        # Case 1 (10): Battery needs service, engine does not need service

        today = date.today()
        last_service_date = today.replace(year=today.year - 3)        
        warning_light_on = False

        car = CarFactory.create_palindrome(today, last_service_date, warning_light_on)
        self.assertTrue(car.needs_service() and car.battery.needs_service() and not car.engine.needs_service())

        # Case 2 (01): Battery does not need service, engine needs service

        today = date.today()
        last_service_date = today.replace(year=today.year - 1)        
        warning_light_on = True

        car = CarFactory.create_palindrome(today, last_service_date, warning_light_on)
        self.assertTrue(car.needs_service() and not car.battery.needs_service() and car.engine.needs_service())

        # Case 3 (11): Battery needs service, engine needs service

        today = date.today()
        last_service_date = today.replace(year=today.year - 3)        
        warning_light_on = True

        car = CarFactory.create_palindrome(today, last_service_date, warning_light_on)
        self.assertTrue(car.needs_service() and car.battery.needs_service() and car.engine.needs_service())

    def test_does_not_need_service(self):
        # Case 4 (00): Battery does not need service, engine does not need service
        today = date.today()
        last_service_date = today.replace(year=today.year - 1)        
        warning_light_on = False

        car = CarFactory.create_palindrome(today, last_service_date, warning_light_on)
        self.assertFalse(car.needs_service() or car.battery.needs_service() or car.engine.needs_service())


class TestRorschach(unittest.TestCase):
    def test_needs_service(self):
        # Case 1 (10): Battery needs service, engine does not need service

        today = date.today()
        last_service_date = today.replace(year=today.year - 5)        
        last_service_mileage = 0
        current_mileage = 59999

        car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service() and car.battery.needs_service() and not car.engine.needs_service())

        # Case 2 (01): Battery does not need service, engine needs service

        today = date.today()
        last_service_date = today.replace(year=today.year - 3)        
        last_service_mileage = 0
        current_mileage = 60001

        car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service() and not car.battery.needs_service() and car.engine.needs_service())

        # Case 3 (11): Battery needs service, engine needs service

        today = date.today()
        last_service_date = today.replace(year=today.year - 5)        
        last_service_mileage = 0
        current_mileage = 60001

        car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service() and car.battery.needs_service() and car.engine.needs_service())

    def test_does_not_need_service(self):
        # Case 4 (00): Battery does not need service, engine does not need service
        today = date.today()
        last_service_date = today.replace(year=today.year - 3)        
        last_service_mileage = 0
        current_mileage = 59999

        car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service() or car.battery.needs_service() or car.engine.needs_service())


class TestThovex(unittest.TestCase):
    def test_needs_service(self):
        # Case 1 (10): Battery needs service, engine does not need service

        today = date.today()
        last_service_date = today.replace(year=today.year - 5)        
        last_service_mileage = 0
        current_mileage = 29999

        car = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service() and car.battery.needs_service() and not car.engine.needs_service())

        # Case 2 (01): Battery does not need service, engine needs service

        today = date.today()
        last_service_date = today.replace(year=today.year - 3)        
        last_service_mileage = 0
        current_mileage = 30001

        car = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service() and not car.battery.needs_service() and car.engine.needs_service())

        # Case 3 (11): Battery needs service, engine needs service

        today = date.today()
        last_service_date = today.replace(year=today.year - 5)        
        last_service_mileage = 0
        current_mileage = 30001

        car = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service() and car.battery.needs_service() and car.engine.needs_service())

    def test_does_not_need_service(self):
        # Case 4 (00): Battery does not need service, engine does not need service
        today = date.today()
        last_service_date = today.replace(year=today.year - 3)        
        last_service_mileage = 0
        current_mileage = 29999

        car = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service() or car.battery.needs_service() or car.engine.needs_service())


if __name__ == '__main__':
    unittest.main()
