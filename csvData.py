#Reads reviews list and creates a list for every review in each site (NO. OF SITES MUST MATCH "numOfSites" INTEGER)
def getReviews(reviewList: list, numOfSites: int):
    currentsite_revs = []
    startindex = 0
    temp_list = []
    currentsite = reviewList[0][0]

    for j in range(0,numOfSites):
        for i in range(startindex,len(reviewList)):
            if reviewList[i][0] == currentsite:
                temp_list.append(reviewList[i][1])
            else:
                currentsite = reviewList[i][0]
                startindex=i
                break
        currentsite_revs.append(temp_list)
        temp_list = []

    return currentsite_revs

#Reads reviews list and appends each site
def getSites(reviewList: list):
    sites = []
    startindex = 0
    currentsite = ""

    for i in range(startindex,len(reviewList)):
        if reviewList[i][0] != currentsite:
            sites.append(reviewList[i][0])
            currentsite = reviewList[i][0]
        else:
            startindex=i
            continue

    return sites