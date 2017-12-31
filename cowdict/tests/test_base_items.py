
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


keys = ("foo1", "foo2", "foo3", "foo4", "foo5")


def test_same_changed(base_dict):
    cd = CowDict(base_dict)

    base_dict["foo2"] = "baz2"
    base_dict["foo5"] = "baz5"

    for key in keys:
        if key in ("foo2", "foo5"):
            assert cd[key] == key.replace("foo", "baz")
        else:
            assert cd[key] == base_dict[key]

    assert set(cd.items()) == {
        ('foo1', 'bar1'),
        ('foo2', 'baz2'),
        ('foo3', 'bar3'),
        ('foo4', 'bar4'),
        ('foo5', 'baz5'),
    }


def test_new_keys_added(base_dict):
    cd = CowDict(base_dict)

    base_dict["foo6"] = "bar6"
    base_dict["foo7"] = "bar7"

    for key in keys:
        assert cd[key] == base_dict[key]

    assert cd["foo6"] == "bar6"
    assert cd["foo7"] == "bar7"

    assert set(cd.items()) == {
        ('foo1', 'bar1'),
        ('foo2', 'bar2'),
        ('foo3', 'bar3'),
        ('foo4', 'bar4'),
        ('foo5', 'bar5'),
        ('foo6', 'bar6'),
        ('foo7', 'bar7'),
    }


def test_base_keys_deleted(base_dict):
    cd = CowDict(base_dict)

    del base_dict["foo1"]
    del base_dict["foo5"]

    assert cd["foo2"] == "bar2"
    assert cd["foo3"] == "bar3"
    assert cd["foo4"] == "bar4"

    assert set(cd.items()) == {
        ('foo2', 'bar2'),
        ('foo3', 'bar3'),
        ('foo4', 'bar4'),
    }

    with pytest.raises(KeyError):
        cd["foo1"]

    with pytest.raises(KeyError):
        cd["foo5"]


def test_new_keys_deleted(base_dict):
    cd = CowDict(base_dict)

    base_dict["foo6"] = "bar6"
    base_dict["foo7"] = "bar7"
    del cd["foo6"]
    del cd["foo7"]

    for key in keys:
        assert cd[key] == base_dict[key]
