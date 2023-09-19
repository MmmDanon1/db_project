import json

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

def add_json_vacancy(employer_ids):
    """
    метод довавления вакансий в json-файл
    """
    list_vacancies = []
    for employer_id in employer_ids:
        if employer_id != []:
            with open('vacancy.json', 'w', encoding='utf-8') as f:
                json.dump(list_vacancies, f, ensure_ascii=False)
            with open('vacancy.json', 'r', encoding='utf-8') as f:
                json.load(f)
                list_vacancies.append(employer_id)
            with open('vacancy.json', 'w', encoding='utf-8') as f:
                json.dump(list_vacancies, f, ensure_ascii=False)

def delete_json():
    open('vacancy.json', 'w').close()
    open('employers.json', 'w').close()

def insert_data_to_tables_employers(cur):
    """функция для наполнения таблиц данными"""
    try:
        with open('employers.json', 'r', encoding='utf-8') as json_file:
            employers = json.load(json_file)
            for employer in employers:
                employer_id = employer['id']
                company_name = employer['name']
                employer_url = employer["alternate_url"]
                open_vacancies = employer['open_vacancies']
                cur.execute("INSERT INTO employers VALUES (%s, %s, %s, %s)",
                            (employer_id, company_name, employer_url, open_vacancies))
    except:
        ""

def insert_data_to_tables_vacancies(cur):
    """функция для наполнения таблиц данными"""
    try:
        with open('vacancy.json', 'r', encoding='utf-8') as json_file:
            vacancies = json.load(json_file)
            for vacancy in vacancies:
                vacancy_id = vacancy['id']
                vacancy_name = vacancy['name']
                try:
                    vacancy_salary_from = vacancy['salary']['from']
                except:
                    vacancy_salary_from = 0
                try:
                    vacancy_salary_to = vacancy['salary']['to']
                except:
                    vacancy_salary_to = 0
                employer_id = vacancy['employer']['id']
                url = vacancy['alternate_url']
                cur.execute("INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s, %s)",
                            (vacancy_id, employer_id, vacancy_name, vacancy_salary_from, vacancy_salary_to, url))
    except:
        ""
