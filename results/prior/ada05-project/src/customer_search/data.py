"""Fictitious, read-only demonstration data."""

from .models import Customer


CUSTOMERS: tuple[Customer, ...] = (
    Customer("C001", "Ana López", "ana.lopez@example.com"),
    Customer("C002", "Bruno García", "bruno.garcia@example.com"),
    Customer("C003", "Carla Méndez", "carla.mendez@example.com"),
    Customer("C004", "Daniel Ruiz", "daniel.ruiz@example.com"),
)
