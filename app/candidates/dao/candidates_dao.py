from typing import Any
import json


class CandidateDAO:
    """
    Класс кандидатов.

    Атрибуты:
        path (str): Путь к файлу.
    Методы:
        load_data: Загружает данные из файла о всех кандидатах.
        get_all: Возвращает список со всеми данными.
        get_by_pk: Возвращает кандидата по его номеру.

    """

    def __init__(self, path: str) -> None:
        """
        Устанавливает атрибуты для объекта класса CandidateDAO.

        Параметры:
            path: (str): Адрес json файла содержащего информацию о
            кандидатах.

        Возвращаемое значение:
            None.
        """
        self.path = path

    def load_data(self) -> list[dict[str, Any]]:
        """
        Загружает данные из файла.

        Возвращаемое значение:
            list[dict]: Список с данными о кандидатах.
        """
        with open(self.path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def get_all(self):
        """
        Возвращает список со всеми данными.

        Возвращаемое значение:
            list[dict]: Список с данными о кандидатах.
        """
        return self.load_data()

    def get_by_pk(self, pk: int) -> dict[str, Any]:
        """
        Возвращает кандидата по его номеру.

        Возвращаемое значение:
            candidate (dict[str, Any]): Данные о кандидате.
        """
        candidates: list[dict[str, Any]] = self.load_data()
        for candidate in candidates:
            if candidate['pk'] == pk:
                return candidate
