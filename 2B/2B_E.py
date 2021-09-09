
def func(N, a):
    return sum(a) - max(a)

def main():
    N = int(input())
    a = list(map(int, input().split()))
    print(func(N, a))

def test():
    assert func(2, [2, 1]) == 1

if __name__ == '__main__':
    main()