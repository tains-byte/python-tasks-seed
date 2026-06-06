import copy
import random
from itertools import pairwise
import pytest
from comp_swap_container import CompSwapList
import sortings

    
@pytest.fixture(scope="module")
def fatal_array():
    """
    Create a shuffled array of 1000 elements with fixed seed
    """
    r = random.Random()
    r.seed(123456)

    data = list(range(1000))
    r.shuffle(data)
    yield CompSwapList(data)

@pytest.fixture
def empty_data():
    return CompSwapList([])

@pytest.fixture
def single_element():
    return CompSwapList([404])

@pytest.fixture
def already_sorted():
    return CompSwapList([1, 2, 23, 55, 100, 2425, 2949])

@pytest.fixture
def reversed_data():
    return CompSwapList([24692, 22599, 21594, 20000, 10009, 10001, 9999, 2332, 23, 1])

@pytest.fixture
def duplicates():
    r = random.Random()
    r.seed(3425)
    data = list(range(100))+list(range(100))+list(range(1000))
    r.shuffle(data)
    yield CompSwapList(data)

@pytest.fixture
def two_elements():
    return CompSwapList([2, 1])

    
Case = ["fatal_array", "empty_data", "single_element", "reversed_data", "already_sorted", "duplicates", "two_elements"]

def test_selection_sort(fatal_array, empty_data, single_element, reversed_data, 
                        already_sorted, duplicates, two_elements):
    Massive = [
        copy.copy(fatal_array),    
        copy.copy(empty_data),
        copy.copy(single_element),
        copy.copy(reversed_data),
        copy.copy(already_sorted),
        copy.copy(duplicates),
        copy.copy(two_elements),
    ]


    for i in range(len(Massive)):
        sortings.selection_sort(Massive[i])
        assert all(x <= y for x, y in pairwise(Massive[i])), f"Failed on {Case[i]}"


def test_merge_sort(fatal_array, empty_data, single_element, reversed_data, 
                    already_sorted, duplicates, two_elements):
    Massive = [
        copy.copy(fatal_array),
        copy.copy(empty_data),
        copy.copy(single_element),
        copy.copy(reversed_data),
        copy.copy(already_sorted),
        copy.copy(duplicates),
        copy.copy(two_elements),
    ]
    
    for i in range(len(Massive)):
        sortings.merge_sort(Massive[i])
        assert all(x <= y for x, y in pairwise(Massive[i])), f"Failed on {Case[i]}"

    

