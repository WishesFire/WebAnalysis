from .interface import IFabricStatistic
from AnalizeData.models.database import DataBase


class Statistics(IFabricStatistic):

    @classmethod
    def _get_data(cls):
        database = DataBase()
        return database.get_all_store()

    def _prepare_data(self):
        pass

    def execute_stat(self, data):
        pass

    def start(self):
        ready_data_elastic = self._get_data()
        self.execute_stat(ready_data_elastic)

    def __str__(self):
        return 'Creating statistics...'
