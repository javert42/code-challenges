#!/usr/bin/env python


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):

    def __init__(self):
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._add(self.root, value)

    def _add(self, node, value):
        if value < node.value:
            if node.left:
                self._add(node.left, value)
            else:
                node.left = Node(value)
        else:
            if node.right:
                self._add(node.right, value)
            else:
                node.right = Node(value)

    def print_inline(self):
        out = ""
        todo = []
        if self.root:
            todo.append(self.root)
        while todo:
            nextline = []
            for node in todo:
                out += str(node.value) + " "
                if node.left:
                    nextline.append(node.left)
                if node.right:
                    nextline.append(node.right)
            todo = nextline
            out += "\n"
        print(out)

    def invert_tree(self):
        self._invert_tree(self.root)
        return self.root

    def _invert_tree(self, node):
        if node:
            self._invert_tree(node.left)
            self._invert_tree(node.right)
            node.left, node.right = node.right, node.left

    @classmethod
    def create_bst(cls, numbers):
        bst = cls()
        for number in numbers:
            bst.add(number)
        return bst


if __name__ == "__main__":
    import sys
    if len(sys.argv) is not 2:
        sys.stderr.write("Please provide a list of numbers to create the BST.\n")
        sys.exit(-1)
    numbers = map(int, sys.argv[1].split())
    bst = BST.create_bst(numbers)
    bst.print_inline()
    bst.invert_tree()
    bst.print_inline()

