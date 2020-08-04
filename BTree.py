
from itertools import islice


class BTree(object):

    class Node(object):

        def __init__(self, order, id):
            self.keys = []
            self.children = []
            self.leaf = True
            self.order = order
            self.id = id

        def split(self, parent, payload, newNodeID):
            new_node = self.__class__(self.order, newNodeID)

            mid_point = self.size // 2
            split_value = self.keys[mid_point]
            parent.add_key(split_value)

            # Add keys and children to appropriate nodes
            new_node.children = self.children[mid_point + 1:]
            self.children = self.children[:mid_point + 1]
            new_node.keys = self.keys[mid_point + 1:]
            self.keys = self.keys[:mid_point]

            # If the new_node has children, set it as internal node
            if len(new_node.children) > 0:
                new_node.leaf = False

            parent.children = parent.add_child(new_node)
            if payload < split_value:
                return self
            else:
                return new_node

        @property
        def _is_full(self):
            return self.size == self.order

        @property
        def size(self):
            return len(self.keys)

        def add_key(self, value):
            self.keys.append(value)
            self.keys.sort()

        def add_child(self, new_node):
            i = len(self.children) - 1
            while i >= 0 and self.children[i].keys[0] > new_node.keys[0]:
                i -= 1
            return self.children[:i + 1] + [new_node] + self.children[i + 1:]

        def addToDict(self, dict):
            nodeString = ""
            if self.keys:
                for key in self.keys[:-1]:
                    nodeString += str(key) + ","
                nodeString += str(self.keys[-1])
            nodeString += ";"
            if self.children:
                for child in self.children[:-1]:
                    nodeString += str(child.id) + ","
                nodeString += str(self.children[-1].id)
            nodeString += ";"
            nodeString += str(self.leaf)
            nodeString += "\n"

            dict[self.id] = nodeString

            for child in self.children:
                dict.update(child.addToDict(dict))

            return dict

    def __init__(self, order):

        self.order = order
        if self.order <= 1:
            raise ValueError("B-Tree must have a degree of 2 or more.")
        self.nodes = 1
        self.root = self.Node(order, self.nodes)

    def insert(self, payload):
        node = self.root
        if node._is_full:
            self.nodes += 1
            new_root = self.Node(self.order, self.nodes)
            new_root.children.append(self.root)
            new_root.leaf = False
            self.nodes += 1
            node = node.split(new_root, payload, self.nodes)
            self.root = new_root

        while not node.leaf:
            i = node.size - 1
            while i > 0 and payload < node.keys[i]:
                i -= 1
            if payload > node.keys[i]:
                i += 1

            next = node.children[i]
            if next._is_full:
                self.nodes += 1
                node = next.split(node, payload, self.nodes)
            else:
                node = next
        node.add_key(payload)

    def write(self, fileName):
        rootID = self.root.id
        nodes = dict()

        self.root.addToDict(nodes)
        sortedNodes = dict()
        for i in sorted(nodes):
            sortedNodes[i] = nodes[i]

        file = open(fileName, "w")
        file.write(str(rootID) + "\n")
        for i in sortedNodes:
            file.write(sortedNodes[i])
        file.close()


def readNode(file, nodeID):
    file.seek(0)
    for line in islice(file, nodeID):
        pass
    node = file.readline()
    node = node[:-1]
    node = node.split(";")

    keys = node[0]
    if keys != "":
        keys = keys.split(",")
        keys = [int(key) for key in keys]
    else:
        keys = []

    children = node[1]
    if children != "":
        children = children.split(",")
        children = [int(child) for child in children]
    else:
        children = []

    leaf = (node[2] == "True")
    return keys, children, leaf


def searchNode(num, file, nodeID, IOCount):
    keys, children, leaf = readNode(file, nodeID)
    if num in keys:
        return True, IOCount
    elif leaf:
        return False, IOCount
    else:
        i = 0
        while i < keys.__len__() and num > keys[i]:
            i += 1
        IOCount += 1
        return searchNode(num, file, children[i], IOCount)


def searchBTree(num, fileName):
    file = open(fileName, "r")
    rootID = int(file.readline())
    IOCount = 1
    return searchNode(num, file, rootID, IOCount)
