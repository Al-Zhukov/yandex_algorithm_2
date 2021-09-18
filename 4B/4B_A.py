def add_to_dict(input_list):

    sum_colors_dict = {}
    for color, number in input_list:
        if color not in sum_colors_dict:
            sum_colors_dict[color] = 0
        sum_colors_dict[color] += number

    return sorted(sum_colors_dict.items(), key=lambda x: x[0])

def main():
    n = int(input())
    ad_list = [list(map(int, input().split())) for _ in range(n)]
    for string in add_to_dict(ad_list):
        print(*string)

def test():
    assert add_to_dict([[1, 5], [10, -5], [1, 10], [4, -2], [4, 3], [4, 1], [4, 0]]) == [(1, 15), (4, 2), (10, -5)]
    assert add_to_dict([[5, -10000], [-5, 100000000000], [10, 2000000000000], [-5, -300000000000], [0, 10000000000000]]) == [(-5, -200000000000), (0, 10000000000000), (5, -10000), (10, 2000000000000)]

if __name__ == '__main__':
    main()