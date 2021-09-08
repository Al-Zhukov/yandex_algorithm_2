def func(N, a):
    return a[N//2]

def main():
    N = int(input())
    a = list(map(int, input().split()))
    print(func(N, a))

def test():
    assert func(4, [1, 2, 3, 4]) in [2, 3]
    assert func(3, [-1, 0, 1]) == 0
    assert func(5, [1, 2, 3, 6, 10]) == 3

if __name__ == '__main__':
    main()