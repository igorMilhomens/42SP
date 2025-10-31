import sys


if __name__ == "__main__":
    try:
        value_float = sys.argv[1]
        print(float(value_float))
    except ValueError:
        print("conversion impossible")
