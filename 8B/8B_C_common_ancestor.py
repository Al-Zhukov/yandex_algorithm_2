def common_ancestor(parents_dict, first, second):
    first_ancestors = set()
    while first in parents_dict:
        first_ancestors.add(first)
        first = parents_dict[first]
    first_ancestors.add(first)

    while second not in first_ancestors:
        second = parents_dict[second]
    return second

def main():
    parents_dict = dict()
    with open('input.txt') as inf:
        s = int(inf.readline().strip())
        for i in range(s-1):
            child, parent = inf.readline().strip().split()
            parents_dict[child] = parent
        for line in inf:
            first, second = line.strip().split()
            print(common_ancestor(parents_dict, first, second))

if __name__ == '__main__':
    main()