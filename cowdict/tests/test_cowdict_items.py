
import pytest
from cowdict import CowDict

base_dict = {
    "foo1": "bar1",
    "foo2": "bar2",
    "foo3": "bar3",
    "foo4": "bar4",
    "foo5": "bar5",
}

base_dict_items = tuple(base_dict.items())
keys = ("foo1", "foo2", "foo3", "foo4", "foo5")


def test_same_unchanged():
    cd = CowDict(base_dict)

    for key in keys:
        assert cd[key] == base_dict[key]

    assert set(base_dict_items) == set(cd.items())
    assert base_dict_items == tuple(base_dict.items())


def test_same_changed():
    cd = CowDict(base_dict)

    cd["foo2"] = "baz2"
    cd["foo5"] = "baz5"

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

    assert base_dict_items == tuple(base_dict.items())


def test_new_keys_added():
    cd = CowDict(base_dict)

    cd["foo6"] = "bar6"
    cd["foo7"] = "bar7"

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

    assert base_dict_items == tuple(base_dict.items())


def test_base_keys_deleted():
    cd = CowDict(base_dict)

    del cd["foo1"]
    del cd["foo5"]

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

    assert base_dict_items == tuple(base_dict.items())


def test_new_keys_deleted():
    cd = CowDict(base_dict)

    cd["foo6"] = "bar6"
    cd["foo7"] = "bar7"
    del cd["foo6"]
    del cd["foo7"]

    for key in keys:
        assert cd[key] == base_dict[key]

    assert set(base_dict_items) == set(cd.items())

    assert base_dict_items == tuple(base_dict.items())


def test_missing_keys_deleted():
    cd = CowDict(base_dict)

    with pytest.raises(KeyError):
        del cd["foo6"]

    assert base_dict_items == tuple(base_dict.items())
