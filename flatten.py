"""
Flatten This

For our purposes we're going to assume that our woodchuck JSON data has
already been loaded into Python dictionaries, so our job is just to
flatten those dictionaries as described in the README example. You do
not need to read or write any JSON.

Guidelines for your solution:
 * Stick to the function signature and docstring specification
   provided below for the main flatten function.
 * Make sure that your solution would flatten the example "Cap'n Chuck"
   dictionary as described in the README.
 * At the same time, keep in mind that some of our woodchuck data is
   more complex than the "Cap'n Chuck" example, so make your solution
   general and not tied to the specific structure from the README
   example.
 * Please use Python 3 and do your best to stick to the standard
   library.
"""

from flatten_dict import flatten as flatten_py_function


class NotADictionary(Exception):
    pass


def flatten(obj: dict) -> dict:
    """
    This function takes a dictionary with arbitrary levels of nested
    lists and dictionaries and flattens it.

    Raises NotADictionary if the input is invalid.

    code adapted from https://codereview.stackexchange.com/a/21035
    """
    if not isinstance(obj, dict):
        raise NotADictionary

    def _items(default_separator="."):
        # iterate over dict items
        for key, value in obj.items():

            # check if value is a dict
            if isinstance(value, dict):
                for subkey, subvalue in flatten(value).items():
                    yield f"{key}{default_separator}{subkey}", subvalue

            # check if value is a list
            elif isinstance(value, list):
                for subkey in range(0, len(value)):
                    yield f"{key}{default_separator}{subkey}", value[subkey]

            # just yield values, nothing to do
            else:
                print(f"key: {key}, value: {value}")
                yield key, value

    return dict(_items())


def flatten_py(obj: dict) -> dict:
    """
    This function takes a dictionary with arbitrary levels of nested
    lists and dictionaries and flattens it.

    Raises NotADictionary if the input is invalid.


    wrapper function for flatten-dict pypy module.
    package has also recently been updated and the
    team would have less code to maintain.
    """

    if not isinstance(obj, dict):
        raise NotADictionary

    return flatten_py_function(obj, reducer="dot", enumerate_types=(list,))
