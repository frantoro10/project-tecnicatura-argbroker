from abc import ABC, abstractmethod

class DataAccessDAO(ABC):
    @abstractmethod
    def __init__(self, db_conn: bool = None, sql_query: bool =None):
        pass
    
    @abstractmethod
    def get(self, id: int):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def create(self, object):
        pass

    @abstractmethod
    def update(self, object):
        pass

    @abstractmethod
    def delete(self, object):
        pass

