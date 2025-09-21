from enum import Enum


class PatchedOrderRequestStatus(str, Enum):
    CANCELLED = "cancelled"
    DELIVERED = "delivered"
    PENDING = "pending"
    PROCESSING = "processing"
    SHIPPED = "shipped"

    def __str__(self) -> str:
        return str(self.value)
