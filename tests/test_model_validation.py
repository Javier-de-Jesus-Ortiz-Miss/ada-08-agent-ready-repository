"""I verify CR-ADA08-01 against the existing customer identifier invariant."""

from dataclasses import FrozenInstanceError

import pytest

from customer_search import Customer


@pytest.mark.parametrize("identifier", ["", None, 0, False, [], b"C1"])
def test_customer_rejects_invalid_id(identifier):
    with pytest.raises(ValueError):
        Customer(identifier, "Ana", "ana@example.com")


@pytest.mark.parametrize("identifier", ["C900", "  C900  ", " "])
def test_customer_preserves_nonempty_text_id(identifier):
    customer = Customer(identifier, "Ana", "ana@example.com")
    assert customer.id == identifier
    assert customer.name == "Ana"
    assert customer.email == "ana@example.com"


def test_customer_remains_frozen():
    customer = Customer("C900", "Ana", "ana@example.com")
    with pytest.raises(FrozenInstanceError):
        customer.id = "changed"
