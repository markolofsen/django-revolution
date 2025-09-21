from enum import Enum


class OrderRequestStatus(str, Enum):
    CANCELLED = "cancelled"
    DELIVERED = "delivered"
    PENDING = "pending"
    PROCESSING = "processing"
    SHIPPED = "shipped"

    def __str__(self) -> str:
        return str(self.value)
