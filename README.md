# Universal-setup.py
A single setup.py file for all my Python projects

## Instructions:
To use, simply copy the `setup.py` file in this repo into the top level
of a Python project. This setup script requires Python 3.5 or greater, but
making it work with an earlier version should be pretty simple. This is left
as an exercise for the reader. ;)

### Note:
In order to get the most out of this setup script, a few things should be
kept in mind:

* [PEP 8](https://www.python.org/dev/peps/pep-0008/) should be used throughout your code.
* Your `__init__.py` files should start with a single line description of
it's package.
* You should use the `__author__`, `__version__`, `__email__`, and
`__license__` variables in your `__init__.py` file.
* Your dependencies should be in a file called `requirements.txt` in the same
 directory as the `setup.py` file.

I've tried to stick with convention with these design choices. If you don't
like them, feel free to make your own version of this script. :)
