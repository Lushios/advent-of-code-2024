with open("input.txt") as file:
    data = file.read().splitlines()

ylen = 103
xlen = 101


class Robot:
    def __init__(self, x, y, velocity_x, velocity_y):
        self.x = x
        self.y = y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    def move(self, times=1):
        for _ in range(times):
            if self.x + self.velocity_x < 0:
                self.x = xlen - (-self.velocity_x - self.x)
            elif self.x + self.velocity_x >= xlen:
                self.x = self.velocity_x - (xlen - self.x)
            else:
                self.x += self.velocity_x

            if self.y + self.velocity_y < 0:
                self.y = ylen - (-self.velocity_y - self.y)
            elif self.y + self.velocity_y >= ylen:
                self.y = self.velocity_y - (ylen - self.y)
            else:
                self.y += self.velocity_y


robots = []
for line in data:
    p, v = line.split(' ')
    px, py = p[2:].split(',')
    vx, vy = v[2:].split(',')
    robots.append(Robot(int(px), int(py), int(vx), int(vy)))


def find_a_straight_line(robot_coordinates):
    for robotx, roboty in robot_coordinates:
        vertical_line = True
        for i in range(10):
            if (robotx, roboty + i) not in robot_coordinates:
                vertical_line = False
                break
        if vertical_line:
            return True
    return False



positions = set()
# i = 0
# while True:
for i in range(10404):
    for robot in robots:
        robot.move()
    robot_coordinates = [(robot.x, robot.y) for robot in robots]
    print(i)
    if find_a_straight_line(robot_coordinates):
        print(i, 'found')
        with open(f'output{i}.txt', 'w') as file:
            for y in range(ylen):
                for x in range(xlen):
                    if any(robot.x == x and robot.y == y for robot in robots):
                        file.write('#')
                    else:
                        file.write('.')
                file.write('\n')
    # positions_hash = hash(frozenset([(robot.x, robot.y, robot.velocity_x, robot.velocity_y) for robot in robots])) # the positions loop in 10403 turns
    # print(i)
    # if positions_hash in positions:
    #     break
    # positions.add(positions_hash)
    # i += 1

