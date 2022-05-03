reviews = [["discord","suck"],["discord","ew"], ["discord","poop"], ["a","Yes!"], ["a", 'no!'], ['b','frick']]

#Reads reviews list and creates a list for every review in each site (NO. OF SITES MUST MATCH "howmanywebsites" INTEGER)
currentsite_revs = []
startindex = 0
howmanywebsites = 3
temp_list = []
currentsite = reviews[0][0]

for j in range(0,howmanywebsites):
    for i in range(startindex,len(reviews)):
        if reviews[i][0] == currentsite:
            temp_list.append(reviews[i][1])
        else:
            currentsite = reviews[i][0]
            startindex=i
            break
    currentsite_revs.append(temp_list)
    temp_list = []

print(currentsite_revs)

#Reads reviews list and appends each site
sites = []
startindex = 0
howmanywebsites = 3
currentsite = ""

for i in range(startindex,len(reviews)):
    if reviews[i][0] != currentsite:
        sites.append(reviews[i][0])
        currentsite = reviews[i][0]
    else:
        startindex=i
        continue
    
    temp_list = []

print(sites)