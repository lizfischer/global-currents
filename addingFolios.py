import sys, csv
from gcutils.iiif import *

alreadyProcessed = {}

def processURL(url):
    druid = getDruid(url)
    data = getJSONfromDruid(druid)
    

    getFolioData(data, i) # i is Index of folio in canvas


    pass

def main():
    if len(sys.argv) < 3: #if not enough arguments
        print ("Usage: python addingFolios.py <input images> <output file>")
    else:
        with open(sys.argv[1], "rb") as infile, open(sys.argv[2], "wb") as outfile:
            for (line in infile):
                outfile.write(processURL(line))


if __name__ == "__main__":
    main()
