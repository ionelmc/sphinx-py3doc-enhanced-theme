:mod:`foo.bar` --- Boring lorem ipsum
=====================================

.. module:: foo.bar
    :synopsis: Some fake module to test rendering

Lorem ipsum dolor sit amet, consectetur adipiscing elit. In auctor mi odio, quis vehicula quam gravida at. Aliquam
venenatis ante augue, vel aliquam nulla porttitor a. Donec congue, metus quis viverra ultrices, mauris tellus sagittis
lectus, ac varius felis est nec sem. Etiam quis condimentum dui, non mollis nisi. Donec vehicula laoreet lorem et
dapibus. Etiam faucibus pulvinar nulla in lobortis. Fusce in ultricies lectus. Nulla felis leo, tristique vel venenatis
eget, placerat sit amet turpis. Nullam eget arcu vel ipsum finibus porttitor non nec quam.

.. seealso::

    The :mod:`foobar` offers some more lorem ipsum.

.. note::

    Pellentesque elementum convallis ``$nibh``, et semper nunc ornare et. Ut posuere condimentum auctor. Pellentesque
    ultricies nisi pellentesque ipsum tempus varius. Donec in tempor turpis, imperdiet euismod ligula. Vivamus ut tellus
    augue. Nunc porta porttitor purus non viverra. Cras in ante sed nibh pulvinar mattis in a neque. Lorem ipsum dolor
    sit amet, consectetur adipiscing elit. Suspendisse potenti. Aenean tristique congue nibh tincidunt sodales. In
    porttitor rhoncus lacus, sit amet condimentum tellus lacinia vel.

.. function:: bob(val)

    Sed pellentesque pretium magna, in ``{"pulvinar": "justo"}`` bibendum at. Aliquam at leo non urna mollis consequat
    nec in felis. Duis dui magna, ultrices eget nisl non, dapibus pretium risus. Proin eget risus eget est tempor
    dictum. Duis vehicula faucibus leo ac luctus. Nulla lobortis neque non aliquet hendrerit.

    ::

        foo
            bar

    .. sourcecode:: python

        def foo():
            return bar

    .. note:: Blublublub

        Some more stuff here:

        ::

            foo
                bar

        .. sourcecode:: python

            def foo():
                return bar

.. function:: lorem(ipsum)

    Nulla volutpat dignissim maximus. Nunc at erat sem. Proin justo augue, porttitor a erat non, elementum dignissim sem.
    Vestibulum hendrerit aliquam scelerisque. Aenean bibendum nibh id neque interdum, nec cursus ligula dapibus. Ut in
    nulla sit amet sem pretium tristique non vel ante.

.. py:function:: foo.bar(target, args=(), kwargs=None, setup=None)

    :type  args: list or tuple
    :param args:

    :type  kwargs: dict
    :param kwargs:

    :type  setup: callable
    :param setup: The setup function can also return the arguments for the function (in case you need to create new arguments every time).

        .. sourcecode:: python

            def test_with_setup(benchmark):
                def setup():
                    # can optionally return a (args, kwargs) tuple
                    return (1, 2, 3), {'foo': 'bar'}
                benchmark.pedantic(stuff, setup=setup, rounds=100)

        .. note::

            if you use a ``setup`` function then you cannot use the ``args``, ``kwargs`` and ``iterations`` options.
