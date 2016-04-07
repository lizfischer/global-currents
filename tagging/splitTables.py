import csv, sys
from gcutils.iiif import *

def getSecColors(row):
    string = row[1]['secondary_colors']
    if string.strip() != "":
        return [x.strip() for x in string.split(';')]
    return []

def getError(row):
    string = row[1]['is_error']
    if string.strip() == "T":
        return 1
    return 0

def EC():
    infile = open(sys.argv[1], "rb")
    out_main= open(sys.argv[2]+".csv", "wb")
    out_c = open(sys.argv[2]+"_colors.csv", "wb")

    reader = csv.DictReader(infile, delimiter=',', quotechar='\"')
    main_writer = csv.writer(out_main, delimiter=',', quotechar='\"', quoting=csv.QUOTE_ALL)
    c_writer = csv.writer(out_c, delimiter=',', quotechar='\"', quoting=csv.QUOTE_ALL)

    for row in enumerate(reader):  
        # EC
        # url x y msNumber folioNumber w h primaryColor letter isError errorType notes

        main_writer.writerow([
            row[1]['URL'], row[1]['x'], row[1]['y'], row[1]['ms_no'], row[1]['folio'], row[1]['w'], row[1]['h'], row[1]['primary_color'].strip().lower(), row[1]['letter'].strip().upper(), row[1]['is_error'], row[1]['error_type'],
             row[1]['notes'].replace("\"", "'").strip()        
        ])

        for color in getSecColors(row):
                c_writer.writerow([row[1]['URL'], color.strip])    
   
    return


def main():
    if len(sys.argv) < 3: #if not enough arguments
        print ("Usage: python tagging_to_tables.py <input.csv> <feature: EC/LN/IS> <base for output>")
    else:
        if (sys.argv[1] == 'EC'):
            EC()
        elif (sys.argv[1] == 'LN'):
            LN()
        elif (sys.argv[1] == 'IS'):
            IS()
        else:
            print ("Please enter a valid feature code (EC, LN, IS).")

if __name__ == "__main__":
    main()
