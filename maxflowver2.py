from collections import defaultdict
import copy
 
# This class represents a directed graph 
# using adjacency matrix representation
class Graph:
 
    def __init__(self, graph):
        self.graph = graph  # residual graph
        self. ROW = len(graph)
        # print(self.ROW)
        # self.COL = len(gr[0])
 
    '''Returns true if there is a path from source 's' to sink 't' in
    residual graph. Also fills parent[] to store the path '''
 
    def BFS(self, s, t, parent):
 
        # Mark all the vertices as not visited
        visited = [False]*(self.ROW)
 
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True
 
         # Standard BFS Loop
        while queue:
 
            # Dequeue a vertex from queue and print it
            u = queue.pop(0)
 
            # Get all adjacent vertices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                      # If we find a connection to the sink node, 
                    # then there is no point in BFS anymore
                    # We just have to set its parent and can return true
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True
 
        # We didn't reach sink in BFS starting 
        # from source, so return false
        return False
             
     
    # Returns the maximum flow from s to t in the given graph
    def FordFulkerson(self, source, sink):
 
        # This array is filled by BFS and to store path
        parent = [-1]*(self.ROW)
 
        max_flow = 0 # There is no flow initially
 
        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent) :
 
            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while(s !=  source):
                path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]
 
            # Add path flow to overall flow
            max_flow +=  path_flow
 
            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while(v !=  source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                v = parent[v]
        
        
        return max_flow
    

def subtract_arrays(arr1, arr2):
    '''used to subtract elements between two matrices'''
    # Ensure that both arrays have the same dimensions
    if len(arr1) != len(arr2) or any(len(row1) != len(row2) for row1, row2 in zip(arr1, arr2)):
        raise ValueError("Arrays must have the same dimensions")

    result = [[element1 - element2 for element1, element2 in zip(row1, row2)] for row1, row2 in zip(arr1, arr2)]
    return result

def add_arrays(arr1, arr2):
    '''used to subtract elements between two matrices'''
    # Ensure that both arrays have the same dimensions
    if len(arr1) != len(arr2) or any(len(row1) != len(row2) for row1, row2 in zip(arr1, arr2)):
        raise ValueError("Arrays must have the same dimensions")

    result = [[element1 + element2 for element1, element2 in zip(row1, row2)] for row1, row2 in zip(arr1, arr2)]
    return result

def print_2d_list(my_2d_list):
    '''used to print a 2d list'''
    for row in my_2d_list:
        for item in row:
            print(item, end=" ")
        print()
        
def verify(flow, maxflowgraph, minflowgraph):
    '''used to verify the solution'''
    if len(flow) != len(minflowgraph) or len(flow) != len(maxflowgraph):
        raise ValueError("All lists must have the same dimensions")

    for row_to_check, row_lower, row_upper in zip(flow, minflowgraph, maxflowgraph):
        for value_to_check, lower_bound, upper_bound in zip(row_to_check, row_lower, row_upper):
            if not (lower_bound <= value_to_check <= upper_bound):
                return False

    return True
    

###EXAMPLE ONE###

#nodes = 7

# edges =   [(0, 2, 8)
#     ,(0,1,5)
#     ,(0, 3, 6)
#     ,(1, 3, 4)
#     ,(1, 4, 10)
#     ,(2, 3,4)
#     ,(2, 5, 8)
#     ,(3, 4, 6)
#     ,(3, 5, 5)
#     ,(3, 6, 4)
#     ,(4, 6, 4)
#     ,(5, 6, 6)]

#minimum = []

#source = 0; sink = 6

###EXAMPLE TWO###
nodes = 17

maxint = 10000#a really large value

edges = [(0, 1, 200)#source, destination, capacity
,(1, 2, 100)
,(1, 3, 50)
,(2, 4, 30)
,(2, 5, 70)
,(3, 6, 40)
,(3, 7, 60)
,(4, 8, 10)
,(4, 9, 20)
,(5, 10, 30)
,(5, 11, 10)
,(6, 12, 10)
,(6, 13, 30)
,(7, 14, 40)
,(7, 15, 60)
,(8,16,maxint)
,(9,16, maxint)
,(10,16,maxint)
,(11,16, maxint)
,(12,16, maxint)
,(13,16, maxint)
,(14,16, maxint)
,(15,16, maxint)]


minflow = [(0, 1, 40)#the minimum capacity of each of the edges  
,(1, 2, 20)
,(1, 3, 20)
,(2, 4, 10)
,(2, 5, 10)
,(3, 6, 10)
,(3, 7, 10)
,(4, 8, 5)
,(4, 9, 5)
,(5, 10, 5)
,(5, 11, 5)
,(6, 12, 5)
,(6, 13, 5)
,(7, 14, 5)
,(7, 15, 5)]

source = 0; sink = 16


###RUNNING THE ALGORITHM###

max_graph = [[0 for i in range(nodes)] for j in range(nodes)]
min_graph = [[0 for i in range(nodes)] for j in range(nodes)]

for edge in edges:
    max_graph[edge[0]][edge[1]]= edge[2]

for edge in minflow:
    min_graph[edge[0]][edge[1]]= edge[2]
    
graph = subtract_arrays(max_graph,min_graph)

g1 = copy.deepcopy(graph)  

g = Graph(graph)
  
print ("The maximum possible flow is %d " % (g.FordFulkerson(source, sink)+min_graph[0][1]))
print("")
print("The matrix representing the flow along each edge is")
final_flow = add_arrays(subtract_arrays(g1,graph),min_graph)
print_2d_list(final_flow)

if verify(final_flow,max_graph,min_graph):
    print("The bandwidth in each edge are consistent with the requirements")
else:
    print("The bandwidth is not consistent with the requirements")