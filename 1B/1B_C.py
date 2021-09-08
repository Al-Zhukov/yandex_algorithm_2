def func(x, y, z):
    return 0 if (x <= 12) and (y <= 12) and x!=y else 1

def main():
    x, y, z = map(int, input().split())
    print(func(x, y, z))

def test():
    assert func(1, 2, 2003) == 0
    assert func(2, 29, 2008) == 1
    assert func(2, 2, 2008) == 1

if __name__ == '__main__':
    main()
