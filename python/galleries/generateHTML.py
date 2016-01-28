import csv, sys
from gcutils.iiif import *


if (len(sys.argv) < 3): 
	print('Please specify input CSV, and base name for HTML output files')
	quit()
infile = open(sys.argv[1], 'rb')
outfile = open(sys.argv[2]+".html", 'wb')
error = open("ERROR", 'a')
nRowsPer = 50 if len(sys.argv) < 4 else int(sys.argv[3])
percent = 40 if len(sys.argv) < 5 else int(sys.argv[4])

reader = csv.DictReader(infile, delimiter = ',', quotechar='\"')

index = 0
fileNum = 1
outfile.write("<div id='thumbnails'>")
for row in enumerate(reader):
	try:
		full = row[1]['URL']
		index += 1
		ms = getMSNumber(full)
		folio = getFolio(full)
		x = int(int(row[1]['X'])*2.5)
		y = int(int(row[1]['Y'])*2.5)
		w = int(int(row[1]['W'])*2.5)
		h = int(int(row[1]['H'])*2.5)
		thumb = getSectionURL(full, x,y,w,h)
		thumb = getPercentURL(thumb, percent)

		html = ("<a href='%s' data-lightbox='lb-%d' data-title='%s %s: %d,%d,%d,%d'>"
				 "<img class='thumbnail' onmouseover='preview.src=img%d.src' name='img%d' src='%s' alt=' '/>"
				 "</a>\n") % (full, index, ms, folio, x, y, w, h, index, index, thumb)

		if (index % nRowsPer == 0):
			outfile.write("</div>")
			fileNum += 1
			newFileName= sys.argv[2] + str(fileNum) + ".html"
			outfile = open(newFileName, 'wb')
			outfile.write("<div id='thumbnails'>")
		outfile.write(html)
	except:
		error.write(str(reader.line_num)+", "+str(row[1]['URL']))



#html = ("<div class='lazyload'>"
#        "<!--<a href='%s' data-lightbox='lb-%d' data-title='%s %s: %d,%d,%d,%d'>"
#        "<img onmouseover='preview.src=img%d.src' name='img%d' src='%s' alt=' '/>"
#        "</a>--></div>\n") % (full, index, ms, folio, x, y, w, h, index, index, thumb)
