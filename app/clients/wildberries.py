import requests

from app.clients.base import BaseClient


class WildberriesClient(BaseClient):
    """Client for Wildberries marketplace API."""

    BASE_URL = "https://card.wb.ru/cards/v4/detail"

    def __init__(
        self,
        dest: int = -1257786,
        curr: str = "rub",
        spp: int = 30,
        timeout: int = 15,
    ) -> None:
        self.dest = dest
        self.curr = curr
        self.spp = spp
        self.timeout = timeout

    def get_product_info(self, product_id: int) -> dict:
        params = {
            "appType": 1,
            "curr": self.curr,
            "dest": self.dest,
            "spp": self.spp,
            "nm": product_id,
        }
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json",
        }
        response = requests.get(
            self.BASE_URL, params=params, headers=headers, timeout=self.timeout
        )
        response.raise_for_status()
        data = response.json()

        products = data.get("products", [])
        if not products:
            return {}

        product = products[0]
        sizes = product.get("sizes", [])
        if not sizes:
            return {}

        price = sizes[0].get("price", {})
        basic = price.get("basic")
        product_price = price.get("product")

        return {
            "nm_id": product.get("id"),
            "name": product.get("name"),
            "basic_kop": basic,
            "product_kop": product_price,
            "basic_rub": basic / 100 if basic is not None else None,
            "product_rub": (
                product_price / 100 if product_price is not None else None
            ),
        }
