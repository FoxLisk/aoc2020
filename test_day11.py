from unittest import TestCase

from day11 import FloorPlan

class Test(TestCase):
    def setUp(self):
        self.start = [l.strip() for l in '''
    L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''.strip().splitlines() if l.strip()]
        self.floorplan = FloorPlan(self.start)

    def test_indices(self):
        f = FloorPlan(['...', '...', '...'])
        self.assertEqual(
            sorted([
                (0, 1), (1, 0), (1, 1)
            ]),
            sorted(f.neighbor_indices(0, 0))
        )
        '''
        yyn
        syn
        yyn
        '''
        self.assertEqual(
            sorted([
                (0, 0), (1, 0), (1, 1), (0, 2), (1, 2)
            ]),
            sorted(f.neighbor_indices(0, 1))
        )
        self.assertEqual(
            sorted([
                (0,0), (0, 1), (0, 2),
                (1, 0), (1, 2),
                (2, 0), (2, 1), (2, 2)
            ]), sorted(f.neighbor_indices(1, 1))
        )

    def test_floor_plan(self):
        self.assertEqual(
            '''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''

            , str(self.floorplan)
        )
        self.floorplan.step()
        self.assertEqual('''#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##''', str(self.floorplan))
        self.floorplan.step()
        self.assertEqual('''#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##''', str(self.floorplan))

    def test_sim(self):
        self.floorplan.sim()
        self.assertEqual(37, self.floorplan.num_alive())