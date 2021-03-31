from Astar import Astar, minValue, distance

#helper functions

#program start
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

cities = input("Enter the cities you don't want to visit in a space separated list, or press enter to not skip any:")
noVisitList = cities.split(" ")

response = '\0'
mode = [False, False] #bool list for activating step by step and minimum city heuristic modes
while response != 'y' and response != 'n':
    response = input("Do you want to show the step-by-step? enter y/n")
    if response == 'y':
        mode[0] = True
    elif response == 'n':
        mode[0] = False
    else: print("Invalid response")

while response != 'd' and response != 'c':
    response = input("Do you want to use the minimum distance heuristic OR the minimum # of cities heuristic? enter d/c")
    if response == 'c':
        mode[1] = True
    elif response == 'd':
        mode[1] = False
    else: print("Invalid response")

if I not in adjList or F not in adjList:
    exit("One of the vertices you entered is not in the graph")

print("The initial vertex is: " + I + " and the final vertex is: " + F)

pathMap = Astar(adjList, location, I, F, mode, noVisitList)

if pathMap != False: #if dfs succeeded
    curr = F #start at the target node
    output = [] #the path will be backwards so store in a list first
    while (curr != I):
        output.append(curr)
        curr = pathMap[curr] #and use the path map to trace back the steps taken
    output.append(I) #add the starting point separately
else: exit("A path to the final vertex was not found")

#print formatted output
if mode[1] == False:
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

else:
    print("The path from", I, "to", F, "is:")
    output = output[::-1]
    total = 0
    for i in range(0, len(output)-1):
        v1 = output[i]
        v2 = output[i+1]
        length = 1
        total += length
        print(v1, "to", v2, "length", length)
    print("Total path length",total)
