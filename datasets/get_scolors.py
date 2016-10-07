import sys, csv, string

def makeTaggingSpreadsheet(dataCSV, emptyCSV):
    fieldnames = ['URL', 'secondary_color']

    infile = open(dataCSV, 'rb')
    outfile = open(emptyCSV, 'wb')

    reader = csv.DictReader(infile, delimiter = ',', quotechar='\"')
    writer = csv.writer(outfile, delimiter=",", quotechar='\"', quoting=csv.QUOTE_MINIMAL)

    #write header
    writer.writerow(fieldnames)
    for i, row in enumerate(reader):
		URL = row['URL']
		colors = row['secondary_colors'].split(';')
		for j in colors:
			writer.writerow([URL, j])
    print("Success!")


def main():
    if len(sys.argv) < 3: #if not enough arguments
        print ("Please specify a file to read, and a file to write.")
    else:
        makeTaggingSpreadsheet(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()

