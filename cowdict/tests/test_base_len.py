
import pytest
from cowdict import CowDict


@pytest.fixture
def base_dict():
    return {
        "foo1": "bar1",
        "foo2": "bar2",
        "foo3": "bar3",
        "foo4": "bar4",
        "foo5": "bar5",
    }


def test_same_changed(base_dict):
    cd = CowDict(base_dict)

    base_dict["foo2"] = "baz2"
    base_dict["foo5"] = "baz5"

    assert len(cd) == len(base_dict)


def test_new_keys_added(base_dict):
    cd = CowDict(base_dict)

    base_dict["foo6"] = "bar6"
    base_dict["foo7"] = "bar7"

    assert len(cd) == len(base_dict)


def test_keys_deleted(base_dict):
    cd = CowDict(base_dict)

    del base_dict["foo1"]
    del base_dict["foo5"]

    assert len(cd) == len(base_dict)
