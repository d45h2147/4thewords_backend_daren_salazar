import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.core.settings import app_setting
from app.schemas.legend_schema import CantonDTO, DistrictDTO, ProvinceDTO


@pytest.fixture
def client():
    return TestClient(app)


def test_get_cantons(client):
    response = client.get(f"{app_setting.api_version}/location/cantons")
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    for item in data:
        model_instance = CantonDTO(**item)
        assert isinstance(model_instance, CantonDTO)


def test_get_provinces(client):
    response = client.get(f"{app_setting.api_version}/location/provinces")
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    for item in data:
        model_instance = ProvinceDTO(**item)
        assert isinstance(model_instance, ProvinceDTO)


def test_get_districts(client):
    response = client.get(f"{app_setting.api_version}/location/districts")
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    for item in data:
        model_instance = DistrictDTO(**item)
        assert isinstance(model_instance, DistrictDTO)
