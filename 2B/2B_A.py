def func():
    max_elem = -1
    max_cnt = 0
    n = -1
    while n != 0:
        n = int(input())
        if n > max_elem:
            max_elem, max_cnt = n, 0
        if n == max_elem:
            max_cnt += 1
    return max_cnt

def main():
     print(func())

if __name__ == '__main__':
    main()