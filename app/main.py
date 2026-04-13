import uvicorn
import requests
from fastapi import FastAPI, HTTPException
from http import HTTPStatus

app = FastAPI()

def get_wb_price(product_id: int, dest: int = -1257786, curr: str = "rub", spp: int = 30) -> dict:
    url = "https://card.wb.ru/cards/v4/detail"
    params = {
        "appType": 1,
        "curr": curr,
        "dest": dest,
        "spp": spp,
        "nm": product_id,
    }
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json",
    }
    response = requests.get(url, params=params, headers=headers, timeout=15)
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
    basic = price.get("basic")        # старая цена в копейках
    product_price = price.get("product")  # текущая цена в копейках
    return {
        "nm_id": product.get("id"),
        "name": product.get("name"),
        "basic_kop": basic,
        "product_kop": product_price,
        "basic_rub": basic / 100 if basic is not None else None,
        "product_rub": product_price / 100 if product_price is not None else None,
    }

@app.get("/{product_id}")
def get_item_info(product_id: int):
    if product_id < 1:
        raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail="Invalid user id")
    result = get_wb_price(product_id)
    return result

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)