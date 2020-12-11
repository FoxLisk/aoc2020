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
            self.next_state = None

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
            self.next_state = self.ALIVE

        def die(self):
            if self.state == self.EMPTY:
                raise ValueError()
            self.next_state = self.DEAD

        def effect(self):
            changed = False
            if self.state == self.EMPTY:
                if self.next_state is not None:
                    raise ValueError()
            elif self.next_state is None:
                raise ValueError()
            else:
                if self.state != self.next_state:
                    changed = True
                self.state = self.next_state
                # self.next_state = None
            return changed

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

    def step_p1(self):
        new_neighbors = [
            row[:]
            for row in self.neighbors
        ]
        for y in range(self.height):
            for x in range(self.width):
                cell = self.state[y][x]
                if cell.is_empty():
                    continue
                if self.neighbors[y][x] == 0:
                    if cell.is_dead():
                        for ix, iy in self.neighbor_indices(x, y):
                            new_neighbors[iy][ix] += 1
                    cell.live()
                if self.neighbors[y][x] >= 4:
                    if cell.is_alive():
                        for ix, iy in self.neighbor_indices(x, y):
                            new_neighbors[iy][ix] -= 1
                    cell.die()
        self.neighbors = new_neighbors
        self._steps += 1
        return self.effect()

    def void(self):
        pass

    def rays(self):
        self.void()
        return [
            (-1, -1), (0, -1), (1, -1),
            (-1, 0), (1, 0),
            (-1, 1), (0, 1), (1, 1),
        ]

    def is_valid_index(self, x, y):
        return (0 <= x < self.width) and (0 <= y < self.height)

    def effect(self):
        changed = False
        for row in self.state:
            for c in row:
                changed = c.effect() or changed
        return changed

    def step(self):
        for y in range(self.height):
            for x in range(self.width):
                cell = self.state[y][x]
                if cell.is_empty():
                    continue
                visible = 0
                for dx, dy in self.rays():
                    nx, ny = x, y
                    while True:
                        nx += dx
                        ny += dy
                        if not self.is_valid_index(nx, ny):
                            break
                        if self.state[ny][nx].is_alive():
                            visible += 1
                            break
                        elif self.state[ny][nx].is_dead():
                            # seeing an empty seat counts, the fact that there might be an
                            # occupied seat in that direction is irrelevant
                            break
                if visible == 0:
                    cell.live()
                elif visible >= 5:
                    cell.die()

        self._steps += 1
        changed = self.effect()
        return changed

    def sim(self, phase=2):
        while True:
            if phase == 1:
                changed = self.step_p1()
            else:
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
