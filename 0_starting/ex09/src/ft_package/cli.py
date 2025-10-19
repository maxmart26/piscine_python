from . import hello, __version__


def main() -> None:
    """Console script: prints a greeting."""
    import argparse

    parser = argparse.ArgumentParser(prog="ft-hello", description="Say hello from ft_package")
    parser.add_argument("name", nargs="?", default="world", help="Name to greet")
    args = parser.parse_args()

    print(hello(args.name))
