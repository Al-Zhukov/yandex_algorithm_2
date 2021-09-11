def func(array):
    counters = {}
    for value in array:
        if value in counters:
            counters[value] += 1
        else:
            counters[value] = 1

    answer = []
    for value in array:
        if counters[value] == 1:
            answer.append(value)
    return answer

def main():
    a = list(map(int, input().split()))
    print(*func(a))

def test():
    assert func([1, 2, 2, 3, 3, 3]) == [1]
    assert func([4, 3, 5, 2, 5, 1, 3, 5]) == [4, 2, 1]

if __name__ == '__main__':
    main()