CREATE TABLE employers
(
employer_id int PRIMARY KEY
company_name varchar(50)
vacancies_url text
open_vacancies int
);

CREATE TABLE vacancies
(
vacancy_id int PRIMARY KEY
vacancy_name text
salary_from int
salary_to int
url text
employer_id int
);

