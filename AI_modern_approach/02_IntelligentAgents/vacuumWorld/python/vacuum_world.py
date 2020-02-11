import numpy as np


def main():
    world = World1D(5, 0.8)
    print(world)
    print(world.is_dirty())
    robot = Robot(world)
    sim = Simulation(world, robot)


class World1D:
    def __init__(self, n_rooms, prob_dirty):
        self.n_rooms = n_rooms
        self.states = ['clean', 'dirty']
        self.world = np.random.choice(
            self.states, size=self.n_rooms, p=[1 - prob_dirty, prob_dirty])

    def __str__(self):
        return str(self.world)

    def __len__(self):
        return len(self.world)

    def is_dirty(self):
        return (self.world == 'dirty').any()


class Robot:
    def __init__(self, world):
        self.world = world
        self.world_len = len(world)
        self.location = np.random.choice(range(self.world_len))

    def move_left(self):
        self.location = max(0, self.location - 1)

    def move_right(self):
        self.location = min(self.location + 1, self.world_len)

    def is_dirty(self):
        return self.world[self.location] == 'dirty'

    def clean(self):
        self.world[self.location] = 'clean'


class Simulation:
    def __init__(self, world, robot):
        self.world = world
        self.robot = robot
                                         


if __name__ == '__main__':
    main()
