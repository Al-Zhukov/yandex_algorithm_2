def final_solution(r, i, c):

    if i == 0:
        if r != 0:
            return 3
        else:
            return c
    elif i == 1:
        return c
    elif i == 4:
        if r != 0:
            return 3
        else:
            return 4
    elif i == 6:
        return 0
    elif i == 7:
        return 1
    else:
        return i

def main():
    r = int(input())
    i = int(input())
    c = int(input())
    print(final_solution(r, i ,c))

def test():
    assert final_solution(0, 0 ,0) == 0
    assert final_solution(-1, 0, 1) == 3
    assert final_solution(42, 1, 6) == 6
    assert final_solution(44, 7, 4) == 1
    assert final_solution(1, 4, 0) == 3
    assert final_solution(-3, 2, 4) == 2

if __name__ == '__main__':
    main()


