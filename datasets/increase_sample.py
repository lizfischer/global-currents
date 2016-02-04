import sys, random_sampling

##############################################################
#  Writes a random <pct>% of a CSV file to another CSV file  #
#  Assumes input file lacks headers (as our results CSVs do.)#
#  Assigns the string defined in <headers> as the column     #
#  in the new file.                                          #
##############################################################


def increaseSample(input, output, exclude, pct, headers):
    excludedLines = [line.strip() for line in exclude]
    print("Num excluded: " + str(len(excludedLines)))

    # Get which lines haven't been used
    print("Checking for unused lines...")
    unused = []
    for line in input:
        if line.strip() not in excludedLines:
            unused.append(line)
    print("Num unused: " + str(len(unused)))

    # Adjust percent (to account for smaller pool)
    totalLines = len(unused) + len(excludedLines)
    adjustedPercent = (float(pct)*totalLines)/len(unused)/100
    print("Adjusted %: "+str(adjustedPercent))

    # Sample
    random_sample = random_sampling.doSampling(adjustedPercent, unused)
    print("Num sampled: " + str(len(random_sample)))

    # Write
    random_sampling.writeFile(headers, random_sample, output)


def main():
    if len(sys.argv) < 5: #if not enough arguments
        print ("Please specify a file to read, a file to write, a file to exclude, and the percent (e.g. 15) to get")
    else:
        headers = "URL,Label,X,Y,W,H\n"
        with open(sys.argv[1], "rb") as inFile, open(sys.argv[2], "wb") as outFile, open(sys.argv[3], "rb") as exclude:
            print("In: "+ inFile.name)
            print("Out: "+outFile.name)
            print("Exclude: "+exclude.name)
            increaseSample(inFile, outFile, exclude, sys.argv[4], headers)


if __name__ == "__main__":
    main()