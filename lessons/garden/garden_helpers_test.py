"""Testing garden helpers."""

__author__ = "730569217"

from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date


def test_kind_use() -> None:
    """Testing adding to garden by kind of plant."""
    g: dict[str, list[str]] = {'flower': ['daisy'], 'veggie': ['carrot']}
    t: str = "flower"
    p: str = "rose"
    add_by_kind(g, t, p)
    assert g == {'flower': ['daisy', 'rose'], 'veggie': ['carrot']}


def test_kind_edge() -> None:
    """Testing adding to an empty garden."""
    g: dict[str, list[str]] = {}
    add_by_kind(g, "veggie", "broccoli")
    assert g == {"veggie": ["broccoli"]}


def test_date_use() -> None:
    """Testing adding to the garden by date."""
    m: dict[str, list[str]] = {'april': ['daisy', 'petunia']}
    p: str = 'april'
    d: str = 'rose'
    add_by_date(m, p, d) 
    assert m == {'april': ['daisy', 'petunia', 'rose']}


def test_date_edge() -> None:
    """Testing adding to an empty garden."""
    m: dict[str, list[str]] = {'april': []}
    p: str = 'april'
    d: str = ''
    add_by_date(m, p, d)
    assert m == {'april': ['']}


def test_lookup_use() -> None:
    """Testing looking up plants in a month."""
    g: dict[str, list[str]] = {'veggies': ['peas'], 'flower': ['rose']}
    d: dict[str, list[str]] = {'march': ['peas'], 'april': ['rose']}
    fg = lookup_by_kind_and_date(g, d, 'veggies', 'march')
    o = "veggies to plant in march: ['peas']"
    assert fg == o


def test_lookup_edge() -> None:
    """Testing to see if list does not return anything."""
    g: dict[str, list[str]] = {}
    d: dict[str, list[str]] = {}
    assert lookup_by_kind_and_date(g, d, "veggie", "april") == "No veggies to plant in april"
