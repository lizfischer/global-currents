import csv
import sys

#infile = open('ln_stats.csv', 'rb')
#outfile = open('ln_test.json','wb')

row_count = sum(1 for row in infile)-1 #number of data rows (-1 accounts for header)
infile.close()
infile = open('ln_stats.csv', 'rb')

reader = csv.DictReader(infile, delimiter = ',', quotechar='\"')
fieldnames = ['URL', 'ms_no', 'page', 'rv', 'x', 'y', 'w', 'h', 'pageW', 'pageH', 'pctW', 'pctH', 'color']

TAB = "    "


#Write header
outfile.write('{ "lns" : [\n') 

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
	pageW = row['image.width']
	pageH = row['image.height']
	pctW = row['perc.w']
	pctH = row['perc.h']

	
	color = ""				

	## RECONSTRUCT URL ##
	URL = "https://stacks.stanford.edu/image/iiif/"+row['DocID']+"/"+x+","+y+","+w+","+h+"/pct:40/0/default.jpg"

	## FORMATTING ##
	outfile.write(TAB+'{\n')
	outfile.write(TAB+TAB+'\"url\":\"'+URL+'\",\n')
	outfile.write(TAB+TAB+'\"ms_no\":\"'+ms_no+'\",\n')
	outfile.write(TAB+TAB+'\"folio\":\"'+page+'\",\n')
	outfile.write(TAB+TAB+'\"rv\":')
	if (rv != None): outfile.write('\"'+rv+'\"')
	else: outfile.write('null')
	outfile.write(',\n')
	outfile.write(TAB+TAB+'\"x\":'+x+',\n') 
	outfile.write(TAB+TAB+'\"y\":'+y+',\n') 
	outfile.write(TAB+TAB+'\"w\":'+w+',\n') 
	outfile.write(TAB+TAB+'\"h\":'+h+',\n')
	outfile.write(TAB+TAB+'\"pctW\":'+pctW+',\n')
	outfile.write(TAB+TAB+'\"pctH\":'+pctH+',\n')
	outfile.write(TAB+TAB+'\"color\":null\n')
	outfile.write(TAB+"}")
	if (i!=row_count-1): outfile.write(',') #write comma after entry unless it's the last one
	outfile.write('\n')

#Write footer
outfile.write(']}')
print("Success!")
