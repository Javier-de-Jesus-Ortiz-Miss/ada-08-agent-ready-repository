"""Search and validate customer queries."""

from collections.abc import Iterable

from .models import Customer


def search_customers(term: str, customers: Iterable[Customer]) -> list[Customer]:
    """Return matching customers in input order."""
    if not isinstance(term, str):
        raise ValueError("El término de búsqueda debe ser texto.")

    query = term.strip().casefold()
    if not query:
        raise ValueError("Escribe un término de búsqueda no vacío.")

    return [
        customer
        for customer in customers
        if query in customer.name.casefold() or query in customer.email.casefold()
    ]
