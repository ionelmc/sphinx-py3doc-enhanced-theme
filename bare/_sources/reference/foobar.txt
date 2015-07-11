:mod:`foobar` --- Boring lorem ipsum
=====================================

.. module:: foobar
    :synopsis: Some other fake module to test rendering


.. sourcecode:: pycon

    >>> def fib(n):
    >>>     a, b = 0, 1
    >>>     while a < n:
    >>>         print(a, end=' ')
    >>>         a, b = b, a+b
    >>>     print()
    >>> fib(1000)
    0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987

.. sourcecode:: python

    def fib(n):
        a, b = 0, 1
        while a < n:
            print(a, end=' ')
            a, b = b, a+b
        print()

    fib(1000)

Just goofing around with ``automodule`` ...
-------------------------------------------

::

    .. automodule:: tempfile
        :members:

----

.. automodule:: tempfile
    :members:
