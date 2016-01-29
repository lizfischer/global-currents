import sys, random, math

##############################################################
#  Writes a random <pct>% of a CSV file to another CSV file  #
#  Assumes input file lacks headers (as our results CSVs do.)#
#  Assigns the string defined in <headers> as the column     #
#  in the new file.                                          #
##############################################################

def randomSampleCSV(inFile, outFile, pct, headers):
    percent = float(pct)/100
    with open(inFile, "rb") as source, open(outFile, 'w') as output:
        print("Copying random " + str(percent*100) + "% of "+ source.name +" to " + output.name)
        lines = [line for line in source] #Read lines from file into memory
        sample_size = int(math.ceil(len(lines)*percent)) #Calculate sample size, rounded up
        random_sample = random.sample(lines, sample_size) #Get <sample size> number of tuples from <lines>

        output.write(headers) #add column headers to output file
        for item in random_sample:
            output.write(item)


def main():
    if len(sys.argv) < 4: #if not enough arguments
        print ("Please specify a file to read, a file to write, and the percent (e.g. 15) to get")
    else:
        headers = "URL,Label,X,Y,W,H\n"
        randomSampleCSV(sys.argv[1], sys.argv[2], sys.argv[3], headers)


if __name__ == "__main__":
    main()