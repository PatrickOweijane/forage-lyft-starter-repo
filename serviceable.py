from abc import ABC, abstractmethod


class Serviceable(ABC):
    '''
    Interface defining the function needs_service
    '''

    @abstractmethod
    def needs_service(self):
        pass
