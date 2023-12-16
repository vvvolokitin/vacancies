class TestMain:
    """
    Класс тестирования main blueprint.

    Методы:
        test_root_status: Проверяет статус код страницы.
        test_root_content: Проверяет отображение контента на главной странице.
    """

    def test_root_status(self, test_client):
        """Проверяет статус код страницы."""
        response = test_client.get('/', follow_redirects=True)
        assert response.status_code == 200, 'Статус код неверный'

    def test_root_content(self, test_client):
        """Проверяет отображение контента на главной странице."""
        response = test_client.get('/', follow_redirects=True)
        assert 'Это главная страница' in response.data.decode(
            'utf-8'
        ), 'Ошибка контента на главной страницу'
