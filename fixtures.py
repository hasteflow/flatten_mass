import pytest


@pytest.fixture
def flatten_input_dict():
    return {
        "name": "Cap'n Chuck",
        "aliases": ["Chuck Force 1", "Whistlepig"],
        "physical": {"height_in": 26, "weight_lb": 18},
        "wood_chucked_lbs": 2281,
    }


@pytest.fixture
def flatten_expected_dict():
    return {
        "name": "Cap'n Chuck",
        "aliases.0": "Chuck Force 1",
        "aliases.1": "Whistlepig",
        "physical.height_in": 26,
        "physical.weight_lb": 18,
        "wood_chucked_lbs": 2281,
    }
