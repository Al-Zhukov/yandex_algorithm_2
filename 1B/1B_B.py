def func(stations, start, finish):
    if start > finish:
        start, finish = finish, start
    way_1 = (finish - start)
    way_2 = (start + stations - finish)
    return min(way_1, way_2) - 1 # -1, т.к. нужно количество промежуточных станций, а не количество перегонов.

def main():
    N, i, j = map(int, input().split())
    print(func(N, i, j))

def test():
    assert func(100, 5, 6) == 0
    assert func(10, 2, 5) == 2
    assert func(10, 1, 9) == 1

if __name__ == '__main__':
    main()


