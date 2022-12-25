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
the expected units involved in operations.


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

The classes :class:`Unit` and :class:`IntUnit` should never be instantiated, and
neither the derived classes that define the units just as in the exemple above.

Instead, they should be used just for type hinting and type casting should be
managed via :func:`strip_unit` and :func:`embed_unit`.

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


This package makes it more difficult for magic constants that actually
have units to silently live in the code preventing things like a sustainable
units conversion for example.