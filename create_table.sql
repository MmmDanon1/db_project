--
-- Name: employers; Type: TABLE; Schema: public; Owner: -; Tablespace:
--
CREATE TABLE employers
(
employer_id int,
company_name text,
employer_url text,
open_vacancies int
);

--
-- Name: vacancies; Type: TABLE; Schema: public; Owner: -; Tablespace:
--

CREATE TABLE vacancies
(
vacancy_id int,
employer_id int,
vacancy_name text,
vacancy_salary_from int DEFAULT 0,
vacancy_salary_to int DEFAULT 0,
url text
)

