def main(d):
    if d == 1:
        return 0
    layer = 0
    while d > (layer*2+1)*(layer*2+1):
        layer += 1

    prev_base = layer*2 - 1
    next_base = layer*2 + 1

    corners = [prev_base*prev_base,
               prev_base*prev_base + next_base - 1,
               prev_base*prev_base + 2*(next_base - 1),
               prev_base*prev_base + 3*(next_base - 1),
               next_base*next_base]

    for x in corners:
        if d == x:
            return layer * 2

    for i in range(4):
        if d > corners[i] and d < corners[i+1]:
            return layer * 2 - min(d-corners[i], corners[i+1]-d)


def main2(d):
    curr = [1, 2, 4, 5, 10, 11, 23, 25]
    layer = 1
    while True:
        prev = curr
        curr = []
        layer += 1
        j = 0
        total = (layer*2+1)*(layer*2+1)-(layer*2-1)*(layer*2-1)
        for i in range(total):
            if i == 0:
                curr.append(prev[j] + prev[j-1])
                #print(curr, j)
            elif i + 2 == total:
                curr.append(curr[-1] + prev[j] + prev[j-1] + curr[0])
                #print(curr, j)
            elif i + 1 == total:
                curr.append(curr[-1] + prev[j] + curr[0])
                #print(curr, j)
            elif (i+2) % (layer*2) == 0:
                curr.append(curr[-1] + prev[j-1] + prev[j])
                #print(curr, j)
            elif (i+1) % (layer*2) == 0:
                curr.append(curr[-1] + prev[j])
                #print(curr, j)
            elif i % (layer*2) == 0:
                curr.append(curr[-1] + curr[-2] + prev[j] + prev[j+1])
                #print(curr, j)
                j += 1
            else:
                curr.append(curr[-1] + prev[j] + prev[j-1] + prev[j+1])
                #print(curr, j)
                j += 1
        if curr[-1] > d:
            for x in curr:
                if x > d:
                    return x


if __name__ == '__main__':
    print(main(361527))
    print(main2(361527))
