def turtoise_and_hare(number_list: list):
    turtoise = number_list[0]
    hare = number_list[0]

    while True:
        turtoise = number_list[turtoise]
        hare = number_list[number_list[hare]]

        if turtoise == hare:
            break

    ptr1 = number_list[0]
    ptr2 = turtoise

    while ptr1 != ptr2:
        ptr1 = number_list[ptr1]
        ptr2 = number_list[ptr2]

    return ptr1


def main():
    numbers = [1, 3, 4, 5, 3, 7 ,8]

    print(turtoise_and_hare(numbers))

    exit(0)


if __name__ == '__main__':
    main()

