__version__ = '2.4.0'

import os


def get_html_theme_path():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), 'themes'))
