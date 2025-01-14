def preorder_iter(tree, i=0):
    if i < len(tree):
        res = [tree[i]]
        left = 2 * i + 1
        right = left + 1
        if left < len(tree) and tree[left] is not None:
            res += preorder(tree, left)
        if right < len(tree) and tree[right] is not None:
            res += preorder(tree, right)
        return res


def inorder_iter(tree, i=0):
    if i < len(tree):
        res = []
        left = 2 * i + 1
        right = left + 1
        if left < len(tree) and tree[left] is not None:
            res += inorder(tree, left)
        res += [tree[i]]
        if right < len(tree) and tree[right] is not None:
            res += inorder(tree, right)
        return res


def postorder_iter(tree, i=0):
    if i < len(tree):
        res = []
        left = 2 * i + 1
        right = left + 1
        if left < len(tree) and tree[left] is not None:
            res += postorder(tree, left)
        if right < len(tree) and tree[right] is not None:
            res += postorder(tree, right)
        res += [tree[i]]
        return res


def preorder_stack(tree):
    if not tree:
        return []
    res, stack = [], [0]

    while stack:
        index = stack.pop()
        res.append(tree[index])
        index = 2 * index + 2
        if index < len(tree) and tree[index] is not None:
            stack.append(index)
        index -= 1
        if index < len(tree) and tree[index] is not None:
            stack.append(index)
    return res


def inorder_stack(tree):
    if not tree:
        return []
    index = 0
    res, stack = [], []

    while True:
        if index < len(tree) and tree[index] is not None:
            stack.append(index)
            index = 2 * index + 1
        elif stack:
            index = stack.pop()
            res.append(tree[index])
            index = 2 * index + 2
        else:
            break
    return res


def postorder_stack(tree):
    if not tree:
        return []
    res, stack = [], [0]
    visit_order = []

    while stack:
        index = stack.pop()
        visit_order.append(index)
        index = 2 * index + 1
        if index < len(tree) and tree[index] is not None:
            stack.append(index)
        index = index + 1
        if index < len(tree) and tree[index] is not None:
            stack.append(index)

    while visit_order:
        index = visit_order.pop()
        res.append(tree[index])
    return res


def preorder(tree, index):
    if index >= len(tree) or tree[index] is None:
        return []
    return [tree[index]] + preorder(tree, 2 * index + 1) + preorder(tree, 2 * index + 2)


def inorder(tree, index):
    if index >= len(tree) or tree[index] is None:
        return []
    return inorder(tree, 2 * index + 1) + [tree[index]] + inorder(tree, 2 * index + 2)


def postorder(tree, index):
    if index >= len(tree) or tree[index] is None:
        return []
    return (
        postorder(tree, 2 * index + 1) + postorder(tree, 2 * index + 2) + [tree[index]]
    )
