from abc import ABC

class Parser(ABC):
    def __init__(self, file_worker):
        self.file_worker = file_worker

    @classmethod
    def load_vacancies(cls, keyword):
        pass


import requests


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self, file_worker):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []
        super().__init__(file_worker)


    def load_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1


class Vacancy():
    def __init__(self, name, url, pay, description):
        self.name = name
        self.url = url
        self.pay = pay
        self.description = description

