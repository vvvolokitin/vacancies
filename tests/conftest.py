import pytest
import run


@pytest.fixture()
def test_client():
    """Фикстура для тестирования всех вьюшек."""
    app = run.app
    return app.test_client()
