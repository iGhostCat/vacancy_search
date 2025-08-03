
class Vacancy:

    def __init__(self, name, link, salary, description):
        self.name = name
        self.link = link
        self.salary = salary
        self.description = description


    def __validate(self, salary):
        if salary:
            self.salary_from = salary['from'] if salary['from'] else 0
            self.salary_to = salary['to'] if salary['to'] else 0
        else:
            self.salary_from = 0
            self.salary_to = 0