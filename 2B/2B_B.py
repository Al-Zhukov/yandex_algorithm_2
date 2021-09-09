def func(array):
    max_dist = -1
    shop_positions = []
    for pos in range(len(array)):
        if array[pos] == 2:
            shop_positions.append(pos)
    for pos in range(len(array)):
        if array[pos] == 1:
            dist = min([abs(pos - shop_pos) for shop_pos in shop_positions])
            if dist > max_dist:
                max_dist = dist
    return max_dist

def main():
    print(func(list(map(int, input().split()))))

def test():
    assert func([2, 0, 1, 1, 0, 1, 0, 2, 1, 2]) == 0

if __name__ == '__main__':
    main()