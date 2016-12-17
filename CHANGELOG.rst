Changelog
=========

2.4.0 (2016-12-17)
------------------

* Added option to use Google Web Fonts. Contributed by Marius P Isken in 
  `#11 <https://github.com/ionelmc/sphinx-py3doc-enhanced-theme/pull/11>`_.

2.3.2 (2015-12-24)
------------------

* Fixed regression in sidebar size when there was no page content. Sidebar has its own height again.

2.3.1 (2015-12-18)
------------------

* Fixed sidebar contents not moving while scrolling at all.

2.3.0 (2015-12-18)
------------------

* Removed use of ``!important`` from various places. Contributed by Matthias Geier in
  `#10 <https://github.com/ionelmc/sphinx-py3doc-enhanced-theme/pull/10>`_.

2.2.4 (2015-10-23)
------------------

* Removed awkward bottom padding of paragraphs in table cells.
* Fix highlight of "p" anchors (that have id and got :target).

2.2.3 (2015-09-13)
------------------

* Fixed display of argument descriptions when there are multiple paragraphs. First paragraph shouldn't be on a second line.

2.2.2 (2015-09-12)
------------------

* Fixed issues with highlighting a section (via anchor location hash). Previously code blocks would get ugly bar on the left.

2.2.1 (2015-08-21)
------------------

* Fixed positioning of navigation sidebar when displayed in narrow mode (at the bottom). Previously it overlapped the
  footer.

2.2.0 (2015-08-19)
------------------

* Added the ``appendcss`` theme options for quick customization.
* Added the ``path`` setuptools entrypoint so ``html_theme_path`` doesn't need to be set anymore in ``conf.py``.

2.1.1 (2015-07-11)
------------------

* Remove background from reference links when ``extrastyling`` is off.

2.1.0 (2015-07-11)
------------------

* Added new theme option ``extrastyling`` which can be used to get the
  original Python 3 docs styling (green code blocks, gray inline code
  blocks, no text shadows etc)
* The ``py.png`` favicon is renamed to ``favicon.png``.
* Added some examples for customizing the styling or using a custom favicon.

2.0.2 (2015-07-08)
------------------

* Make inline code blocks bold.

2.0.1 (2015-03-25)
------------------

* Fix inclusion of default.css (now classic.css).

2.0.0 (2015-03-23)
------------------

* Use HTML5 doctype and force IE into Edge mode.
* Add a embedded flag that removes JS (for building CHM docs).
* Inherit correct theme (default renamed in Sphinx 1.3).

1.2.0 (2015-02-24)
------------------

* Fat-fingered another version. Should had been 1.0.1 ... damn.

1.1.0 (2015-02-24)
------------------

* Match some markup changes in latest Sphinx.

1.0.0 (2015-02-13)
------------------

* Fix depth argument for toctree (contributed by Georg Brandl).

0.1.0 (2014-05-31)
------------------

* First release on PyPI.
