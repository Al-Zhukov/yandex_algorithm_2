def check_parental(parents_dict, child, parent):
    while child in parents_dict:
        if parents_dict[child] == parent:
            return True
        else:
            child = parents_dict[child]
    return False

def main():
    parents_dict = dict()
    with open('input.txt') as inf:
        s = int(inf.readline().strip())
        for i in range(s-1):
            child, parent = inf.readline().strip().split()
            parents_dict[child] = parent
        for line in inf:
            first, second = line.strip().split()
            if check_parental(parents_dict, first, second): # lets check if second is parent of first
                print(2, end=' ')
            elif check_parental(parents_dict, second, first): # lets check if first is parent of second
                print(1, end=' ')
            else:
                print(0, end=' ')

if __name__ == '__main__':
    main()