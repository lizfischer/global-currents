#############################################
# Turn tagging CSVs into proper CSVs for DB #
#############################################

#"X,Y,MS_Number,F_Number, Width, Height, Primary_Color, Letter, IsError, URL, Notes"
import csv, sys
from gcutils.iiif import *

def extract():
    infile = open(sys.argv[1], "rb")
    out_main= open(sys.argv[2]+".csv", "wb")
    out_error=open(sys.argv[2]+"-error.csv", "wb")

    reader = csv.DictReader(infile, delimiter=',', quotechar='\"')
    main_writer = csv.writer(out_main, delimiter=',', quotechar='\"', quoting=csv.QUOTE_ALL)
    no_folio_writer = csv.writer(out_error, delimiter=',', quotechar='\"', quoting=csv.QUOTE_ALL)

    for row in enumerate(reader):
        ms_no = getMSNumber(row[1]['URL'])
        if (ms_no != '45'):
            folio = getFolio(row[1]['URL'])
            if (folio[0].isdigit() or folio[0] =='i'or folio[0] == 'x' or folio[0] =='v'): #try to get rid of covers and other misc pages
                main_writer.writerow([
                    row[1]['URL'], row[1]['x'], row[1]['y'], getMSNumber(row[1]['URL']), folio, row[1]['w'], row[1]['h']
                ])
            else:
                no_folio_writer.writerow([
                    row[1]['URL'], row[1]['x'], row[1]['y'], getMSNumber(row[1]['URL']), folio, row[1]['w'], row[1]['h'],
                ])
    return



def main():
    if len(sys.argv) < 3: #if not enough arguments
        print ("Usage: python is_totables.py <input.csv> <base for output>")
    else:
        extract()

if __name__ == "__main__":
    main()

