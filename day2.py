def main():
    ret = 0
    with open("day2.txt") as ifp:
        for row in ifp:
            line = [int(x) for x in row.split("\t")]
            ret += max(line) - min(line)
    print(ret)

if __name__ == '__main__':
    main()
