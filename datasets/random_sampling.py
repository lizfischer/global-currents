import sys, random, math

##############################################################
#  Writes a random <pct>% of a CSV file to another CSV file  #
#  Assumes input file lacks headers (as our results CSVs do.)#
#  Assigns the string defined in <headers> as the column     #
#  in the new file.                                          #
##############################################################

def calcPercent(pct):
    return float(pct)/100

def doSampling(percent, lines):
    sample_size = int(math.ceil(len(lines)*percent)) #Calculate sample size, rounded up
    sample = random.sample(lines, sample_size) #Get <sample size> number of tuples from <lines>
    return sample

def writeFile(header, lines, file):
    file.write(header)
    for item in lines:
        file.write(item)

def randomSampleCSV(source, output, pct, headers):
    print("Copying random " + str(pct) + "% of "+ source.name +" to " + output.name)
    lines = [line for line in source] #Read lines from file into memory
    random_sample = doSampling(calcPercent(pct), lines)
    writeFile(headers, random_sample, output)

def main():
    if len(sys.argv) < 4: #if not enough arguments
        print ("Please specify a file to read, a file to write, and the percent (e.g. 15) to get")
    else:
        headers = "URL,Label,X,Y,W,H\n"
        with open(sys.argv[1], "rb") as inFile, open(sys.argv[2], "wb") as outFile:
            randomSampleCSV(inFile, outFile, sys.argv[3], headers)


if __name__ == "__main__":
    main()
