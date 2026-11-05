import pytest

from customer_search import Customer, search_customers


CUSTOMERS = [
    Customer("1", "Ana López", "ana@example.com"),
    Customer("2", "Bruno Ana", "bruno@example.com"),
    Customer("3", "Carla", "carla@anadominio.com"),
]


def test_model_has_required_fields():
    assert (CUSTOMERS[0].id, CUSTOMERS[0].name, CUSTOMERS[0].email) == (
        "1", "Ana López", "ana@example.com"
    )


def test_partial_search_preserves_order():
    assert search_customers("an", CUSTOMERS) == CUSTOMERS


def test_partial_name_search():
    assert search_customers("Lóp", CUSTOMERS) == [CUSTOMERS[0]]


def test_partial_email_search():
    assert search_customers("dominio", CUSTOMERS) == [CUSTOMERS[2]]


def test_case_insensitive_and_trimmed():
    assert search_customers("  LÓPEZ  ", CUSTOMERS) == [CUSTOMERS[0]]


def test_customer_matching_both_fields_is_not_duplicated():
    assert search_customers("ana", CUSTOMERS).count(CUSTOMERS[0]) == 1


def test_no_matches_returns_empty_list():
    assert search_customers("inexistente", CUSTOMERS) == []


@pytest.mark.parametrize("term", ["", "   ", "\t\n"])
def test_empty_term_is_rejected(term):
    with pytest.raises(ValueError, match="no vacío"):
        search_customers(term, CUSTOMERS)


def test_non_text_term_is_rejected():
    with pytest.raises(ValueError, match="debe ser texto"):
        search_customers(None, CUSTOMERS)


@pytest.mark.parametrize("field", ["name", "email"])
@pytest.mark.parametrize("term", ["STRASSE", "  strasse  "])
def test_unicode_casefold_matches_name_and_email(field, term):
    # Unlike lower(), casefold() equates the German sharp s with ss.
    customer = Customer(
        "unicode",
        "Straße" if field == "name" else "Cliente",
        "straße@example.com" if field == "email" else "otro@example.com",
    )
    unrelated = Customer("other", "Bruno", "bruno@example.com")
    assert search_customers(term, [unrelated, customer]) == [customer]


@pytest.mark.parametrize(
    ("term", "expected_ids"),
    [("  ANA LÓPEZ  ", ["single"]), ("  ANA  LÓPEZ  ", ["double"])],
)
def test_search_preserves_internal_spaces(term, expected_ids):
    customers = [
        Customer("single", "Ana López", "uno@example.com"),
        Customer("double", "Ana  López", "dos@example.com"),
    ]
    assert [customer.id for customer in search_customers(term, customers)] == expected_ids


def test_search_accepts_generator_and_preserves_order():
    customers = (customer for customer in CUSTOMERS)
    assert search_customers("ANA", customers) == CUSTOMERS
