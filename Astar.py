import math

#Takes 2 dictionaries: One of (vertex -> list of vertices), and one (vertex -> (x,y)) coordinate
#initial/final vertex
#mode is to toggle step by step and minimum distance/#cities
#no visit list contains all vertices to not visit specified by user
#g = total path length from given vertex to start node
#h = straight line distance from given vertex to end node
#f = g + h
def Astar(G, D, I, F, mode, noVisitList):
    pathMap = {} #map to track order of visited nodes
    open = {} #vertices still being considered are here map of:(Vertex -> f)
    closed = noVisitList #list of vertices that no longer need to be considered

    if mode[1] == False: open[I] = distance(I, F, D) #add initial node to open (I -> f)
    else: open[I] = 0 #for minimum cities mode, don't count starting vertex

    while open:
        current = minValue(open) #set current vertex to the key with the lowest estimated distance
        if(current == F): #if current is final vertex, return path
            #return open[current]
            return pathMap
        closed.append(current) #add to closed list

        if mode[0] == True: print("City selected: " + current + "\nPossible cities to where to travel: ", sep='')
        for neighbor in G[current]:
            if neighbor in closed:
                continue
            if mode[0] == True: print(neighbor + " ", end='')

            if mode[1] == False: #minimum distance
                #calculate g, h, f for neighbor
                #the subtraction in calculating g is undoing the straight line distance to get the path length only
                g = distance(neighbor, current, D) + open[current] - distance(current, F, D)
                h = distance(neighbor, F, D)
                f = g + h
            else: #minimum # of cities
                g = open[current]
                h = 1
                f = g + h
            if neighbor in open: #if this vertex is already being considered for a lower estimate, do not add it
                if open[neighbor] <= f:
                    continue
            else: 
                open[neighbor] = f #update the open map with a new lowest estimate for this neighbor
                pathMap[neighbor] = current #and point the neighbor to where it came from

        if mode[0] == True:
            print("\nCities at the end of possible paths: ", end='')
            printMap(open)
            print("\n*******************************************")
        
        open.pop(current) #remove current vertex from open
    
    return False #did not find a path



#helper functions

def minValue(map): #helper function to return the key for lowest value x (key->x)
    return min(map, key = map.get)


def distance(A, B, map): #finds distance between 2 vertices given a map of vertex to x and y coordinate
    x1 = float(map[A][0])
    x2 = float(map[B][0])
    y1 = float(map[A][1])
    y2 = float(map[B][1])
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def printMap(map):
    for item in map:
        print(item, "(", "{:.1f}".format(map[item]), ") ", sep='',end='')