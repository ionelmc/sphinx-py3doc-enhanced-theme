=================================================
Enhanced theme based on py3 documentation's theme
=================================================

| |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/sphinx-py3doc-enhanced-theme/badge/?style=flat
    :target: https://readthedocs.org/projects/sphinx-py3doc-enhanced-theme
    :alt: Documentation Status

.. |travis| image:: http://img.shields.io/travis/ionelmc/sphinx-py3doc-enhanced-theme/master.png?style=flat
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/ionelmc/sphinx-py3doc-enhanced-theme

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/ionelmc/sphinx-py3doc-enhanced-theme?branch=master
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/ionelmc/sphinx-py3doc-enhanced-theme

.. |coveralls| image:: http://img.shields.io/coveralls/ionelmc/sphinx-py3doc-enhanced-theme/master.png?style=flat
    :alt: Coverage Status
    :target: https://coveralls.io/r/ionelmc/sphinx-py3doc-enhanced-theme

.. |landscape| image:: https://landscape.io/github/ionelmc/sphinx-py3doc-enhanced-theme/master/landscape.svg?style=flat
    :target: https://landscape.io/github/ionelmc/sphinx-py3doc-enhanced-theme/master
    :alt: Code Quality Status

.. |version| image:: http://img.shields.io/pypi/v/sphinx-py3doc-enhanced-theme.png?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/sphinx-py3doc-enhanced-theme

.. |downloads| image:: http://img.shields.io/pypi/dm/sphinx-py3doc-enhanced-theme.png?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/sphinx-py3doc-enhanced-theme

.. |wheel| image:: https://pypip.in/wheel/sphinx-py3doc-enhanced-theme/badge.png?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/sphinx-py3doc-enhanced-theme

.. |supported-versions| image:: https://pypip.in/py_versions/sphinx-py3doc-enhanced-theme/badge.png?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/sphinx-py3doc-enhanced-theme

.. |supported-implementations| image:: https://pypip.in/implementation/sphinx-py3doc-enhanced-theme/badge.png?style=flat
    :alt: Supported imlementations
    :target: https://pypi.python.org/pypi/sphinx-py3doc-enhanced-theme

.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/ionelmc/sphinx-py3doc-enhanced-theme/master.png?style=flat
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/ionelmc/sphinx-py3doc-enhanced-theme/

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
