def check_brackets(input_string):
    counter = 0
    for bracket in input_string:
        if bracket == '(':
            counter += 1
        else:
            counter -= 1
        if counter < 0:
            return 'NO'
    if counter == 0:
        return 'YES'
    else:
        return 'NO'

def main():
    a = input()
    print(check_brackets(a))

def test():
    assert check_brackets('(())()') == 'YES'
    assert check_brackets('(()))()') == 'NO'
    assert check_brackets('(())(()') == 'NO'

if __name__ == '__main__':
    main()