class TestCandidates:
    """
    Класс тестирования candidates blueprint.

    Методы:
        test_all_candidates_status: Проверяет при запросе кандидата статус-код.
        test_single_candidate_status: Проверяет при запросе одного кандидата
        статус-код.
    """

    def test_all_candidates_status(self, test_client):
        """Проверяет при запросе кандидата статус-код."""
        response = test_client.get('/candidates/', follow_redirects=True)
        assert response.status_code == 200, 'Статус-код неверный'

    def test_single_candidate_status(self, test_client):
        """Проверяет при запросе одного кандидата статус-код."""
        response = test_client.get('/candidates/1', follow_redirects=True)
        assert response.status_code == 200, 'Статус-код неверный'
