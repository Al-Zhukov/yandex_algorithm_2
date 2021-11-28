class beads_tree():
    def __init__(self, root, level=0, parent=None):
        self.root = root
        self.parent = parent
        self.children = []
        self.level = level

    def construct_tree(self, beads):
        for child in self.children:
            child.add_children(beads[child.root])
        for child in self.children:
            child.construct_tree(beads)

    def add_children(self, connections):
        for connection in connections:
            if connection != self.parent:
                self.children.append(beads_tree(connection, self.level + 1, self.root))

    def print_tree(self):
        print('.' * self.level, self.root, ' ->', *[val.root for val in self.children])
        for child in self.children:
            child.print_tree()

    def find_max_chain(self):
        max_depth_val = 1
        max_depth_elem = self.root
        for child in self.children:
            val, elem = child.find_max_chain()
            val += 1
            if val > max_depth_val:
                max_depth_val, max_depth_elem = val, elem
        return (max_depth_val, max_depth_elem)

def max_depth(beads, root):
    tree = beads_tree(root)
    tree.add_children(beads[root])
    tree.construct_tree(beads)
    _, new_root = tree.find_max_chain()

    new_tree = beads_tree(new_root)
    new_tree.add_children(beads[new_root])
    new_tree.construct_tree(beads)
    return new_tree.find_max_chain()[0]


def main():
    import sys
    sys.setrecursionlimit(2600) # до 2500 бусинок
    with open('input.txt') as inf:
        N = int(inf.readline().strip())
        beads = dict()
        for line in inf:
            first, second = map(int, line.strip().split())
            if first not in beads:
                beads[first] = [second]
            else:
                beads[first].append(second)
            if second not in beads:
                beads[second] = [first]
            else:
                beads[second].append(first)

    print(max_depth(beads, second))

if __name__ == '__main__':
    main()