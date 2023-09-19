import json
from pprint import pprint

from func import get_hh_data_employers, add_json_employers, get_hh_data, get_employer_id, add_json_vacancy, delete_json

delete_json()
user_keyword_employers = input('Введите ключевое слово, для поиска компаний: ')
get_employers = get_hh_data_employers(user_keyword_employers) # Список компаний
json_employers = add_json_employers(get_employers) # Сохранение в JSON файл
employer_ids = get_employer_id()
print(employer_ids)
for employer_id in employer_ids: # Получаем вакансии по id компаний
    hh_ = get_hh_data(employer_id)
    if hh_ != []:
        add_json_vacancy(hh_)

# if hh_ != []:
#     add_json_vacancy(hh_)
