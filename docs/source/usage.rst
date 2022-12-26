Usage
=====

Installation
------------

To use Unitstools, install it using pip:

.. code-block:: console

   pip install unitstools


Basic Usage
-----------

The fundamental objective of this package is to work in tandem with static type
checkers in order to raise warnings in situations that may be violating
the expected units involved in operations. Consider the example below as an
illustration.

.. code-block:: python

   from unitstools import Unit


   class Meters(Unit):
      ...


   def double_height(x: Meters) -> Meters:
      return 2 * x


   def square_height(x: Meters) -> Meters:
      # Checkers will raise a warning for this code, since squaring does not
      # preserve units.
      return x ** 2


   def sum_height(x: Meters) -> Meters:
      # Checkers will raise a warning for this code, since 10 has no units.
      return x + 10

.. currentmodule:: unitstools

.. note::

   The classes :class:`Unit` and :class:`IntUnit` are never actually instantiated
   (for more details, see :doc:`technicaldetails`), and neither are user-defined
   derived classes that establish the units (see the example further below).
   Their purpose is entirely for type hinting via their pseudo-instantiation syntax
   and/or through :func:`strip_unit` and :func:`embed_unit`.

Keep in mind  that the following are equivalent:

.. code-block:: python

   class Kilometers(Unit):
      ...

   x = Kilometers(100)

.. code-block:: python

   class Kilometers(Unit):
      ...

   x = embed_units(100, Kilometers)

The user should decide which syntax to use based primarily on preference.

Examples
--------

The following code does not raise any warnings.

.. code-block:: python

   from unitstools import Unit


   class Seconds(Unit):
      ...


   def add_one_second(second: Seconds) -> Seconds:
      return second + embed_unit(1, Seconds)


   def main():
      starting_time = embed_unit(30, Seconds)
      starting_time_plus_one = add_one_second(starting_time)


On the other hand, Pylance raises a warning for the following code in the
:func:`add_one_second function`, saying that you can't sum a
:class:`Seconds` with a Literal[1].

.. code-block:: python

   from unitstools import Unit


   class Seconds(Unit):
      ...


   def add_one_second(second: Seconds) -> Seconds:
      return second + 1


   def main():
      starting_time = embed_unit(30, Seconds)
      starting_time_plus_one = add_one_second(starting_time)


Alternatively, one could fix the code above as follows:

.. code-block:: python

   from unitstools import Unit


   class Seconds(Unit):
      ...


   def add_one_second(second: Seconds) -> Seconds:
      return second + Seconds(1)


   def main():
      starting_time = Seconds(30)
      starting_time_plus_one = add_one_second(starting_time)


.. note::

   This package makes no runtime conversion. In a sense, it works similarly to the
   behavior of functions such as :func:`typing.cast`, in that at runtime "nothing"
   happens (yes, there is a function call, but it just returns the value and moves
   on). This helps keep performance of number operations instead by still using
   builtin types, while also allowing the aforementioned advantages.
