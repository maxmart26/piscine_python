#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) == 1:
        return
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return
    arg = sys.argv[1]
    if arg.lstrip("-").isdigit():
        number = int(arg)
        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    else:
        print("AssertionError: argument is not an integer")


if __name__ == "__main__":
    main()
