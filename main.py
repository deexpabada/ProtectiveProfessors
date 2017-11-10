import networkx as nx
import matplotlib.pyplot as plt
import rules
import DFS
import helper


#Takes in a graph input, a node input, a key input, and the number of couples
#and creates children on the input node and assigns a unique key to each child.
#Returns the modified graph.
def makeNode_gotoCC (G, knode, key, coupleNum):
    if coupleNum == 2:
        edges = ['AB', 'ab', 'Aa', 'Bb', 'A', 'B', 'a', 'b']  # 2 couple
    else:
        edges = ['Aa', 'Bb', 'Cc', 'A', 'B', 'C', 'a', 'b', 'c', 'AB', 'BC', 'AC', 'ab', 'bc', 'ac']  # 3 couple
    edgeDict = helper.makeDict(edges)
    node = helper.cutKey(knode)
    for edge in edges:
        riverIndex = node.find('|')
        OLRI = node[:riverIndex]        #People in OLRI
        CC = node[riverIndex + 1:]      #People in CC
        count = 0
        if coupleNum == 2:
            conditions = rules.rules_2couple(CC, OLRI, edge)
        else:
            conditions = rules.rules_3couple(CC, OLRI, edge)
        if conditions:
            for char in edge:           #Remove people that have crossed over to CC
                if char in OLRI:
                    count += 1
                    OLRI = OLRI.replace(char, '')
            if count == len(edge):
                newString = str(key) + OLRI + '|' + edge + CC       #Create new node
                G.add_edge(knode, newString, weight=edgeDict[edge])     #Add node to graph
    return G



#Takes in a graph input, a node input, a key input, and the number of couples
#and creates children on the input node and assigns a unique key to each child.
#Returns the modified graph.
def makeNode_gotoOLRI (G, knode, key, coupleNum):
    if coupleNum == 2:
        edges = ['AB', 'ab', 'Aa', 'Bb', 'A', 'B', 'a', 'b']  # 2 couple
    else:
        edges = ['Aa', 'Bb', 'Cc', 'A', 'B', 'C', 'a', 'b', 'c', 'AB', 'BC', 'AC', 'ab', 'bc', 'ac']  # 3 couple
    edgeDict = helper.makeDict(edges)
    node = helper.cutKey(knode)
    for edge in edges:
        riverIndex = node.find('|')
        OLRI = node[:riverIndex]  # People in OLRI
        CC = node[riverIndex + 1:]  # People in CC
        count = 0
        if coupleNum == 2:
            conditions = rules.rules_2couple(CC, OLRI, edge)
        else:
            conditions = rules.rules_3couple(CC, OLRI, edge)
        if conditions:
            for char in edge:           #Remove people that have crossed over to CC
                if char in CC:
                    count += 1
                    CC = CC.replace(char, '')
            if count == len(edge):
                newString = str(key) + OLRI + edge + '|' + CC       #Create new node
                G.add_edge(knode, newString, weight=edgeDict[edge])     #Add node
    return G


#Takes in a graph input, a unique key, the number of iterations, and the number of couples to make the full graph.
#Calls the makeNode functions to create the graphs.
#Returns the modified graph.
def makeGraph(G, key, iterNum, coupleNum):
  leafNodes = list(x for x in G.nodes_iter() if G.out_degree(x) == 0 and G.in_degree(x) == 1) #Find the leaf nodes
  toOlri = True
  for i in range(iterNum):
      for node in leafNodes:
          key += 1
          if (toOlri):
              G = makeNode_gotoOLRI(G, node, key, coupleNum)
          else:
              G = makeNode_gotoCC(G, node, key, coupleNum)
      if toOlri:
          toOlri = False
      else:
          toOlri = True
      leafNodes = list(x for x in G.nodes_iter() if G.out_degree(x) == 0 and G.in_degree(x) == 1)
  return G


#Run for two couple example
#Solution node can be found at depth 7
G2 = nx.DiGraph()       #Make graph
startNode = 'ABab|'
key = 0
G2 = makeNode_gotoCC(G2, startNode, key, 2)     #Create tree of depth one from root
depth2 = 6                            #Depth of graph
G2 = makeGraph(G2, key, depth2, 2)               #Make tree with six iterations
# nx.draw(G2, with_labels = True)             #Uncomment to draw tree
# plt.show()
reg2 = len(list(DFS.DFS_reg(G2, startNode)))        #Calculate number of nodes traversed to find solution without heuristic
print('Regular DFS traversed ', reg2, ' nodes to find the solution.')
heur2 = len(list(DFS.DFS_Heuristic(G2, startNode)))      #Calculate number of nodes traversed to find solution with heuristic
print('Heuristic DFS traversed ', heur2, ' nodes to find the solution.')

#Run for three couple example
#Solution node can be found at depth 9
G3 = nx.DiGraph()
startNode = 'ABCabc|'
key = 0
G3 = makeNode_gotoCC(G3, startNode, key, 3)     #Create tree of depth one from root
depth3 = 8                            #Depth of graph
G3 = makeGraph(G3, key, depth3, 3)               #Make tree with eight iterations
# nx.draw(G3, with_labels = True)             #Uncomment to draw tree
# plt.show()
reg3 = len(list(DFS.DFS_reg(G3, startNode)))        #Calculate number of nodes traversed to find solution without heuristic
heur3 = len(list(DFS.DFS_Heuristic(G3, startNode)))  #Calculate number of nodes traversed to find solution with heuristic
print("Regular DFS traversed ", reg3, " nodes to find the solution.")
print("Heuristic DFS traversed ",heur3," nodes to find the solution.")





