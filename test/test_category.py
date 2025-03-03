import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.core.settings import app_setting
from app.schemas.legend_schema import CategoryDTO


@pytest.fixture
def client():
    return TestClient(app)


def test_get_categories(client):
    response = client.get(f"{app_setting.api_version}/categories")
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    for item in data:
        model_instance = CategoryDTO(**item)
        assert isinstance(model_instance, CategoryDTO)
