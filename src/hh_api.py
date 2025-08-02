from abc import ABC, abstractmethod

import requests


class AbstractAPI(ABC):

    @abstractmethod
    def connect(self, text):
        pass

    @abstractmethod
    def get_vacancies(self, text, multi_page):
        pass


class HH_API(AbstractAPI):
    def __init__(self, page = 0):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__params = {'page' : page, 'per_page' : 15}

    def connect(self, text):
        self.__params['text'] = text
        response = requests.get(self.__url, params = self.__params)
        return response

    def get_vacancies(self, text, multi_page = 0):
        all_vacancies = []
        while self.__params['page'] < multi_page:
            vacancies = self.connect(text).json()['items']
            all_vacancies.extend(vacancies)
            self.__params['page'] += 1
        return all_vacancies

if __name__ == 'main':
    hh = HH_API()
    print(hh.get_vacancies('python', 0 ))