import sys, csv

def combineFiles(inputFiles, output):
	with open(output, 'w') as outfile:
	    for fname in inputFiles:
		with open(fname) as infile:
		    for line in infile:
		        outfile.write(line)
		    print(fname+'\n')
	print('Finished combining files.')

def findDuplicateLines(file1, file2):
	duplicates = []
	with open(file1,"r") as f1, open(file2,"r") as f2:
		f1_lines = f1.read().splitlines()
		f2_lines = f2.read().splitlines()
		for line in f1_lines:
			if line in f2_lines:
				duplicates.append(line)
	return duplicates
