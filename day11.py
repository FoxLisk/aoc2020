# this is a boring game-of-life alike, but i guess i'll go ahead and do it
from itertools import product


def get_floorplan():
    with open('day11_input.txt') as f:
        return [l.strip() for l in f.readlines() if l.strip()]


class FloorPlan(object):
    class Cell(object):
        ALIVE = '#'
        DEAD = 'L'
        EMPTY = '.'

        def __init__(self, l):
            if l == self.ALIVE:
                self.state = self.ALIVE
            elif l == self.DEAD:
                self.state = self.DEAD
            elif l == self.EMPTY:
                self.state = self.EMPTY

        def __repr__(self):
            return self.state

        def is_empty(self):
            return self.state == self.EMPTY

        def is_alive(self):
            return self.state == self.ALIVE

        def is_dead(self):
            return self.state == self.DEAD

        def live(self):
            if self.state == self.EMPTY:
                raise ValueError()
            self.state = self.ALIVE

        def die(self):
            if self.state == self.EMPTY:
                raise ValueError()
            self.state = self.DEAD

    def __init__(self, floorplan):
        self._raw = floorplan
        self.height = len(floorplan)
        self.width = len(floorplan[0])
        self.state = [
            [self.Cell(l) for l in row]
            for row in floorplan
        ]
        self.neighbors = [
            [0 for _ in row]
            for row in floorplan
        ]
        self._steps = 0

    def neighbor_indices(self, x, y):
        xs = []
        ys = []
        if x == 0:
            xs = [x, x + 1]
        elif x == self.width - 1:
            xs = [x - 1, x]
        else:
            xs = [x - 1, x, x + 1]

        if y == 0:
            ys = [y, y + 1]
        elif y == self.height - 1:
            ys = [y - 1, y]
        else:
            ys = [y - 1, y, y + 1]
        return [(_x, _y) for (_x, _y) in product(xs, ys) if not (x == _x and y == _y)]

    def step(self):
        new_neighbors = [
            row[:]
            for row in self.neighbors
        ]
        changed = False
        for y in range(self.height):
            for x in range(self.width):
                cell = self.state[y][x]
                if cell.is_empty():
                    continue
                if self.neighbors[y][x] == 0:
                    if cell.is_dead():
                        changed = True
                        for ix, iy in self.neighbor_indices(x, y):
                            new_neighbors[iy][ix] += 1
                    cell.live()
                if self.neighbors[y][x] >= 4:
                    if cell.is_alive():
                        changed = True
                        for ix, iy in self.neighbor_indices(x, y):
                            new_neighbors[iy][ix] -= 1
                    cell.die()
        self.neighbors = new_neighbors
        self._steps += 1
        return changed

    def sim(self):
        while True:
            changed = self.step()
            if not changed:
                return self._steps

    def num_alive(self):
        return str(self).count(self.Cell.ALIVE)

    def __str__(self):
        return '\n'.join(
            ''.join(c.state for c in row)
            for row in self.state
        )


if __name__ == '__main__':
    _f = get_floorplan()
    f = FloorPlan(_f)

    steps = f.sim()
    print(f)
    print(steps)
    print(f.num_alive())