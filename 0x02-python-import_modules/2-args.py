#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    length = (len(sys.argv) - 1)

    if length == 1:
        print("1 argument:")
    elif length == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(length))

    for x in range(1, len(sys.argv)):
        print("{:d}:".format(x), str(sys.argv[x]))
