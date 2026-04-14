from abc import ABC, abstractmethod


class BaseClient(ABC):
    """Abstract base class for marketplace API clients."""

    @abstractmethod
    def get_product_info(self, product_id: int) -> dict:
        """Fetch product info by ID."""
        ...
