import sys

def cat():
    print("Meiow")

def default():
    print("Hello")

def dog():
    print("Wolf")

def main():
<<<<<<< HEAD
    if sys.argv[1] == 'cat':
        cat()
    else:
    default()
=======
    if sys.argv[1] != "dog":
        default()
    else:
        dog()
>>>>>>> dog


if __name__ == "__main__":
    main()
