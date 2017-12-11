def main():
    valid = 0
    with open("day4.txt") as ifp:
        for row in ifp:
            if len(set(row.split())) == len(row.split()):
                valid += 1
    print(valid)


def main2():
    def is_valid(row):
        splitted = row.split()
        return len(set("".join(sorted(x)) for x in splitted)) == len(splitted)
    valid = 0
    with open("day4.txt") as ifp:
        for row in ifp:
            if is_valid(row):
                valid += 1
    print(valid)

if __name__ == '__main__':
    main()
    main2()
