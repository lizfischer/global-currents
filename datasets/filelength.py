import sys

percentages = [.10, .15, .20, .25]

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def main():
    if len(sys.argv) < 2: #if not enough arguments
        print ("Please specify file")
    else:
        n_items = file_len(sys.argv[1])-1
        for p in percentages:
            print str(int(p*100)) + ": " + str(int(n_items*p))

if __name__ == "__main__":
    main()
