from numpy import isin
from engine.engine import Engine
from battery.battery import Battery

class Car:
    def __init__(self, engine, battery):
        self._engine = engine
        self._battery = battery

    def needs_service(self):
        return self._engine.needs_service() or self._battery.needs_service()

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, new_engine):
        if isinstance(new_engine, Engine):
            self._engine = new_engine
        else:
            print('Please enter a valid engine')

    @property
    def battery(self):
        return self._battery

    @battery.setter
    def battery(self, new_battery):
        if isinstance(new_battery, Battery):
            self._battery = new_battery
        else:
            print('Please enter a valid battery')
