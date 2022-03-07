from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, worn_status):
        self._worn_status = worn_status

    def needs_service(self):
        return any(status >= 0.9 for status in self._worn_status)

    @property
    def worn_status(self):
        return self._worn_status

    @worn_status.setter
    def worn_status(self, new_worn_status):
        if isinstance(new_worn_status, list) and \
            len(new_worn_status) == 4 and \
            all((isinstance(e, float) or isinstance(e, int)) and 0 <= e <= 1 for e in new_worn_status):
            self._worn_status = new_worn_status
        else:
            print('Please enter a valid array of floats of length 4')
