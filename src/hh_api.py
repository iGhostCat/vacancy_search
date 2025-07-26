from abc import ABC, abstractmethod

import requests


class AbstractAPI(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass


class HH_API(AbstractAPI):
    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__params = {'page' : 0, 'per_page' : 30}

    def connect(self, text, page = 0):
        self.__params['text'] = text
        self.__params['page'] = page
        result = requests.get(self.__url, params = self.__params)
        return result


