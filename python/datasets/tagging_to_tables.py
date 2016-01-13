#"X,Y,MS_Number,F_Number, Width, Height, Primary_Color, Letter, IsError, URL, Notes"
import csv, sys
from gcutils.iiif import *

def getSecColors(row):
    string = row[1]['secondary_colors']
    if string != "":
        return [x.strip() for x in string.split(';')]
    return []

def extract():
    infile = open(sys.argv[1], "rb")
    out_main= open(sys.argv[2]+".csv", "wb")
    out_c = open(sys.argv[2]+"_colors.csv", "wb")

    reader = csv.DictReader(infile, delimiter=',', quotechar='\"')
    main_writer = csv.writer(out_main, delimiter=',', quotechar='\"', quoting=csv.QUOTE_ALL)
    c_writer = csv.writer(out_c, delimiter=',', quotechar='\"', quoting=csv.QUOTE_ALL)

    for row in enumerate(reader):
        if row[1]['ms_no'] != '45':
            main_writer.writerow([
                row[1]['URL'], row[1]['x'], row[1]['y'], getMSNumber(row[1]['URL']), getFolio(row[1]['URL']), row[1]['w'],
                row[1]['h'], row[1]['primary_color'], row[1]['letter'], row[1]['is_error'], row[1]['notes'].replace("\"", "'")
            ])

            for color in getSecColors(row):
                c_writer.writerow([row[1]['URL'], color])
    return



def main():
    if len(sys.argv) < 3: #if not enough arguments
        print ("Please specify input .csv and base name for output")
    else:
        extract()

if __name__ == "__main__":
    main()

