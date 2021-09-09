def func(string):
    counter = 0
    for pos in range(len(string) // 2):
        if string[pos] != string[-pos-1]:
            counter +=1
    return counter

def main():
    print(func(input()))

def test():
    assert func('a') == 0
    assert func('ab') == 1
    assert func('cognitive') == 4

if __name__ == '__main__':
    main()