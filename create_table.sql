CREATE TABLE employers
(
employer_id int PRIMARY KEY
name varchar(50)
city varchar(50)
address varchar(100)
description text
);

CREATE TABLE vacancies
(
vacancy_id int PRIMARY KEY
salary_from int
salary_to int
url text
employer_id int
);

