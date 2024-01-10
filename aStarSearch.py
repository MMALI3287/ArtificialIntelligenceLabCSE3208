def a_star(start_node, stop_node):
    open_set = {start_node}
    closed_set = set()
    g = {start_node: 0}  # store distance from starting node
    parents = {start_node: start_node}  # parents contain an adjacency map of CLL nodes

    while len(open_set) > 0:
        n = None
        # node with the lowest f() is found
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n == stop_node or Graph_nodes[n] is None:
            pass
        else:
            for m, weight in get_neighbors(n):
                # nodes 'm' not in the first and last set are added to the first
                # n is set to its parent
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                # for each node m, compare its distance from start i.e. g(m) to the
                # from start through n node
                else:
                    if g[m] > g[n] + weight:
                        # update
                        g[m] = g[n] + weight
                        # change the parent of m to n
                        parents[m] = n
                        # if in the closed set, remove and add to open
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

            print("\nCurrent Node:", n)
            print("Current Path:", get_current_path(parents, start_node, n))
            print(
                "f({}) = {} = g({}) + v({})".format(
                    n, g[n] + heuristic(n), g[n], heuristic(n)
                )
            )

        if n is None:
            print("Path does not exist!")
            return None

        # if the current node is the stop_node
        # then we begin reconstructing the path from it to the start_node
        if n == stop_node:
            path = get_current_path(parents, start_node, n)
            print("\nPath found:", path)
            print("Total Cost:", g[stop_node])
            return path

        # remove n from the open_set, and add it to the closed_set
        # because all of its neighbors were inspected
        open_set.remove(n)
        closed_set.add(n)

    print("Path does not exist!")
    return None


# define function to return neighbor and its distance
# from the passed node
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    return None


# for simplicity we will consider heuristic distances given
# and this function returns heuristic distance for all nodes
def heuristic(n):
    h_dist = {"A": 11, "B": 6, "C": 9, "D": 14, "E": 10, "F": 3, "G": 0, "H": 4}
    return h_dist[n]


# function to get the current path from start to current node
def get_current_path(parents, start, current):
    path = [current]
    while parents[current] != start:
        current = parents[current]
        path.append(current)
    path.append(start)
    path.reverse()
    return path


# Describe your graph here
Graph_nodes = {
    "A": [("B", 7), ("C", 9), ("D", 14)],
    "B": [("A", 7), ("C", 10), ("E", 15)],
    "C": [("A", 9), ("B", 10), ("D", 11), ("F", 2)],
    "D": [("A", 14), ("C", 11), ("E", 9)],
    "E": [("B", 15), ("D", 9), ("F", 6), ("H", 5)],
    "F": [("C", 2), ("E", 6), ("G", 3)],
    "G": [("F", 3), ("H", 4)],
    "H": [("E", 5), ("G", 4)],
}

a_star("D", "G")
