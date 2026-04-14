from fastapi import APIRouter, HTTPException
from http import HTTPStatus

from app.clients.wildberries import WildberriesClient

router = APIRouter(prefix="/api/wb")

wb_client = WildberriesClient()


# TODO create routers schemas
@router.get("/{product_id}")
def get_item_info(product_id: int):
    if product_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
            detail="Invalid product id",
        )

    result = wb_client.get_product_info(product_id)
    if not result:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=f"Product {product_id} not found",
        )

    return result
