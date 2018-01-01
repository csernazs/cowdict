cowdict
~~~~~~~

cowdict is a python module implementing copy-on-write pattern on dictionaries.

This means that if someone change the dict-like object, the original object won't be changed but
the differences will be tracked instead.

Nutshell
--------

Here's a small example:

.. code-block:: python

    base_dict = {"foo": "bar"}
    cd = CowDict(base_dict)
    cd["foo"] = "baz"

    print(base_dict["foo"]) # will still print 'bar'
    print(cd["foo"]) # will print 'baz'

CowDict object (`cd` in the code above) implements the `MutableMapping` interface, simply speaking it has the
same interface as the `dict` object.

This means that it is guaranteed that changing keys/values on this object will never cause the change of the
underlying dictionary (`base_dict` in the example).

Philosophy
----------
The idea behind this module is to avoid copying dictionary where it is possible and use this wrapper class instead.
While it has some penalties on the performance on key lookup and length calculation, the memory footprint can
be kept at minimum (compared to a full copy of the dictionary).


Behind the scenes
-----------------
Behind the scenes, new items are added to a separate directory. Keys which exist on the base dictionary are
'deleted' by keeping a separate set object about the the keys deleted.
Every time when a key is accessed either by `getitem` or `items` or other methods,
these additional structures are involved to produce the correct result.

While having an assumption of having the base dictionary read-only would make the world easier, especially
when calculating the length of the object, the library handles the situation when the base dictionary changes.
