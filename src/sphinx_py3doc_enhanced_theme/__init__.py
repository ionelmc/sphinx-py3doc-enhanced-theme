import os

__version__ = "1.1.0"


def get_html_theme_path():
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
