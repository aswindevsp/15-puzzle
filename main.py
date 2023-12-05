import random
import time

import Astar
import Grid
from GUI import gui


def get_action(a: list, b: list) -> int:
    offset = b.index(0) - a.index(0)
    if offset == 1:
        return Grid.LEFT
    elif offset == -1:
        return Grid.RIGHT
    elif offset == 4:
        return Grid.UP
    elif offset == -4:
        return Grid.DOWN
    else:
        return 0


def get_methods(sequence: list) -> list:
    methods = []
    for i, v in enumerate(sequence):
        if i == len(sequence) - 1:
            break
        methods.append(get_action(v.nums, sequence[i + 1].nums))
    return methods


if __name__ == "__main__":
    # default state
    init = [5, 1, 2, 3, 9, 6, 11, 4, 7, 8, 0, 12, 13, 14, 15, 10]
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,15, 0]

    # uncommit this line to increase difficulty
    # random.shuffle(init)
    start = Grid.Grid(init)

    # if solvable then Astar
    while not start.is_solvable():
        random.shuffle(init)
        start = Grid.Grid(init)
    else:
        print(init)
        start_time = time.process_time()
        paths = Astar.a_star(start, goal)
        end_time = time.process_time()
        elapsed_time = round(end_time - start_time, 4)
        if paths:
            gui(get_methods(paths), init, elapsed_time)
            # print result to console
            print("Used " + str(elapsed_time) + " seconds")
            print("moved " + str(len(paths)) + " steps")
