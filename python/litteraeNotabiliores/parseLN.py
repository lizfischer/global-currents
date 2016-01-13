import csv
import sys

if (len(sys.argv) != 3):
	print('Please specify input CSV and output SQL files')
	quit()
infile = open(sys.argv[1], 'rb')
outfile = open(sys.argv[2], 'wb')

reader = csv.DictReader(infile, delimiter = ',', quotechar='\"')

outfile.write("DELETE FROM Littera_Notabilior;\n")
outfile.write("DELETE FROM LN_Second_Color;\n")

for row in enumerate(reader):
    URL = row[1]['URL']
    Letter = row[1]['Letter']
    PColor = row[1]['primary color']
    SColor_str = row[1]['secondary colors']
    Error = row[1]['is Error']
    if (Error == 'T'): Error = 1
    else: Error = 0

    Notes = row[1]['Error Description']
    MS = row[1]['ms_no']
    Page = row[1]['page']
    RV = row[1]['rv']
    X = row[1]['x']
    Y = row[1]['y']
    W = row[1]['w']
    H = row[1]['h']

    ## SEPARATE Secondary Colors ##
    SColors = SColor_str.split(";")
    for c in SColors:
        c = c.strip()

    ## WRITE ##
    outfile.write("INSERT INTO Littera_Notabilior (X,Y,MS_Number,F_Number,Width,Height,Primary_Color,Letter,IsError,URL,Notes)"
                  "VALUES ('"+X+"','"+Y+"',"+MS+"','"+Page+"','"+W+"','"+H+"','"+PColor+"','"+Letter+"','"+Error+"','"+URL+"','"+Notes+");\n")

    for color in SColors:
        outfile.write("INSERT INTO LN_Second_Colors (Language, MS_Number) VALUES ('"+lang+"','"+MS_Number+"');\n")
    for d in dates:
        tmp = d.split("-")
        century = str(tmp[0])
        if len(tmp) == 2:
            superscript = str(tmp[1])
        else: superscript = ""
        outfile.write("INSERT INTO Date(Century,Super, MS_Number)VALUES("+century+",'"+superscript+"','"+MS_Number+"');\n")

print("Success!")