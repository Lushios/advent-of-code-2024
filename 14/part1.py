from collections import Counter

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
        self.quadrant = None

    def _calculate_quadrant(self):
        if self.x == xlen // 2 or self.y == ylen // 2:
            self.quadrant = None
        if self.x < xlen // 2 and self.y < ylen // 2:
            self.quadrant = 1
        elif self.x > xlen // 2 and self.y < ylen // 2:
            self.quadrant = 2
        elif self.x < xlen // 2 and self.y > ylen // 2:
            self.quadrant = 3
        elif self.x > xlen // 2 and self.y > ylen // 2:
            self.quadrant = 4

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
        self._calculate_quadrant()


robots = []
for line in data:
    p, v = line.split(' ')
    px, py = p[2:].split(',')
    vx, vy = v[2:].split(',')
    robots.append(Robot(int(px), int(py), int(vx), int(vy)))

for robot in robots:
    robot.move(100)

cnt = Counter([robot.quadrant for robot in robots])
print(cnt[1] * cnt[2] * cnt[3] * cnt[4])
