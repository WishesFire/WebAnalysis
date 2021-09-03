from abc import ABC, abstractmethod

# Graphics: 1) Histogram, 2) Curved, 3) Column


class IFabricStatistic(ABC):
    @abstractmethod
    def _prepare_data(self, *args, **kwargs) -> dict:
        pass

    @abstractmethod
    def execute_stat(self, *args, **kwargs):
        pass

    @abstractmethod
    def start(self, *args, **kwargs):
        pass
