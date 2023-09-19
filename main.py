import psycopg2

from config import config
from db_manager import DBManager
from func import get_hh_data_employers, add_json_employers, get_hh_data, get_employer_id, delete_json, add_json_vacancy, \
    insert_data_to_tables_vacancies, insert_data_to_tables_employers

script_file = 'create_table.sql'
db_name = 'my_new_cw_5'

params = config()
conn = None

db = DBManager()
db.create_db(params, db_name)  # Создаем базу данных

params.update({'dbname': db_name})

delete_json()
# Работа с компаниями
user_keyword_employers = input('Введите ключевое слово, для поиска компаний: ')
get_employers = get_hh_data_employers(user_keyword_employers)  # Список компаний
json_employers = add_json_employers(get_employers[0:10])  # Сохранение в JSON файл
employer_ids = get_employer_id()
# Работа с вакансиями
vacancies = get_hh_data(employer_ids)
vac = add_json_vacancy(vacancies)  # Сохранение данных о вакансиях в JSON файле
# Работа с таблицами
try:
    with psycopg2.connect(**params) as conn:
        with conn.cursor() as cur:
            # Создание таблиц
            # db.drop_tables(cur)
            db.create_tables(cur, script_file)
            # Наполняем таблицу данными
            insert_data_to_tables_employers(cur)
            insert_data_to_tables_vacancies(cur)
            # Работа с пользователем
            user_input_get_companies_and_vacancies = input(
                "Вывести список всех компаний и количество вакансий у каждой компании? y/n ").lower()
            if user_input_get_companies_and_vacancies == "y":
                db.get_companies_and_vacancies_count(cur)
            user_input_get_all_vacancies = input("Вывести список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию? y/n ").lower()
            if user_input_get_all_vacancies == "y":
                db.get_all_vacancies(cur)
            user_input_get_avg_salary = input("Вывести среднюю зарплату по вакансиям? y/n ").lower()
            if user_input_get_avg_salary == "y":
                 db.get_avg_salary(cur)
            user_input_get_vacancies_with_higher_salary = input("Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям? y/n ").lower()
            if user_input_get_vacancies_with_higher_salary == "y":
                db.get_vacancies_with_higher_salary(cur)
            user_get_vacancies_with_keyword = input(
                    "Набери слово для поиска вакансий: ").lower()
            db.get_vacancies_with_keyword(cur, user_get_vacancies_with_keyword)

except(Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()

