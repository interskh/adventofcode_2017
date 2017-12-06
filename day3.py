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

if __name__ == '__main__':
    print(main(1))
    print(main(12))
    print(main(23))
    print(main(1024))
    print(main(361527))
