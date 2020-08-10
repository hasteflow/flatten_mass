import pytest
from copy import deepcopy

# :NOTE use one import or the other below depending on which flatten function you want to test
# from flatten import flatten_py as flatten, NotADictionary
from flatten import flatten, NotADictionary

from fixtures import flatten_input_dict, flatten_expected_dict


def test_flatten_returns_a_dict_if_input_is_dict():
    """
    flatten function should return a dictionary.
    Input will be a dictionary
    """
    item = flatten({})
    assert isinstance(item, dict), f"return value must be a dict. {type(item)} given."


def test_flatten_returns_original_dict_for_one_dimension_dict():
    input_dict = {"a": 1, "b": 2, "c": 3}

    item = flatten(input_dict)
    assert item == input_dict


def test_flatten_raises_NotADictionary_exception_if_input_is_not_a_dict():
    with pytest.raises(NotADictionary):
        flatten([])
        flatten(1.23)
        flatten(None)


def test_flatten_does_not_mutate_input_dict(flatten_input_dict):
    expected_dict = deepcopy(flatten_input_dict)

    try:
        # we do not care about returned value in this particular case
        _ = flatten(flatten_input_dict)
    except Exception as e:
        pytest.fail(f"flatten input dict may have been mutated:{e}")

    assert expected_dict == flatten_input_dict


def test_flatten_returns_correct_flattened_dict(
    flatten_input_dict, flatten_expected_dict
):
    """
    Given this input_dict, running flatten function
    must return expected_dict
    """

    returned_dict = flatten(flatten_input_dict)
    assert returned_dict == flatten_expected_dict
