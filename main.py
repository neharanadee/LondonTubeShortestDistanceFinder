from tubemap import tubemap
from queue import Queue

#Cant use Djixtra's or A* algorithm because we do not have any indication of the weights

def findPath(firstStation, secondStation, allPaths): 
    #using BFS
    q = Queue() 
    q.put([firstStation])
    seen = set()
    while not q.empty(): 
        stations = q.get() 
        # taking the last element of the list because that is the recently added one 
        currStation = stations[-1]
        if currStation not in seen: 
            try: 
                for nextStation in tubemap[currStation]: 
                    newList = stations + [nextStation]
                    if nextStation != secondStation:
                        q.put(newList)
                    else: 
                        allPaths.append(newList)
            except Exception: 
                print("This station does not exist")
                break
        seen.add(currStation)


def findAllPaths(firstStation, secondStation): 
    allPaths = [] 
    findPath(firstStation, secondStation, allPaths)
    return allPaths

def findShortestPath(firstStation, secondStation): 
    #assumes that if paths are of the same size then doesnt matter which one is returned
    paths = findAllPaths(firstStation, secondStation)
    if not paths: 
        return []
    shortest = len(paths[0])
    savedList = paths[0]
    for path in paths: 
        if len(path) < shortest: 
            shortest = len(path)
            savedList = path
    return savedList
    
print(findShortestPath("Baker Street", "Tottenham Court Road"))





