==============================================
Enhanced Sphinx theme (based on Python 3 docs)
==============================================

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor|
        |
    * - package
      - |version| |downloads|

.. |docs| image:: https://readthedocs.org/projects/sphinx-py3doc-enhanced-theme/badge/?style=flat
    :target: https://readthedocs.org/projects/sphinx-py3doc-enhanced-theme
    :alt: Documentation Status

.. |travis| image:: http://img.shields.io/travis/ionelmc/sphinx-py3doc-enhanced-theme/master.svg?style=flat&label=Travis
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/ionelmc/sphinx-py3doc-enhanced-theme

.. |appveyor| image:: https://img.shields.io/appveyor/ci/ionelmc/sphinx-py3doc-enhanced-theme/master.svg?style=flat&label=AppVeyor
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/ionelmc/sphinx-py3doc-enhanced-theme

.. |version| image:: http://img.shields.io/pypi/v/sphinx-py3doc-enhanced-theme.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/sphinx-py3doc-enhanced-theme

.. |downloads| image:: http://img.shields.io/pypi/dm/sphinx-py3doc-enhanced-theme.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/sphinx-py3doc-enhanced-theme

A theme based on the theme of https://docs.python.org/3/ with some responsive enhancements.

* Free software: BSD license

Installation
============

::

    pip install sphinx_py3doc_enhanced_theme

Add this in your documentation's ``conf.py``:

.. sourcecode:: python

    import sphinx_py3doc_enhanced_theme
    html_theme = "sphinx_py3doc_enhanced_theme"
    html_theme_path = [sphinx_py3doc_enhanced_theme.get_html_theme_path()]

Customization
=============

Options
-------

Custom favicon
--------------

To have a custom favicon create a ``theme`` directory near your ``conf.py`` and add this ``theme.conf`` in it:

.. sourcecode:: ini

    [theme]
    inherit = sphinx_py3doc_enhanced_theme

Then create a ``favicon.png`` in the ``static`` directory.

And then edit your ``conf.py`` to have something like this:

.. sourcecode:: python

    import sphinx_py3doc_enhanced_theme
    html_theme = "theme"
    html_theme_path = [sphinx_py3doc_enhanced_theme.get_html_theme_path(), "."]

The final file structure should be like this::

    docs
    ├── conf.py
    └── theme
        ├── static
        │   └── favicon.png
        └── theme.conf

Examples
========

* http://python-aspectlib.readthedocs.org/en/latest/
* http://python-manhole.readthedocs.org/en/latest/
