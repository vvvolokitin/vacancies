import pytest

from app.vacancies.dao.vacancies_dao import VacanciesDAO


@pytest.fixture()
def vacancies_dao():
    """Фикстура создания экземпляра класса VacanciesDAO"""
    vacancies_dao_instance = VacanciesDAO('./data/vacancies.json')
    return vacancies_dao_instance


keys_should_be: set = {'pk', 'company', 'position', 'salary'}


class TestVacanciesDAO:
    """
    Класс тестирования VacanciesDAO.

    Методы:
        test_get_all: Проверяет, верный ли список возвращается.
        test_get_by_id: Проверяет, верная ли вакансия возвращается.
    """

    def test_get_all(self, vacancies_dao):
        """Проверяет, верный ли список возвращается."""
        vacancies: list = vacancies_dao.get_all()
        assert type(vacancies) == list, 'Возвращается не список.'
        assert len(vacancies) > 0, 'Возвращается пустой список.'
        assert set(vacancies[0].keys()
                   ) == keys_should_be, 'Неверный список ключей.'

    def test_get_by_id(self, vacancies_dao):
        """Проверяет, верная ли вакансия возвращается."""
        vacancy: dict = vacancies_dao.get_by_pk(1)
        assert (vacancy['pk'] == 1), 'Возвращается неправильный кандидат.'
        assert set(vacancy.keys()
                   ) == keys_should_be, 'Неверный список ключей.'
