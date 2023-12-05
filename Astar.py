from queue import PriorityQueue

from Grid import Grid

map = {}


def a_star(grid: Grid, goal: list):
    open_set = PriorityQueue()
    open_set.put(grid)
    while open_set.not_empty:
        current = open_set.get()
        current_nums = current.nums

        print(current.nums)
        # omit existed state
        if map.__contains__(str(current_nums)):
            continue
        map[str(current_nums)] = 1

        # get answer
        if current_nums == goal:
            path = []
            while current.parent:
                path.append(current)
                current = current.parent
            path.append(current)
            return path[::-1]

        # iterate all current's children
        for node in current.children():
            node.G = current.G + 1
            node.H = manhattan(node.nums)
            node.parent = current
            open_set.put(node)


def manhattan(nums: list) -> int:
    H = 0
    for value in range(1, 16):
        _x = value // 4
        _y = value % 4
        index = nums.index(value) + 1
        x = index // 4
        y = index % 4
        H += abs(_x - x) + abs(_y - y)
    return H
