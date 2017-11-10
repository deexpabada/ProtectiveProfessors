#Takes in a list of edges as the input and creates a dictionary of edges
#because the draw function of networkx needs to take edges in integer form.
#Creates a dictionary with edges as keys and integers as values. Each edge has a unique integer value.
#Returns a dictionary of edges.
def makeDict(edges):
  dict = {}
  index = 0
  for edge in edges:
      dict[edge] = index
      index += 1
  return dict

# Takes in a note input with a unique key attached to it,
# deletes the key of the node and returns the node without the key.
def cutKey(knode):
    count = 0
    for char in knode:
        if char == '|':
            node = knode[count:]
            break
        if char.isalpha():
            node = knode[count:]
            break
        count +=1
    return node
