# input:
#   6

#   1 3
#   2 3
#   3 6
#   5 6
#   5 7
#   4 5
#   4 8
#   8 9
#   11 8
#   10 1
# Example output
#   10


import math

data_set = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
            (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)

# {3: {1, 2}, 6: {3, 5}, 7: {5}, 5: {4}, 8: {11, 4}, 9: {8}, 1: {10}}


def earliest_ancestor(data, person):
    relationship_list = {}

    # creates graph representaion of Child --> Parents
    for parent_child in data:
        if parent_child[1] not in relationship_list:
            relationship_list[parent_child[1]] = set()
            relationship_list[parent_child[1]].add(parent_child[0])
        else:
            relationship_list[parent_child[1]].add(parent_child[0])
    print(relationship_list)

    # if after creating child --> parent list, if target person
    #  is not in the dict, return -1, there is no data on that persons
    # parents
    if person not in relationship_list:
        return -1

    # traverse adjacency list using dfs
    visited = set()
    stack = Stack()

    stack.push([person])

    longest_path = [person]

    while stack.size() > 0:
        print(stack.stack)

        path = stack.pop()
        vertex = path[-1]
        print('vertex', vertex)
        # print('stack looped', current)

        if vertex not in visited:
            visited.add(vertex)

            if vertex not in relationship_list:
                if len(longest_path) == len(path) and longest_path[-1] > vertex:
                    print('new because vertex less than last item', path)
                    longest_path = path
                elif len(path) > len(longest_path):
                    print('new because longest', path)
                    longest_path = path

                continue

            for parent in relationship_list[vertex]:
                copy_path = list(path)
                copy_path.append(parent)
                stack.push(copy_path)
    return longest_path[-1]


print(earliest_ancestor(data_set, 6))
