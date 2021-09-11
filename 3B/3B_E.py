def func(list_of_evidence, list_of_car_numbers):
    diction_of_evidence = {}
    for car_number in list_of_car_numbers:
        car_number_set = set(car_number)
        value = 0
        for evidence in list_of_evidence:
            if len(evidence.difference(car_number_set)) == 0:
                value += 1

        if value not in diction_of_evidence:
            diction_of_evidence[value] = [car_number]
        else:
            diction_of_evidence[value].append(car_number)
    return diction_of_evidence[max(diction_of_evidence)]

def main():
    M = int(input())
    list_of_evidence = [set(input()) for _ in range(M)]

    N = int(input())
    list_of_car_numbers = [input() for _ in range(N)]

    print('\n'.join(func(list_of_evidence, list_of_car_numbers)))

def test():
    assert func([{'B', 'A', 'C'}, {'7', 'A', '3'}, {'B', 'D', 'A', 'C'}], ['A317BD', 'B137AC']) == ['B137AC']
    assert func([{'1', 'B', 'C', 'A'}, {'A', '3', '4', 'B'}], ['A143BC', 'C143AB', 'AAABC1']) == ['A143BC', 'C143AB']

if __name__ == '__main__':
    main()