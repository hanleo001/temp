import sys

def default():
    print("Hello")

def dog():
    print("Wolf")

def main():
    if sys.argv[1] != "dog":
        default()
    else:
        dog()


if __name__ == "__main__":
    main()
