import sys, csv, string

#####################################################
#  For LNs and ECs.                                 #
#  Creates the tagging spreadsheets for student use #
#  from the results CSV files we got back           #
#####################################################


## Adds coords to a IIIF URL ##
def getSectionURL(fullURL, X, Y, W, H):
    sectionStr = str(X)+','+str(Y)+','+str(W)+','+str(H)
    urlParts = string.split(fullURL, "full", 1)
    if len(urlParts) == 2:
        return urlParts[0]+sectionStr+urlParts[1]
    return ""

## Takes data CSV and makes a spreadsheet to be used for tagging ##
def makeTaggingSpreadsheet(dataCSV, emptyCSV):
    fieldnames = ['URL', 'letter', 'primary color', 'secondary colors', 'is_error', 'ms_no', 'folio', 'x', 'y', 'w', 'h', 'notes']
    empty = ''

    infile = open(dataCSV, 'rb')
    outfile = open(emptyCSV, 'wb')

    reader = csv.DictReader(infile, delimiter = ',', quotechar='\"')
    writer = csv.writer(outfile, delimiter=",", quotechar='\"', quoting=csv.QUOTE_MINIMAL)

    #write header
    writer.writerow(fieldnames)
    for i, row in enumerate(reader):
            URL = row['URL']

            #Scale up coords for full size image
            X = int(int(row['X']) * 2.5)
            Y = int(int(row['Y']) * 2.5)
            W = int(int(row['W']) * 2.5)
            H = int(int(row['H']) * 2.5)

            URL = getSectionURL(URL, X, Y, W, H)

            msIndex= URL.find('%')+3 #find start of MS number in URL
            pageIndex = URL.find('_')+1 #find start of folio number in URL
            rvIndex = URL.find('_', pageIndex)+1 #find _ starting from page index to get just before RV, then add 1

            ms_no = URL[msIndex:pageIndex-1].lstrip("0")
            page = URL[pageIndex:rvIndex-1].lstrip("0")

            rv = URL[rvIndex:rvIndex+1]
            if (rv != 'T'):
                page += " "+rv

            # fieldnames = ['URL', 'letter', 'primary color', 'secondary colors', 'is_error', 'ms_no', 'folio', 'x', 'y', 'w', 'h', 'notes']
            writer.writerow([URL, empty, empty, empty, empty, ms_no, page, X, Y, W, H, empty])

    print("Success!")


def main():
    if len(sys.argv) < 3: #if not enough arguments
        print ("Please specify a file to read, and a file to write.")
    else:
        makeTaggingSpreadsheet(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()

