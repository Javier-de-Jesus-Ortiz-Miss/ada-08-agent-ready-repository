"""I check the identifier invariant and compatibility for CR-ADA08-01."""

from dataclasses import FrozenInstanceError

import pytest

from customer_search import Customer


@pytest.mark.parametrize("identifier", ["", None, 0, False, [], b"C1"])
def test_customer_rejects_invalid_id(identifier):
    with pytest.raises(ValueError):
        Customer(identifier, "Ana", "ana@example.com")


@pytest.mark.parametrize("identifier", ["C900", "  C900  ", " "])
def test_customer_preserves_nonempty_text_id(identifier):
    record = Customer(identifier, "Ana", "ana@example.com")
    assert (record.id, record.name, record.email) == (identifier, "Ana", "ana@example.com")


def test_customer_remains_frozen():
    record = Customer("C900", "Ana", "ana@example.com")
    with pytest.raises(FrozenInstanceError):
        record.id = "changed"
