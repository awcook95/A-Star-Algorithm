import math

def dfs(G, I, F):
    pathMap = {} #map to track order of visited nodes

    visited = {} #map of vertex to bool set to false
    for vertex in G:
        visited[vertex] = False

    stack = [] #stack tracks traversal order of vertices for the dfs
    stack.append(I) #push initial vertex

    while stack:
        current = stack.pop()
        if current == F: return pathMap #once final vertex  is found return the path

        if(visited[current]): continue #if node is already visited skip rest of loop
        visited[current] = True #set current node to visited

        for neighbor in G[current]: #for all vertices adjacent to current vertex
            if not visited[neighbor] : 
                stack.append(neighbor)
                pathMap[neighbor] = current #update the current path from the starting point

    return False #final vertex was not found

def distance(A, B, map): #finds distance between 2 vertices given a map of vertex to x and y coordinate
    x1 = float(map[A][0])
    x2 = float(map[B][0])
    y1 = float(map[A][1])
    y2 = float(map[B][1])
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)
    

adjList = {} #dictionary to act as adjacency list

with open("connections.txt", 'r') as f:
    for line in f:
        if 'END' in line:
          break

        line = line.strip('\n') #remove newline
        li = list(line.split(" ")) #convert each line of the file to a list
        adjList[li[0]] = sorted(li[2:], reverse = True) #map the vertex to its adjacent vertices

location = {} #dictionary to hold the coordinates of each vertex

with open("locations.txt", 'r') as f:
    for line in f:
        if 'END' in line:
          break

        line = line.strip('\n') #remove newline
        li = list(line.split(" ")) #convert each line of the file to a list
        location[li[0]] = li[1:] #map the vertex to its x and y coordinate


I = input("Enter the initial vertex\n")
F = input("Enter the final vertex\n")

if I not in adjList or F not in adjList:
    exit("One of the vertices you entered is not in the graph")

print("The initial vertex is: " + I + " and the final vertex is: " + F)

pathMap = dfs(adjList, I, F)

if pathMap != False: #if dfs succeeded
    curr = F #start at the target node
    output = [] #the path will be backwards so store in a list first
    while (curr != I):
        output.append(curr)
        curr = pathMap[curr] #and use the path map to trace back the steps taken
    output.append(I) #add the starting point separately
else: exit("A path to the final vertex was not found")

#print formatted output
print("The path from", I, "to", F, "is:")
output = output[::-1]
total = 0
for i in range(0, len(output)-1):
    v1 = output[i]
    v2 = output[i+1]
    length = distance(v1,v2,location)
    total += length
    print(v1, "to", v2, "length", "%.1f"%length)
print("Total path length","%.1f"%total)