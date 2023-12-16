class TestVacancies:
    """
    Класс тестирования vacancies blueprint.

    Методы:
        test_all_vacancies_status: Проверяет при запросе вакансий статус-код.
        test_single_vacancy_status: Проверяет при запросе одной вакансии
        статус-код.
    """

    def test_all_vacancies_status(self, test_client):
        """Проверяет при запросе вакансий статус-код."""
        response = test_client.get('/vacancies/', follow_redirects=True)
        assert response.status_code == 200, 'Статус-код неверный'

    def test_single_vacancy_status(self, test_client):
        """Проверяет при запросе одной вакансии статус-код."""
        response = test_client.get('/vacancies/1', follow_redirects=True)
        assert response.status_code == 200, 'Статус-код неверный'
