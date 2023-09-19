import json
from pprint import pprint

import requests

def get_hh_data_employers(keyword):
    """Список работодателей"""
    list_employers = []
    url_hh = "https://api.hh.ru/employers"
    params_hh = {"text": keyword,
                 "area": 113,
                 "page": 0,
                 "per_page": 100
                 }
    response = requests.get(url=url_hh, params=params_hh)
    response_json = response.json()
    for item in response_json['items']:
        list_employers.append(item)
    return list_employers


def get_employer_id():
    """id работодателей"""
    EMPLOYERS_ID = []
    with open("employers.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    for emloyer in data:
        if len(EMPLOYERS_ID) < 10:
            EMPLOYERS_ID.append(emloyer["id"])
    return EMPLOYERS_ID


def add_json_employers(list_vacancy):
    """Добавление списка работодателей в json"""
    with open('employers.json', 'w', encoding='utf-8') as f:
        json.dump(list_vacancy, f, ensure_ascii=False)


def get_hh_data(employer_id):
    """Получает данные с hh.ru по API, принимает номер компании"""
    url_hh = "https://api.hh.ru/vacancies"
    params_hh = {"employer_id": employer_id,
                 "area": 113,
                 "page": 0,
                 "per_page": 100
                 }
    response = requests.get(url=url_hh, params=params_hh)
    response_json = response.json()
    list_vacancy = []
    for item in response_json['items']:
        list_vacancy.append(item)
    return list_vacancy
# list_vacancy = []
# ll_ = get_hh_data(['4931636', '2603468', '4679771', '3027217', '2690637', '3896407', '5110456', '1048376', '8932785', '1083682'])
# for lll_ in ll_:
#     with open('vacancy.json', 'w', encoding='utf-8') as f:
#         json.dump(list_vacancy, f)
#     with open('vacancy.json', 'r', encoding='utf-8') as f:
#         json.load(f)
#         list_vacancy.append(lll_)
#     with open('vacancy.json', 'w', encoding='utf-8') as f:
#         json.dump(list_vacancy, f)
# print(len(list_vacancy))
# print(len(ll_))


def add_json_vacancy(employer_ids):
    """
    метод довавления вакансий в json-файл
    """
    list_vacancies = []
    for employer_id in employer_ids:
        with open('vacancy.json', 'w', encoding='utf-8') as f:
            json.dump(list_vacancies, f)
        with open('vacancy.json', 'r', encoding='utf-8') as f:
            json.load(f)
            list_vacancies.append(employer_id)
        with open('vacancy.json', 'w', encoding='utf-8') as f:
            json.dump(list_vacancies, f)
    return list_vacancies



def delete_json():
    open('vacancy.json', 'w').close()
    open('employers.json', 'w').close()

def insert_data_to_tables(cur):
    """функция для наполнения таблиц данными"""
    try:
        with open('employers.json') as json_file:
            employers = json.load(json_file)
            for employer in employers:
                employer_id = employer['id']
                company_name = employer['name']
                vacancies_url = employer['vacancies_url']
                open_vacancies = employer['open_vacancies']
            cur.execute("INSERT INTO suppliers VALUES (%s, %s, %s, %s)",
                        (employer_id, company_name, vacancies_url, open_vacancies))

        with open('vacancy.json.json') as json_file:
            vacancies = json.load(json_file)
            for vacancy in vacancies:
                vacancy_id = vacancy['id']
                vacancy_name = vacancy['name']
                salary_from = vacancy['salary_from']
                salary_to = vacancy['salary_to']
                employer_id = vacancy['employer']['id']
                url = vacancy['alternate_url']
            cur.execute("INSERT INTO suppliers VALUES (%s, %s, %s, %s, %s, %s)",
                        (vacancy_id, employer_id, vacancy_name, salary_from, salary_to, url))
    except:
        ""
