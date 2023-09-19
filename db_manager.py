import psycopg2

from config import config

dbname = 'db_manager'
params = open("database.ini", "r")
class DBManager:
    """Класс для работы с БД"""


    def get_companies_and_vacancies_count(self):
        """Получает список всех компаний и количество вакансий у каждой компании"""
        pass

    def get_all_vacancies(self):
        """Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию"""
        pass


    def get_avg_salary(self):
        """Получает среднюю зарплату по вакансиям"""
        pass

    def get_vacancies_with_higher_salary(self):
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        pass

    def get_vacancies_with_keyword(self, keyword):
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова"""
        pass

    def create_tables(self):
        """Создает таблицу"""
        pass

    def drop_tables(self):
        """Удаляет таблицу"""
        pass

    def create_db(self):
        """Создает Базу Данных"""

        conn = psycopg2.connect(dbname='db_manager', **params)
        conn.autocommit = True
        cur = conn.cursor()

        cur.execute(f"DROP DATABASE {dbname}")
        cur.execute(f"CREATE DATABASE {dbname}")

        conn.close()