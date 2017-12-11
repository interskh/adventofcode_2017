def main():
    ptr = 0
    step = 0
    arr = [int(x) for x in open("day5.txt").readlines()]
    while ptr < len(arr):
        arr[ptr] += 1
        ptr += arr[ptr] - 1
        step += 1
    print(step)


def main2():
    ptr = 0
    step = 0
    arr = [int(x) for x in open("day5.txt").readlines()]
    while ptr < len(arr):
        old = arr[ptr]
        if old >= 3:
            arr[ptr] -= 1
        else:
            arr[ptr] += 1
        ptr += old
        step += 1
    print(step)

if __name__ == '__main__':
    main()
    main2()
