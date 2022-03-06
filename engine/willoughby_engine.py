from engine.engine import Engine


class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage):
        self._last_service_mileage = last_service_mileage
        self._current_mileage = current_mileage

    def needs_service(self):
        return self._current_mileage - self._last_service_mileage > 60000

    @property
    def current_mileage(self):
        return self._current_mileage

    @current_mileage.setter
    def current_mileage(self, new_current_mileage):
        if isinstance(new_current_mileage, int):
            self._current_mileage = new_current_mileage
        else:
            print('Please enter a valid integer')

    @property
    def last_service_mileage(self):
        return self._last_service_mileage

    @last_service_mileage.setter
    def last_service_mileage(self, new_last_service_mileage):
        if isinstance(new_last_service_mileage, int):
            self._last_service_mileage = new_last_service_mileage
        else:
            print('Please enter a valid integer')
