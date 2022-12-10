""""""

import numpy as np
import pandas as pd

VALUE_LIST = {
    "int": 465,
    "float": 846.346,
    "str": "Hello World!",
    "bool_true": True,
    "bool_false": False,
    "bytes": bytes("Hello World!", "utf-8"),
    "list": [1, 2, 3, 45, "asd", 3244],
    "nested_list": [[1, 2, 3], [4, 5, 6], [[7, 8], [9, 10]]],
    "nested_list_dict": [
        [1, 2, 3],
        [4, 5, 6],
        [[7, 8], [9, 10], {"a": 1, "b": 2, "c": 3}],
        {"e": {"f": 3, "g": 4, "h": 5}},
    ],
    "dict": {"a": 1, "b": 2, "c": 3},
    "nested_dict": {"a": {"b": 1, "c": 2}, "d": {"e": {"f": 3, "g": 4, "h": 5}}},
    "nested_dict_list": {
        "a": {"b": 1, "c": 2},
        "d": {"e": {"f": 3, "g": 4, "h": 5, "i": [[7, 8], [9, 10]]}, "j": [9, 10]},
    },
    "ndarray": np.array([1, 2, 3, 4]),
    "ndarray_large": np.random.rand(10, 10, 10),
    "dataframe": pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]}),
}


def compare_values(value1, value2):
    if type(value1) == np.ndarray:
        assert np.array_equal(value1, value2)
    elif type(value1) == pd.DataFrame:
        assert value1.equals(value2)
    elif type(value1) == float:
        assert abs(value1 - value2) < 0.01
    else:
        assert value1 == value2
