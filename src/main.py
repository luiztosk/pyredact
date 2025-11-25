import sys

from pyredact import PyRedact

def main():
    try:
        red = PyRedact()
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)
    red.redact()
    red.diff()