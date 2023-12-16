import pytest
from run import app


@pytest.fixture()
def test_client():
    """Фикстура для тестирования всех вьюшек."""
    return app.test_client()
