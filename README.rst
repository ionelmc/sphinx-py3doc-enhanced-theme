=================================================
Enhanced theme based on py3 documentation's theme
=================================================

| |version| |downloads|

.. |version| image:: http://img.shields.io/pypi/v/sphinx-py3doc-enhanced-theme.png?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/sphinx-py3doc-enhanced-theme

.. |downloads| image:: http://img.shields.io/pypi/dm/sphinx-py3doc-enhanced-theme.png?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/sphinx-py3doc-enhanced-theme

A theme based on the theme of https://docs.python.org/3/ with some responsive enhancements.

* Free software: BSD license

Installation
============

::

    pip install sphinx_py3doc_enhanced_theme
    
Add this in your documentation's ``conf.py``::

    import sphinx_py3doc_enhanced_theme
    html_theme = "sphinx_py3doc_enhanced_theme"
    html_theme_path = [sphinx_py3doc_enhanced_theme.get_html_theme_path()]

Examples
========

* http://python-aspectlib.readthedocs.org/en/latest/
* http://python-manhole.readthedocs.org/en/latest/
