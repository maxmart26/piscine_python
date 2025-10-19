"""
ft_package — A sample test package for 42.

Expose:
- hello(name="world") -> str
- __version__
"""

__all__ = ["hello", "__version__"]
__version__ = "0.0.1"


def hello(name: str = "world") -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}!"
