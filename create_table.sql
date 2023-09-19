CREATE TABLE employers
(
employer_id int PRIMARY KEY
name varchar(50)
vacancies_url text
);

CREATE TABLE vacancies
(
vacancy_id int PRIMARY KEY
salary_from int
salary_to int
url text
employer_id int
);

