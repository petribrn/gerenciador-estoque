from abc import ABC, abstractmethod
import pickle

class AbstractDAO(ABC):

    @abstractmethod
    def __init__(self, datasource=''):
        self.__datasource = datasource
        self.__cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))

    def __load(self):
        self.__cache = pickle.load(open(self.__datasource, 'rb'))

    def persist(self, key, obj):
        self.__cache[key] = obj
        self.__dump()

    def remove(self, key):
        self.__cache.pop(key)
        self.__dump()

    def get_all(self):
        return self.__cache.values()