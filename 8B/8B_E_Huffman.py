class HuffmanTree():
    def __init__(self, value='', parent=None, type=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        self.type = type

    def construct(self, code):
        if code[0] == 'D':
            if self.left is None:
                self.left = HuffmanTree(self.value + '0', self, 'left')
                if len(code) > 1:
                    self.left.construct(code[1:])
            else:
                self.right = HuffmanTree(self.value + '1', self, 'right')
                if len(code) > 1:
                    self.right.construct(code[1:])
        if code[0] == 'U':
            if self.type == 'right':
                self.parent.construct(code)
            elif self.type == 'left':
                self.parent.right = HuffmanTree(self.parent.value + '1', self.parent, 'right')
                if len(code) > 1:
                    self.parent.right.construct(code[1:])

    def calc_leaves(self):
        if self.left is None and self.right is None:
            return 1
        else:
            l = self.left.calc_leaves() if self.left is not None else 0
            r = self.right.calc_leaves() if self.right is not None else 0
        return l + r


    def print_tree(self):
        if self.left is None and self.right is None:
            print(self.value)
        if self.left is not None:
            self.left.print_tree()
        if self.right is not None:
            self.right.print_tree()

def main():
    import sys
    sys.setrecursionlimit(101000) # до 100000 символов в одном коде

    N = int(input())
    for _ in range(N):

        tree = HuffmanTree()
        tree.construct(list(input()))
        print(tree.calc_leaves())
        tree.print_tree()

if __name__ == '__main__':
    main()