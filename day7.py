def main():
    graph = {}
    for row in open("day7.txt").readlines():
    #for row in open("test.txt").readlines():
        arr = row.split()
        name = arr[0]
        if len(arr) > 2:
            for dep in arr[3:]:
                if dep.endswith(','):
                    graph[dep[:-1]] = name
                else:
                    graph[dep] = name
        if name not in graph:
            graph[name] = None
    print([x for x, y in graph.items() if not y])


def main2():
    graph = {}
    weights = {}
    #for row in open("day7.txt").readlines():
    for row in open("test.txt").readlines():
        arr = row.split()
        name = arr[0]
        weight = int(arr[1][1:-1])
        weights[name] = [weight]
        if len(arr) > 2:
            for dep in arr[3:]:
                if dep.endswith(','):
                    graph[dep[:-1]] = name
                else:
                    graph[dep] = name
        if name not in graph:
            graph[name] = None

if __name__ == '__main__':
    main()
    main2()
