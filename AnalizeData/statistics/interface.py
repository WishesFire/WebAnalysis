from abc import ABC, abstractmethod

# Graphics: 1) Histogram, 2) Curved, 3) Column


class IFabricStatistic(ABC):
    @abstractmethod
    def prepare_data(self, data_from_elastic) -> dict:
        pass

    @abstractmethod
    def execute_stat(self):
        pass
