
class Vacancy:

    def __init__(self, name, link, salary, description):
        self.name = name
        self.link = link
        self.__validate(salary)
        self.description = description


    def __validate(self, salary):
        if salary:
            self.salary_from = salary['from'] if salary['from'] else 0
            self.salary_to = salary['to'] if salary['to'] else 0
        else:
            self.salary_from = 0
            self.salary_to = 0

    def __lt__(self, other):
        '''Знак меньше <'''
        return self.salary_from < other.salary_from
