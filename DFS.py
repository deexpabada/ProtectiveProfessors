import helper

def DFS_Heuristic(G, coupleNum, source=None):
    """Produce edges in a depth-first-search (DFS).
    Parameters
    ----------
    G : NetworkX graph
    source : node, optional
       Specify starting node for depth-first search and return edges in
       the component reachable from source.
    coupleNum: Number of couples in the problem
    Returns
    -------
    edges: generator
       A generator of edges in the depth-first-search.
    Notes
    -----
    Based on http://www.ics.uci.edu/~eppstein/PADS/DFS.py
    by D. Eppstein, July 2004.

    If a source is not specified then a source is chosen arbitrarily and
    repeatedly until all components in the graph are searched.
    """
    if coupleNum == 2:
        edges = ['AB', 'ab', 'Aa', 'Bb', 'A', 'B', 'a', 'b']  # 2 couple
    else:
        edges = ['Aa', 'Bb', 'Cc', 'A', 'B', 'C', 'a', 'b', 'c', 'AB', 'BC', 'AC', 'ab', 'bc', 'ac']   #3 couple
    edgeDict = helper.makeDict(edges)
    reverse_edgeDict = {v: k for k, v in edgeDict.items()}

    if source is None:
        # produce edges for all components
        nodes = G
    else:
        # produce edges for components with source
        nodes = [source]
    visited=set()
    for start in nodes:
        if start in visited:
            continue
        visited.add(start)
        # stack = [(start,iter(G[start]))]
        x = []
        #Heuristic DFS
        for child in G[start]: #If a node at depth 1 is of patterns 'Aa' or 'Bb' or 'Cc' explore first
            if coupleNum == 2:
                if reverse_edgeDict[G.get_edge_data(start, child)['weight']] == "Aa" or reverse_edgeDict[G.get_edge_data(start, child)['weight']] == "Bb":
                    x.append(child)
            else:
                if reverse_edgeDict[G.get_edge_data(start, child)['weight']] == "Aa" or reverse_edgeDict[G.get_edge_data(start, child)['weight']] == "Bb"\
                        or reverse_edgeDict[G.get_edge_data(start, child)['weight']] == "Cc":
                    x.append(child)
        stack = [(start, iter(x))]
        while stack:
            parent,children = stack[-1]
            try:
                child = next(children)
                cleanChild = helper.cutKey(child)
                if cleanChild[0] == '|':        #If solution is found stop loop
                    yield parent,child
                    break;
                if child not in visited:
                    yield parent,child
                    visited.add(child)
                    stack.append((child,iter(G[child])))
            except StopIteration:
                stack.pop()


# DFS without heuristic
def DFS_reg(G, source=None):
    if source is None:
        # produce edges for all components
        nodes = G
    else:
        # produce edges for components with source
        nodes = [source]
    visited=set()
    for start in nodes:
        if start in visited:
            continue
        visited.add(start)
        stack = [(start,iter(G[start]))]
        while stack:
            parent,children = stack[-1]
            try:
                child = next(children)
                cleanChild = helper.cutKey(child)
                if cleanChild[0] == '|':        #If solution is found break loop
                    yield parent, child
                    break;
                if child not in visited:
                    yield parent,child
                    visited.add(child)
                    stack.append((child,iter(G[child])))
            except StopIteration:
                stack.pop()


