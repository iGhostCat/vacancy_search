from src.vacancy import Vacancy
from src.json_saver import JSONSaver
from src.hh_api import HH_API

def main():
    query_yn = str(input("Здравствуйте! Хотите получить вакансии по запросу? Да/Нет\n"))
    print(query_yn)





main()
'''hh = HH_API()
vacancies = hh.get_vacancies('python', 1)
json_saver = JSONSaver()
json_saver.write_vacancies(vacancies)'''