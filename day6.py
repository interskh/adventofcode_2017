def redistribute(arr):
    max_ = max(arr)
    for i, x in enumerate(arr):
        if x == max_:
            break
    remain = arr[i]
    arr[i] = 0
    while remain:
        i = (i+1) % len(arr)
        arr[i] += 1
        remain -= 1


def hash(arr):
    return ",".join(str(x) for x in arr)


def main():
    arr = [int(x) for x in open("day6.txt").read().split("\t")]
    cycle = 0
    seen = set()
    seen.add(hash(arr))

    while True:
        redistribute(arr)
        cycle += 1
        if hash(arr) in seen:
            return cycle
        else:
            seen.add(hash(arr))


def main2():
    arr = [int(x) for x in open("day6.txt").read().split("\t")]
    cycle = 0
    seen = {}
    seen[hash(arr)] = cycle

    while True:
        redistribute(arr)
        cycle += 1
        if hash(arr) in seen:
            return cycle - seen[hash(arr)]
        else:
            seen[hash(arr)] = cycle

if __name__ == '__main__':
    print(main())
    print(main2())
