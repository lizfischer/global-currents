import urllib, json, sys, os

if len(sys.argv) < 2:
    print('Please specify at least one list of druids as input')
    quit()

numFiles = len(sys.argv)-1
for i in range (1, numFiles+1):
    infile = open(sys.argv[i], "rb")
    fileName = sys.argv[i][sys.argv[i].find('/')+1:]

    # MAKE DIRECTORY FOR OUT FILES #
    outPath = "./output/"+fileName+"/"
    if not os.path.exists(outPath):
        os.makedirs(outPath)

    def folioFromURL (url):
        msIndex= url.find('%')+3  #find start of MS number in DocID
        pageIndex = url.find ('_')+1  #find start of folio number in DocID
        rvIndex = url.find('_', pageIndex)+1

        ms_no = url[msIndex:pageIndex-1].lstrip('0')
        page = url[pageIndex:rvIndex-1].lstrip('0')

        rv = url[rvIndex:rvIndex+1]
        if (rv != 'T'):
            page += " "+rv

        return [page, ms_no]


    ## GET DRUIDS ##
    print ("Opening File " + fileName + "... (file " + str(i) + " of " + str(numFiles) + ")")
    print ("Creating URLs...")
    druids = infile.read().splitlines()
    infile.close()

    ## PROCESS JSON ##
    c = 0
    for druid in druids:
        c += 1
        url = "https://purl.stanford.edu/"+ druid + "/iiif/manifest.json"

        #print "Getting JSON for " + druid + "..."
        response = urllib.urlopen(url)
        data = json.loads(response.read())

        numImages = len(data['sequences'][0]['canvases'])

        ## WRITE INFO TO FILE ##
        outfile = open(outPath + druid, "wb")
        print ("Writing " + druid + " to file... (" + str(c) + "/" + str(len(druids)) + ")")
        for i in range(0, numImages):
            canvas = data['sequences'][0]['canvases'][i]
            label = canvas['label'][:2]
            url = canvas['images'][0]['resource']['@id']
            type = url[-29:-27] #get TC or NC in URL
            if type == "TC" and (label == "f." or label == "p." or label == " f"):#only look at TC, and folio/page images
                height = canvas['height']
                width = canvas['width']
                folioInfo = folioFromURL(url)
                line = folioInfo[0] + "," + folioInfo[1] + "," + str(width) + "," +str(height) + "," + url + "\n"
                outfile.write(line)
        outfile.close()
