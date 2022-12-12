from typing import Generator

def read_input(infile: str) -> list[str]:
    with open(infile, 'r') as f:
        session_lines = [x.strip() for x in f.readlines()]
    return session_lines

class TreeNode:
    def __init__(self, name: str, size: int = 0) -> None:
        self.name: str = name
        self.size: int = size
        self.parent: TreeNode = self
        self.children: list[TreeNode] = list()

    def add(self, node: "TreeNode") -> None:
        self.children.append(node)
        node.parent = self

    def get_size(self) -> int:
        size = self.size
        for child in self.children:
            size += child.get_size()
        return size

    def get_child(self, name: str) -> "TreeNode":
        for child in self.children:
            if child.name == name:
                return child
        raise IndexError("TreeNode does not have child {}".format(name))

    def traverse(self) -> Generator:
        yield self
        if self.children:
            for child in self.children:
                yield from child.traverse()

def parse_tree(session_lines: list[str]) -> TreeNode:
    root: TreeNode = TreeNode("/")
    cwd: TreeNode = root
    for line in session_lines:
        if line.startswith("$ cd"):
            dst = line.split(' ')[2]
            cwd = cwd.parent if dst == ".." else cwd.get_child(dst)
        elif line.startswith("$ ls"):
            pass
        else: # file or dir
            sline = line.split(' ')
            cwd.add(TreeNode(sline[1], 0 if sline[0] == 'dir' else int(sline[0])))
    return root

def find_p1_sum(file_tree) -> int:
    rsum: int = 0
    for node in file_tree.traverse():
        if node.size == 0: # dir
            size = node.get_size()
            if size <= 100000:
                rsum += size
    return rsum

if __name__ == "__main__":
    session_lines = read_input("input.txt")
    file_tree = parse_tree(session_lines[1:])
    print(find_p1_sum(file_tree))
