from src.vacancy import Vacancy
from src.json_saver import JSONSaver
from src.hh_api import HH_API

hh = HH_API()
vacancies = hh.get_vacancies('python')
json_saver = JSONSaver()