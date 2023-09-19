import psycopg2

from config import config

dbname = 'db_manager'
params = open("database.ini", "r")
class DBManager:
    """Класс для работы с БД"""


    def get_companies_and_vacancies_count(self, cur):
        """Получает список всех компаний и количество вакансий у каждой компании"""

        cur.execute("SELECT company_name, open_vacancies FROM employers")

    def get_all_vacancies(self, cur):
        """Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию"""

        cur.execute("SELECT vacancies.vacancy_name, employers.company_name, vacancies.salary_from, vacancies.salary_to, vacancies.url FROM vacancies"
                    "JOIN employers USING(employer_id)"
                    )

    def get_avg_salary(self, cur):
        """Получает среднюю зарплату по вакансиям"""

        cur.execute("SELECT AVG(salary_from), AVG(salary_to) FROM vacancies")

    def get_vacancies_with_higher_salary(self, cur):
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""

        cur.execute("SELECT * FROM vacancies"
                    "WHERE salary_from > AVG(salary_from) AND salary_to > AVG(salary_to)"
                    )

    def get_vacancies_with_keyword(self, cur, keyword):
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова"""

        cur.execute("SELECT * FROM vacancies"
                    f"WHERE vacancy_name LIKE '{keyword}%' or LIKE '%{keyword}' or LIKE '%{keyword}%')"
                    )

    def create_tables(self, cur, script_file):
        """Создает таблицу"""

        with open(script_file, "r") as f:
            cur.execute(f.read())

    def drop_tables(self, cur):
        """Удаляет таблицу"""

        cur.execute("DROP TABLE vacancies;"
                    "DROP TABLE employers")

    def create_db(self):
        """Создает Базу Данных"""

        conn = psycopg2.connect(dbname='db_manager', **params)
        conn.autocommit = True
        cur = conn.cursor()

        cur.execute(f"DROP DATABASE {dbname}")
        cur.execute(f"CREATE DATABASE {dbname}")

        conn.close()