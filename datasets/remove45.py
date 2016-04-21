import sys, csv
from gcutils.iiif import *


#####################################################
# Removes data from manuscript 45 from a .csv file  #
#####################################################

def remove(input, output):
    fieldnames = input.fieldnames
    print(fieldnames)
    output.writerow(fieldnames)
    for row in enumerate(input):
        msno = getMSNumber(row[1]['URL'])
        if msno != '45':
            out_row = []
            for key in fieldnames:
                out_row.append(row[1][key])
            output.writerow(out_row)

def main():
    if len(sys.argv) < 3: #if not enough arguments
        print ("Usage: python remove45.py <input csv> <output csv>")
    else:
        with open(sys.argv[1], "rb") as inFile, open(sys.argv[2], "wb") as outFile:
            reader = csv.DictReader(inFile, delimiter=',', quotechar='\"')
            writer = csv.writer(outFile, delimiter=',', quotechar='\"', quoting=csv.QUOTE_ALL)
            remove(reader, writer)

if __name__ == "__main__":
    main()