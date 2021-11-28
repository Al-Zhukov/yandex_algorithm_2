class BinTree():
    def __init__(self, root=None, level=0):
        self.root = root
        self.level = level
        self.left = None
        self.right = None

    def add_element(self, new_element):
        if self.root is None:
            self.root = new_element
            print('DONE')
        elif self.root == new_element:
            print('ALREADY')
        elif self.root > new_element:
            if self.left is None:
                self.left = BinTree(new_element, self.level + 1)
                print('DONE')
            else:
                self.left.add_element(new_element)
        elif self.root < new_element:
            if self.right is None:
                self.right = BinTree(new_element, self.level + 1)
                print('DONE')
            else:
                self.right.add_element(new_element)

    def find_element(self, element):
        if self.root is None:
            print('NO')
        elif self.root == element:
            print('YES')
        elif self.root > element:
            if self.left is None:
                print('NO')
            else:
                self.left.find_element(element)
        elif self.root < element:
            if self.right is None:
                print('NO')
            else:
                self.right.find_element(element)

    def print_tree(self):
        if self.left is not None:
            self.left.print_tree()
        if self.root is not None:
            print('.' * self.level, self.root, sep='')
        if self.right is not None:
            self.right.print_tree()

def main():
    tree = BinTree()
    with open('input.txt') as inf:
        for line in inf:
            command, *value = line.strip().split()
            if command == 'ADD':
                tree.add_element(int(value[0]))
            elif command == 'SEARCH':
                tree.find_element(int(value[0]))
            elif command == 'PRINTTREE':
                tree.print_tree()

if __name__ == '__main__':
    main()