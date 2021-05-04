# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

import sphinx_py3doc_enhanced_theme

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
]
if os.getenv('SPELLCHECK'):
    extensions += 'sphinxcontrib.spelling',
    spelling_show_suggestions = True
    spelling_lang = 'en_US'

source_suffix = '.rst'
master_doc = 'index'
project = 'Enhanced Sphinx theme (based on Python 3 docs)'
year = '2014-2015'
author = 'Ionel Cristian Mărieș'
copyright = '{0}, {1}'.format(year, author)
version = release = '2.4.0'

html_theme = "sphinx_py3doc_enhanced_theme"
html_theme_path = [sphinx_py3doc_enhanced_theme.get_html_theme_path()]
html_theme_options = {
    'githuburl': 'https://github.com/ionelmc/sphinx-py3doc-enhanced-theme/',
}
if os.environ.get('EXTRASTYLING', 'false') == 'false':
    html_theme_options.update({
        'bodyfont': '"Lucida Grande",Arial,sans-serif',
        'headfont': '"Lucida Grande",Arial,sans-serif',
        'codefont': 'monospace,sans-serif',
        'linkcolor': '#0072AA',
        'visitedlinkcolor': '#6363bb',
        'extrastyling': False,
    })
    pygments_style = 'friendly'
else:
    pygments_style = 'trac'
templates_path = ['.']
html_use_smartypants = True
html_last_updated_fmt = '%b %d, %Y'
html_split_index = True
html_sidebars = {
    '**': ['searchbox.html', 'globaltoc.html', 'sourcelink.html'],
}
html_short_title = '%s-%s' % (project, version)
