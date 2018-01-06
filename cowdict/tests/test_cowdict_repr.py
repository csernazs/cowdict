
from cowdict import CowDict


def test_repr_and_str():
    base = {"key1": "value1", "key2": "value2"}
    cd = CowDict(base)
    cd["new_key"] = "new_value"

    del cd["key2"]

    expected = (
        "{'new_key': 'new_value', 'key1': 'value1'}",
        "{'key1': 'value1', 'new_key': 'new_value'}",
    )

    assert repr(cd) in expected
    assert str(cd) in expected
