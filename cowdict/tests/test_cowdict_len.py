
import pytest
from cowdict import CowDict

base_dict = {
    "foo1": "bar1",
    "foo2": "bar2",
    "foo3": "bar3",
    "foo4": "bar4",
    "foo5": "bar5",
}
keys = ("foo1", "foo2", "foo3", "foo4", "foo5")


def test_same_unchanged():
    cd = CowDict(base_dict)

    assert len(cd) == len(base_dict)


def test_same_changed():
    cd = CowDict(base_dict)

    cd["foo2"] = "baz2"
    cd["foo5"] = "baz5"

    assert len(cd) == len(base_dict)


def test_new_keys_added():
    cd = CowDict(base_dict)

    cd["foo6"] = "bar6"
    cd["foo7"] = "bar7"

    assert len(cd) == len(base_dict) + 2


def test_keys_deleted():
    cd = CowDict(base_dict)

    del cd["foo1"]
    del cd["foo5"]

    assert len(cd) == len(base_dict) - 2


def test_multiple_operations():
    cd = CowDict(base_dict)
    del cd["foo1"]
    del cd["foo3"]

    cd["foo4"] = "changed_value"
    cd["new_key1"] = "new_value1"
    cd["new_key2"] = "new_value2"

    assert len(cd) == len(base_dict)
