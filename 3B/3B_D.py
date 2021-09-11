def func(ans_set, s1, s2):
    numbers_set = set(map(int, s1.split()))
    if s2 == 'YES':
        ans_set &= numbers_set
        return ans_set
    else:
        ans_set -= numbers_set
        return ans_set

def main():
    n = int(input())
    possible_answers = {i+1 for i in range(n)}
    s1 = input()
    while s1 != 'HELP':
        s2 = input()
        possible_answers = func(possible_answers, s1, s2)
        s1 = input()
    print(*sorted(possible_answers))

def test():
    assert func({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, '1 2 3 4 5', 'YES') == {1, 2, 3, 4, 5}
    assert func({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, '2 4 6 8 10', 'NO') == {1, 3, 5, 7, 9}
    assert func({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, '5 4 3 2 1', 'YES') == {1, 2, 3, 4, 5}
    assert func({2, 3, 4, 5, 6, 7, 8, 9, 10}, '1 2 3 4 5', 'YES') == {2, 3, 4, 5}

if __name__ == '__main__':
    main()