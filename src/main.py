from src.vacancy import Vacancy
from src.json_saver import JSONSaver
from src.hh_api import HH_API

def main():
    query_yn = str(input("Здравствуйте! Хотите получить вакансии по запросу? Да/Нет\n"))
    if query_yn.lower() == 'нет' or query_yn.lower() == 'no':
        print('Извините за беспокойство, до свидания!')
        return 0
    elif query_yn.lower() == 'да' or  query_yn.lower() == 'yes':
        search_query = str(input("Введите ключевые слова для поиска:\n"))






main()
'''hh = HH_API()
vacancies = hh.get_vacancies('python', 1)
json_saver = JSONSaver()
json_saver.write_vacancies(vacancies)'''