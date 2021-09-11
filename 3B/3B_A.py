def func(set1, set2):
    return len(set1.intersection(set2))

def main():

    s1 = set(map(int, input().split()))
    s2 = set(map(int, input().split()))
    print(func(s1, s2))

def test():
    assert func({1, 3, 2}, {4, 3, 2}) == 2
    assert func({1, 2, 6, 4, 5, 7}, {10, 2, 3, 4, 8}) == 2
    assert func({1, 7, 3, 8, 10, 2, 5}, {6, 5, 2, 8, 4, 3, 7}) == 5

if __name__ == '__main__':
    main()