from .interface import IFabricStatistic


class Statistics(IFabricStatistic):
    def prepare_data(self, data_from_elastic) -> dict:
        pass

    def execute_stat(self):
        pass

    def start(self):
        pass
