import sys
def main():
    if len(sys.argv) < 2: #if not enough arguments
        print ("Usage: python removeBlank.py <input csv>")
    else:
        with open(sys.argv[1], "rb") as file, open(sys.argv[1]+"-stripped", "wb") as out:
            for line in file:
                if line.strip():
                    out.write(line)

if __name__ == "__main__":
    main()
