"""Domain model for customer records."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Customer:
    id: str
    name: str
    email: str

    def __post_init__(self) -> None:
        """I reject invalid IDs while preserving every non-empty string verbatim."""
        if not isinstance(self.id, str):
            raise ValueError("Customer id must be text.")
        if not self.id:
            raise ValueError("Customer id must not be empty.")
