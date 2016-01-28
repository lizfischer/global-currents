from gcutils.iiif import *
import sys, csv

def run():
    infile = open(sys.argv[1], "rb")
    outfile= open(sys.argv[2], "a")
    reader = csv.DictReader(infile, delimiter=',', quotechar='\"')

    for i, row in enumerate(reader):
        if '' in (row['X'], row['Y'], row['W'], row['H']):
            outfile.write(row[''] + ", " + row['URL'] +"\n")

def main():
    if len(sys.argv) < 3: #if not enough arguments
        print ("Please specify input .csv, and output file")
    else:
        run()

if __name__ == "__main__":
    main()

