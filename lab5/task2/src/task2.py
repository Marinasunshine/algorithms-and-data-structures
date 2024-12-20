def find_height(parents, n):
    def height(node):
        if not children[node]:
            return 1
        return 1 + max(height(child) for child in children[node])

    children = [[] for _ in range(n)]
    root = -1
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            children[parents[i]].append(i)

    return height(root)

