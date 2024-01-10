class Node:
    def __init__(self, state, parent=None, cost_from_start=0):
        self.state = state
        self.parent = parent
        self.cost_from_start = cost_from_start

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(self.state)


def successors(node):
    graph = {
        "Start": [("CityA", 5), ("CityB", 10)],
        "CityA": [("CityC", 8)],
        "CityB": [("CityD", 6), ("CityE", 9)],
        "CityC": [("CityF", 4)],
        "CityD": [("CityE", 7), ("Goal", 10)],
        "CityE": [("CityF", 3), ("Goal", 5)],
        "CityF": [("Goal", 2)],
        "Goal": [],
    }

    return [
        (Node(successor, node, node.cost_from_start + cost), cost)
        for successor, cost in graph.get(node.state, [])
    ]


def heuristic(node):
    heuristic_values = {
        "Start": 15,
        "CityA": 10,
        "CityB": 12,
        "CityC": 6,
        "CityD": 8,
        "CityE": 3,
        "CityF": 1,
        "Goal": 0,  # Update this to a non-zero value, e.g., 0
    }

    return heuristic_values.get(node.state, 0)


def goal_test(node):
    return node.state == "Goal"


def best_first_search(start_node, goal_test, successors, heuristic):
    open_set = {start_node}
    closed_set = set()

    while open_set:
        current_node = min(
            open_set, key=lambda node: node.cost_from_start + heuristic(node)
        )
        open_set.remove(current_node)

        print("Working on Node:", current_node.state)
        print("Total Cost:", current_node.cost_from_start)
        print("Working Path:", reconstruct_path(current_node))

        if goal_test(current_node):
            final_path = reconstruct_path(current_node)
            print("Final Path:", final_path)
            print("Total Cost:", current_node.cost_from_start)
            return final_path

        closed_set.add(current_node)

        for successor, cost in successors(current_node):
            if successor not in open_set and successor not in closed_set:
                open_set.add(successor)

    print("Path not found.")
    return None


def reconstruct_path(node):
    path = []
    while node:
        path.insert(0, node.state)
        node = node.parent
    return path


# Example
start_node = Node("Start")
result = best_first_search(start_node, goal_test, successors, heuristic)

if result:
    print("Path found:", result)
else:
    print("Path not found.")
