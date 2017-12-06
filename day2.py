def main():
    ret = 0
    with open("day2.txt") as ifp:
        for row in ifp:
            line = [int(x) for x in row.split("\t")]
            ret += max(line) - min(line)
    print(ret)


def main2():
    ret = 0
    with open("day2.txt") as ifp:
        for row in ifp:
            line = [int(x) for x in row.split("\t")]
            found = False
            for i, x in enumerate(line):
                for j, y in enumerate(line):
                    if i != j and x % y == 0:
                        ret += x//y
                        found = True
                        break
                if found:
                    break
    print(ret)

if __name__ == '__main__':
    main()
    main2()
