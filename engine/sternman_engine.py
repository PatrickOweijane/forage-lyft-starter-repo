from engine.engine import Engine


class SternmanEngine(Engine):
    def __init__(self, warning_light_on):
        self._warning_light_on = warning_light_on

    def needs_service(self):
        return self._warning_light_on

    @property
    def warning_light_on(self):
        return self._warning_light_on

    @warning_light_on.setter
    def warning_light_on(self, new_warning_light_on):
        if isinstance(new_warning_light_on, bool):
            self._warning_light_on = new_warning_light_on
        else:
            print('Please enter a valid boolean')
