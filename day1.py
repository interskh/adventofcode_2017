def main():
    st = open("day1.txt").read().strip()
    ret = 0
    for i, s in enumerate(st):
        if i < len(st)-1 and s == st[i+1]:
            ret += int(s)
        elif i == len(st)-1 and s == st[0]:
            ret += int(s)
    print(ret)


def main2():
    st = open("day1.txt").read().strip()
    ret = 0
    half_len = len(st)//2
    for i in range(half_len):
        if st[i] == st[i+half_len]:
            ret += int(st[i]) * 2
    print(ret)

if __name__ == '__main__':
    main()
    main2()
