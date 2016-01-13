import csv
import sys

if (len(sys.argv) != 3): 
	print('Please specify input and output CSV files')
	quit()
infile = open(sys.argv[1], 'rb')
outfile = open(sys.argv[2], 'wb')

row_count = sum(1 for row in infile)-1 #number of data rows (-1 accounts for header)
infile.close()
infile = open(sys.argv[1], 'rb')

reader = csv.DictReader(infile, delimiter = ',', quotechar='\"')
writer = csv.writer(outfile, delimiter=",", quotechar='\"', quoting=csv.QUOTE_MINIMAL)
fieldnames = ['URL', 'ms_no', 'page', 'rv', 'x', 'y', 'w', 'h', 'color']

#write header
writer.writerow(fieldnames)

for i, row in enumerate(reader):
	DocID = row['DocID']	

	## FOLIO INFO ##
	msIndex= DocID.find('%')+3 #find start of MS number in DocID
	pageIndex = DocID.find ('_')+1 #find start of folio number in DocID
	rvIndex = DocID.find('_', pageIndex)+1		
	
	ms_no = DocID[msIndex:pageIndex-1]			
	page = DocID[pageIndex:pageIndex+3]
	if (page[2] == '_'): page = page[:-1] #remove _ from end

	rv = DocID[rvIndex:rvIndex+1]
	if (rv == 'T'): rv = None
	
	## POSITION INFO ##
	x = row['x']
	y = row['y']
	w = row['w']
	h = row['h']
	#pageW = row['image.width']
	#pageH = row['image.height']
	#pctW = row['perc.w']
	#pctH = row['perc.h']
	color = ""				

	## RECONSTRUCT URL ##
	URL = "https://stacks.stanford.edu/image/iiif/"+row['DocID']+"/"+x+","+y+","+w+","+h+"/pct:40/0/default.jpg"

	## WRITE ##
	writer.writerow([URL, ms_no, page, rv, x, y, w, h, color])
	
print("Success!")
