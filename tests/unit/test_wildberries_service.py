from app.clients.wildberries import WildberriesClient


class FakeResponse:
    def json(self) -> dict:
        return {
            "products": [
                {
                    "id": 122268164,
                    "name": "Test product",
                    "sizes": [
                        {
                            "price": {
                                "basic": 251000,
                                "product": 82500,
                            }
                        }
                    ],
                }
            ]
        }


def test_get_product_info_formats_prices(monkeypatch) -> None:
    def fake_get(url, params, headers, timeout):
        assert url == WildberriesClient.BASE_URL
        assert params["nm"] == 122268164
        assert headers["Accept"] == "application/json"
        assert timeout == 15
        return FakeResponse()

    monkeypatch.setattr("app.clients.wildberries.requests.get", fake_get)

    client = WildberriesClient()

    result = client.get_product_info(122268164)

    assert result == {
        "nm_id": 122268164,
        "name": "Test product",
        "basic_kop": 251000,
        "product_kop": 82500,
        "basic_rub": 2510.0,
        "product_rub": 825.0,
    }
