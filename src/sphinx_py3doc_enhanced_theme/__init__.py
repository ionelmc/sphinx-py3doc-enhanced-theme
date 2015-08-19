import os

__version__ = "2.2.0"


def get_html_theme_path():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), 'themes'))
