import psycopg2

class DBManager:
    """Класс для работы с БД"""

    def get_companies_and_vacancies_count(self, cur):
        """Получает список всех компаний и количество вакансий у каждой компании"""

        list = []
        cur.execute("SELECT company_name, open_vacancies FROM employers")
        rows = cur.fetchall()
        for row in rows:
            list.append(row)
        for vac in list:
            print(f"Компания: {vac[0]}")
            print(f"Количество вакансий: {vac[1]}")
            print()

    def get_all_vacancies(self, cur):
        """Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию"""
        list = []
        cur.execute(
            "SELECT vacancies.vacancy_name, employers.company_name, vacancies.vacancy_salary_from, vacancies.vacancy_salary_to, vacancies.url FROM vacancies JOIN employers USING (employer_id)"
            )
        rows = cur.fetchall()
        for row in rows:
            list.append(row)
        for vac in list:
            print(f"Название вакансии: {vac[0]}")
            print(f"Имя компании: {vac[1]}")
            print(f"Зарплата от: {vac[2]} до {vac[3]}")
            print(f"Url: {vac[4]}")
            print()

    def get_avg_salary(self, cur):
        """Получает среднюю зарплату по вакансиям"""
        list = []
        cur.execute("SELECT AVG(vacancy_salary_from), AVG(vacancy_salary_to) FROM vacancies")
        rows = cur.fetchall()
        for row in rows:
            list.append(row)
        for vac in list:
            print(f"Средняя зарплата от: {vac[0]} до {vac[1]}")
            print()

    def get_vacancies_with_higher_salary(self, cur):
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        list = []
        cur.execute(
            "SELECT * FROM vacancies WHERE vacancy_salary_from > (SELECT AVG(vacancy_salary_from) FROM vacancies) AND vacancy_salary_to > (SELECT AVG(vacancy_salary_to) FROM vacancies)"
            )
        rows = cur.fetchall()
        for row in rows:
            list.append(row)
        for vac in list:
            print(f"ID вакансии: {vac[0]}")
            print(f"ID компании: {vac[1]}")
            print(f"Название вакансии: {vac[2]}")
            print(f"Зарплата от: {vac[3]} до {vac[4]}")
            print(f"Url: {vac[5]}")
            print()

    def get_vacancies_with_keyword(self, cur, keyword):
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова"""
        list = []
        cur.execute(
            f"(SELECT * FROM vacancies WHERE vacancy_name LIKE '%{keyword}%')"
            )
        rows = cur.fetchall()
        if rows == []:
            print("Ничего не найдено")
        else:
            for row in rows:
                list.append(row)
            for vac in list:
                print(f"ID вакансии: {vac[0]}")
                print(f"ID компании: {vac[1]}")
                print(f"Название вакансии: {vac[2]}")
                print(f"Зарплата от: {vac[3]} до {vac[4]}")
                print(f"Url: {vac[5]}")
                print()

    def create_tables(self, cur, script_file):
        """Создает таблицу"""

        with open(script_file, "r") as f:
            cur.execute(f.read())

    def drop_tables(self, cur):
        """Удаляет таблицу"""

        cur.execute("DROP TABLE vacancies;"
                    "DROP TABLE employers")

    def create_db(self, params, db_name):
        """Создает Базу Данных"""

        conn = psycopg2.connect(dbname='postgres', **params)
        conn.autocommit = True
        cur = conn.cursor()

        cur.execute(f"DROP DATABASE {db_name}")
        cur.execute(f"CREATE DATABASE {db_name}")

        conn.close()
