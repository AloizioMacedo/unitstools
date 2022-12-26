Technical Details
=================

To have a summarised version of the behavior of this package, we could simply state:

.. highlights::

    *We do nothing at runtime. We just fool the type checkers.*

For more details, read ahead.

Instantiation
-------------

.. currentmodule:: unitstools

The classes :class:`Unit` and :class:`IntUnit` (and their derived classes defined
by the user) are never actually instantiated. Their instantiation produce :code:`ints`
and :code:`floats`, as can be seen in the definitions of their :func:`__new__`
dunder method.

This should be kept in mind in order to understand that, in runtime, things
like :code:`IntUnit(2)` are just :code:`ints`. This means that the following
code would raise an error.

.. code-block:: python

    class Seconds(IntUnit):
        ...

    x = Seconds(2)
    assert isinstance(x, Seconds)


.. note::

    The same observations apply, *mutatis mutandis*, to :func:`embed_unit` and
    its return.

Inherting from int (or float)
-----------------------------

.. currentmodule:: unitstools

A reasonable suggestion would be to have :class:`Unit` (resp. :class:`IntUnit`)
inherit from :code:`float` (resp. :class:`int`). For instance, this would make
the builtin :func:`sum` function not raise a warning.

However, this pushes back situations where problems may live. For example,
summing a :class:`IntUnit` with an :code:`int` would not raise a warning. Instead,
the sum will become an :class:`int`, and this would probably result in a warning
only further down the code (for example, if the return type was an :class:`IntUnit`).

Not only is this inconvenient, but we also want to deliberately consider the sum
of something that has a unit with something that does not have to be an "error".

However, if the user thinks that this behavior is desirable, it suffices to
make their units inherit from :code:`float`/:code:`int` like so:

.. code-block:: python

    from unitstools import IntUnit

    class Seconds(IntUnit, int):
        ...

.. note::
    It is important for :class:`IntUnit` be the first class of the inheritance
    due to how Python's resolution order works.

Final Comments
--------------

So, to reiterate: this package does nothing at runtime (with the exception of
the conversion functionalities, which are just multiplications at runtime).
This is by design, choice and scope of the project. For example, if an user
wants to define centimeters and meters, adding them will raise an error
with Pylance (which, again, is by design). If they want to make the code
raise no typing errors, they should convert one of them to the other by means
of a conversion function or something similar.

.. note::

    There are tools which provide ways to work with units at runtime, e.g.
    `Pint <https://pint.readthedocs.io>`_. This is not the scope of unitstools.