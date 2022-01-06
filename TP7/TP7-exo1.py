import sys

def main(argv):
    print (f"le nombre d'argument est {len(argv)}")
    if len(argv) <=1:
        print (f" pas assez d'arguments")
    else:
        print(f" il y a assez d'arguments")

if (__name__ == "__main__"):
    main(sys.argv)
