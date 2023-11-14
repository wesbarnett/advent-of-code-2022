from aoc import get_input  # , submit


class Node:
    def __init__(self, name, parent=None, size=0):
        self.name = name
        self.files = []
        self.dirs = []
        self.parent = parent
        self.size = size

    def __repr__(self):
        return f"Node(name={self.name},size={self.size})"

    def add_dir(self, dirname, parent):
        for d in self.dirs:
            if d.name == dirname:
                print("dir already added")
                return
        self.dirs.append(Node(dirname, parent))

    def add_file(self, filename, parent, size):
        for f in self.files:
            if f.name == filename:
                print("file already added")
                return
        self.files.append(Node(filename, parent, size))


if __name__ == "__main__":
    year, day, level = 2022, 7, 1
    aoc_input = get_input(year, day)
    lines = aoc_input.rstrip("\n").split("\n")

    node = Node(-1)
    for line in lines:
        if line.startswith("$ cd"):
            loc = line.split(" ")[-1]
            if loc == "..":
                node = node.parent
            else:
                # Check if node already added
                for d in node.dirs:
                    if d.name == loc:
                        node = d
                        break
                else:
                    node = Node(loc, parent=node)
        elif line.startswith("$ ls"):
            pass
        else:
            if line.startswith("dir"):
                node.add_dir(line.split(" ")[-1], parent=node)
            else:
                size, name = line.split(" ")
                node.add_file(name, parent=node, size=int(size))

    node = node.parent

    def traverse(node, total_size=0):
        size = 0
        for d in node.dirs:
            s, total_size = traverse(d, total_size)
            size += s

        for f in node.files:
            size += f.size

        if size > 100000:
            total_size += size

        return size, total_size

    size, total_size = traverse(node)

    print(total_size)

    # submit(total_size, year, day, level)
