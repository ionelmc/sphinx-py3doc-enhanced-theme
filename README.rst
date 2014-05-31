=================================================
Enhanced theme based on py3 documentation's theme
=================================================

.. image:: http://img.shields.io/pypi/v/sphinx_py3doc_enhanced_theme.png
    :alt: PYPI Package
    :target: https://pypi.python.org/pypi/sphinx_py3doc_enhanced_theme

.. image:: http://img.shields.io/pypi/dm/sphinx_py3doc_enhanced_theme.png
    :alt: PYPI Package
    :target: https://pypi.python.org/pypi/sphinx_py3doc_enhanced_theme

A theme based on the theme of https://docs.python.org/3/

Installation
============

::

    pip install sphinx_py3doc_enhanced_theme
    
Add this in your documentation's ``conf.py``::

    import sphinx_py3doc_enhanced_theme
    html_theme = " 	sphinx_py3doc_enhanced_theme"
    html_theme_path = [sphinx_py3doc_enhanced_theme.get_html_theme_path()]
