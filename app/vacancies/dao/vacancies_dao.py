import json

from typing import Any


class VacanciesDAO:
    """
    Класс вакансий.

    Атрибуты:
        path (str): Путь к файлу.
    Методы:
        load_data: Загружает данные из файла о всех вакансиях.
        get_all: Возвращает список со всеми данными.
        get_by_pk: Возвращает вакансию по номеру.

    """

    def __init__(self, path: str) -> None:
        """
        Устанавливает атрибуты для объекта класса VacanciesDAO.

        Параметры:
            path: (str): Адрес json файла содержащего информацию о
            вакансиях.

        Возвращаемое значение:
            None.
        """
        self.path = path

    def load_data(self) -> list[dict[str, Any]]:
        """
        Загружает данные из файла.

        Возвращаемое значение:
            list[dict]: Список с данными о вакансиях.
        """
        with open(self.path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def get_all(self):
        """
        Возвращает список со всеми данными.

        Возвращаемое значение:
            list[dict]: Список с данными о вакансиях.
        """
        return self.load_data()

    def get_by_pk(self, pk: int) -> dict[str, Any]:
        """
        Возвращает вакансию по номеру.

        Возвращаемое значение:
            vacancy (dict[str, Any]): Данные о кандидате.
        """
        vacancies: list[dict[str, Any]] = self.load_data()
        for vacancy in vacancies:
            if vacancy['pk'] == pk:
                return vacancy
