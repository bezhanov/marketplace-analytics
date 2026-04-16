import requests
from http import HTTPStatus

TEST_PRODUCT_ID = 122268164


def test_get_correct_product_info(app_url):
    response = requests.get(f"{app_url}/api/wb/{TEST_PRODUCT_ID}")
    assert response.status_code == HTTPStatus.OK

    body = response.json()
    assert body["nm_id"] == TEST_PRODUCT_ID, "Product have correct ID"
    assert isinstance(body["name"], str), "Product have name"
    assert isinstance(
        body["basic_kop"], int
    ), "Product have correct basic price (kop)"
    assert isinstance(
        body["product_kop"], int
    ), "Product have correct product price (kop)"
    assert isinstance(
        body["basic_rub"], float
    ), "Product have correct basic price (rub)"
    assert isinstance(
        body["product_rub"], float
    ), "Product have correct product price (rub)"
