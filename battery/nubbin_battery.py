from battery.battery import Battery
from datetime import date


class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self._last_service_date = last_service_date
        self._current_date = current_date

    def needs_service(self):
        service_threshold_date = self._last_service_date.replace(year=self._last_service_date.year + 4)
        return service_threshold_date < self._current_date

    @property
    def last_service_date(self):
        return self._last_service_date

    @last_service_date.setter
    def last_service_date(self, new_last_service_date):
        if isinstance(new_last_service_date, date):
            self._last_service_date = new_last_service_date
        else:
            print('Please enter a valid date')

    @property
    def current_date(self):
        return self._current_date

    @current_date.setter
    def current_date(self, new_current_date):
        if isinstance(new_current_date, date):
            self._current_date = new_current_date
        else:
            print('Please enter a valid date')
