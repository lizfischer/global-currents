import csv
import sys

if (len(sys.argv) != 3): 
	print('Please specify input CSV and output SQL files')
	quit()
infile = open(sys.argv[1], 'rb')
outfile = open(sys.argv[2], 'wb')

reader = csv.DictReader(infile, delimiter = ',', quotechar='\"')

outfile.write("DELETE FROM Manuscript;\n")
outfile.write("DELETE FROM Date;\n")
outfile.write("DELETE FROM Location;\n")
outfile.write("DELETE FROM Language;\n")

for row in enumerate(reader):
    MS_Number = row[1]['MS_Number']
    Columns = row[1]['Columns']
    Language = row[1]['Language']
    Date = row[1]['Century']
    Institution = row[1]['Institution']
    Region = row[1]['Region']
    Title = row[1]['Title']

    Title = Title.replace("'","''")
    Region = Region.replace("'","''")
    Institution = Institution.replace("'","''")

    ## SEPARATE LANGUAGES ##
    languages = Language.split(";")
    for l in languages:
        l = l.strip()
        l= l.replace("'","''")

    ## SEPARATE DATES ##
    dates = Date.split(";")

    ## WRITE ##
    outfile.write("INSERT INTO Manuscript VALUES ('"+MS_Number+"','"+Title+"',"+Columns+");\n")
    outfile.write("INSERT INTO Location (Region, Institution, MS_Number) VALUES('"+Region+"','"+Institution+"','"+MS_Number+"');\n")
    
    for lang in languages:
        outfile.write("INSERT INTO Language (Language, MS_Number) VALUES ('"+lang+"','"+MS_Number+"');\n")
    for d in dates:
        tmp = d.split("-")
        century = str(tmp[0])
        if len(tmp) == 2:
            superscript = str(tmp[1])
        else: superscript = ""
        outfile.write("INSERT INTO Date(Century,Super, MS_Number)VALUES("+century+",'"+superscript+"','"+MS_Number+"');\n")
    
print("Success!")
