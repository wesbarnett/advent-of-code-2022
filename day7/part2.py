from aoc import get_input, submit


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
    year, day, level = 2022, 7, 2
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

    def traverse(node):
        size = 0
        for d in node.dirs:
            size += traverse(d)

        for f in node.files:
            size += f.size

        return size

    size = traverse(node)

    total_disk_space = 70000000
    unused_space = total_disk_space - size

    needed_space = 30000000 - unused_space

    def get_min_dir_size(node, min_dir_size, needed_space):
        size = 0
        for d in node.dirs:
            s, mds = get_min_dir_size(d, min_dir_size, needed_space)
            size += s
            min_dir_size = min(mds, min_dir_size)

        for f in node.files:
            size += f.size

        if size >= needed_space:
            min_dir_size = min(size, min_dir_size)

        return size, min_dir_size

    size, min_dir_size = get_min_dir_size(node, float("inf"), needed_space)
    print(min_dir_size)

    submit(min_dir_size, year, day, level)
