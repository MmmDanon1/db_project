Проект по БД
В рамках проекта вам необходимо получить данные о компаниях и вакансиях с сайта hh.ru, спроектировать таблицы в БД PostgreSQL и загрузить полученные данные в созданные таблицы.

Основные шаги проекта
Получить данные о работодателях и их вакансиях с сайта hh.ru. Для этого используйте публичный API hh.ru и библиотеку 
requests
.
Выбрать не менее 10 интересных вам компаний, от которых вы будете получать данные о вакансиях по API.
Спроектировать таблицы в БД PostgreSQL для хранения полученных данных о работодателях и их вакансиях. Для работы с БД используйте библиотеку 
psycopg2
.
Реализовать код, который заполняет созданные в БД PostgreSQL таблицы данными о работодателях и их вакансиях.
Создать класс 
DBManager
для работы с данными в БД.
Для запуска программы необходимо создать файл congig.py, заполнить файл (пример в файле config.manager.py)
Список зависимостей в файле requriements.txt
->

Виртуальная среда: Для Windows python -m venv venv

Для Linux, macOS python3 -m venv venv

Активация виртуальной среды: .\venv\Scripts\активировать

Менеджер пакетов поэзии.

Windows установить pip poetry

macOS создаем установочную поэзию

Linux, macOS curl -sSL https://install.python-poetry.org | python3 - путь экспорта="$HOME/.local/bin:$PATH"

Установка с помощью поэзии дополнение к поэзии –G dev pytest

Установка через pip pip установить pytest

