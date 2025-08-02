from abc import ABC, abstractmethod

import json

class AbsJSON(ABC):
    @abstractmethod
    def write_vacancies(self, vacancies: list[dict]):
        pass

    @abstractmethod
    def read_vacancies(self):
        pass

    @abstractmethod
    def delete_vacancies(self):
        pass


class JSONSaver(AbsJSON):

    def __init__(self, filepath ='../data/vacancies.json'):
        self.__filepath = filepath


    def write_vacancies(self, vacancies: list[dict]):
        vacancies_filter = []
        for vacancy in vacancies:
            vacancies_filter.append({"name": vacancy["name"],
                                     "link": vacancy["alternate_url"],
                                     "salary": vacancy["salary"],
                                     "description": vacancy["snippet"]["requirement"]})
        with open(self.__filepath, "w", encoding="utf-8") as file:
            json.dump(vacancies_filter, file)

    def read_vacancies(self):
        pass

    def delete_vacancies(self):
        pass
