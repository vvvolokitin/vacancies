import pytest

from app.candidates.dao.candidates_dao import CandidateDAO


@pytest.fixture()
def candidates_dao():
    """Фикстура создания экземпляра класса CandidateDAO"""
    candidates_dao_instance = CandidateDAO('./data/candidates.json')
    return candidates_dao_instance


keys_should_be: set = {'pk', 'name', 'position'}


class TestCandidateDAO:
    """
    Класс тестирования CandidateDAO.

    Методы:
        test_get_all: Проверяет, верный ли список возвращается.
        test_get_by_id: Проверяет, верный ли кандидат возвращается.
    """

    def test_get_all(self, candidates_dao):
        """Проверяет, верный ли список возвращается."""
        candidates: list = candidates_dao.get_all()
        assert type(candidates) == list, 'Возвращается не список.'
        assert len(candidates) > 0, 'Возвращается пустой список.'
        assert set(candidates[0].keys()
                   ) == keys_should_be, 'Неверный список ключей.'

    def test_get_by_id(self, candidates_dao):
        """Проверяет, верный ли кандидат возвращается."""
        candidate: dict = candidates_dao.get_by_pk(1)
        assert (candidate['pk'] == 1), 'Возвращается неправильный кандидат.'
        assert set(candidate.keys()
                   ) == keys_should_be, 'Неверный список ключей.'
