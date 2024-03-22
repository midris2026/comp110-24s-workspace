"""Dictionary Testing."""

__author__ = "730569217"

import pytest
from exercises.ex05.dictionary import invert, count, favorite_color, alphabetizer, update_attendance

# invert


def test_invert_first_use() -> None:
    """Test basic use case for invert function."""
    t: dict[str, str] = {'apples': '1', 'bananas': '2', 'pears': '3'}
    d: dict[str, str] = {'1': 'apples', '2': 'bananas', '3': 'pears'}
    assert invert(t) == d


def test_invert_second_use() -> None:
    """Test basic use case for invert function."""
    t: dict[str, str] = {'jack': 'jill', 'dog': 'cat', 'panera': 'bread'}
    assert invert(t) == {'jill': 'jack', 'cat': 'dog', 'bread': 'panera'}


def test_invert_edge() -> None:
    """Test function if same keys are present."""
    with pytest.raises(KeyError):
        t: dict[str, str] = {'turtle': 'sea', 'dolphin': 'sea'}
        invert(t)

# count
        

def test_count_first_use() -> None:
    """Test basic use case for count function."""
    l: list[str] = ['birks', 'hokas']
    assert count(l) == {'birks': 1, 'hokas': 1}


def test_count_second_use() -> None:
    """Test basic use case for count function."""
    l: list[str] = ['birks', 'hokas', 'birks', 'dunks', 'converse', 'blazers', 'blazers']
    assert count(l) == {'birks': 2, 'hokas': 1, 'dunks': 1, 'converse': 1, 'blazers': 2}


def test_count_edge() -> None:
    """Test function if input is empty."""
    l: list[str] = []
    assert count(l) == {}

# favorite color
    

def test_fc_first_use() -> None:
    """Test basic use case for favorite color function."""
    t: dict[str, str] = {'muk': 'green', 'law': 'blue', 'feran': 'green'}
    assert favorite_color(t) == 'green'


def test_fc_second_use() -> None:
    """Test basic use case for favorite color function."""
    t: dict[str, str] = {'muk': 'green', 'law': 'blue', 'feran': 'green', 'ansel': 'blue', 'laney': 'pink', 'kat': 'blue'}
    assert favorite_color(t) == 'blue'


def test_fc_edge() -> None:
    """Test if input is empty."""
    t: dict[str, str] = {}
    assert favorite_color(t) == ""

# alphabetizer
    

def test_alphabetizer_first_use() -> None:
    """Test basic use case for alphabetizer function."""
    t: dict[str, str] = {'caleb', 'blake', 'brendan', 'lucas'}
    assert alphabetizer(t) == {'b': ['blake', 'brendan'], 'c': ['caleb'], 'l': ['lucas']}


def test_alphabetizer_second_use() -> None:
    """Test basic use case for alphabetizer fucntion."""
    t: dict[str, str] = {'bee', 'gio', 'jodee', 'grace'}
    assert alphabetizer(t) == {'b': ['bee'], 'g': ['gio', 'grace'], 'j': ['jodee']}


def test_alphabetizer_edge() -> None:
    """Test if input is empty."""
    t: list[str] = []
    assert alphabetizer(t) == {}

# count attendance
    

def test_ca_first_use() -> None: 
    """Test basic use case for count attendance functiion."""
    a: dict[str, list[str]] = {'Monday': ['ang', 'jules'], 'Tuesday': ['pat', 'cam']}
    update_attendance(a, 'Tuesday', 'morgan') 
    assert a == {'Monday': ['ang', 'jules'], 'Tuesday': ['pat', 'cam', 'morgan']}


def test_ca_second_use() -> None: 
    """Test basic use case for count attendance functiion."""
    a: dict[str, list[str]] = {'Monday': ['ang', 'jules'], 'Tuesday': ['pat', 'cam']}
    update_attendance(a, 'Monday', 'tyler')
    assert a == {'Monday': ['ang', 'jules', 'tyler'], 'Tuesday': ['pat', 'cam']}


def test_ca_edge() -> None: 
    """Test if attendance log is empty."""
    a: dict[str, list[str]] = {}
    update_attendance(a, 'Tuesday', 'lauryn')
    assert a == {'Tuesday': ['lauryn']}