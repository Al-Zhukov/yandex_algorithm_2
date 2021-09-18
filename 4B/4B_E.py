def func(n):
    from collections import Counter
    forum_list = [0] * n
    for i in range(n):
        number = int(input())
        if number == 0:
            theme, _ = input(), input() # theme and message
            forum_list[i] = theme
        else:
            _ = input() # only message
            forum_list[i] = forum_list[number - 1]
    return Counter(forum_list).most_common(1)[0][0]

def main():
    n = int(input())
    print(func(n))

if __name__ == '__main__':
    main()