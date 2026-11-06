"""Domain model for customer records."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Customer:
    id: str
    name: str
    email: str

    def __post_init__(self) -> None:
        if not isinstance(self.id, str) or self.id == "":
            raise ValueError("Customer id must be non-empty text.")
