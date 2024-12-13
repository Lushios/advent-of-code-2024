with open("input.txt") as file:
    data = file.read()


class Game:
    def __init__(self, buttonA, buttonB, prize):
        self.buttonA = buttonA
        self.buttonB = buttonB
        self.prize = prize
        self.solutions = []

    # im fucking sure this will not work in part 2, but I'm writing this, and it's already 23:30
    def find_solutions(self):
        for a in range(0, 101):
            for b in range(0, 101):
                if (self.buttonA[0] * a + self.buttonB[0] * b) == self.prize[0] and (self.buttonA[1] * a + self.buttonB[1] * b) == self.prize[1]:
                    self.solutions.append((a, b))

    def get_cheapest_solution(self):
        if not self.solutions:
            return 0

        solution_prices = [a * 3 + b for a, b in self.solutions]
        return min(solution_prices)



blocks = data.split('\n\n')

games = []

for block in blocks:
    separated_block = block.split('\n')
    buttonA = separated_block[0][10:]
    buttonAx, buttonAy = buttonA.split(', ')
    buttonAx = int(buttonAx[2:])
    buttonAy = int(buttonAy[2:])

    buttonB = separated_block[1][10:]
    buttonBx, buttonBy = buttonB.split(', ')
    buttonBx = int(buttonBx[2:])
    buttonBy = int(buttonBy[2:])

    prize = separated_block[2][7:]
    prizex, prizey = prize.split(', ')
    prizex = int(prizex[2:])
    prizey = int(prizey[2:])

    games.append(Game((buttonAx, buttonAy), (buttonBx, buttonBy), (prizex, prizey)))


result = 0
for game in games:
    game.find_solutions()
    result += game.get_cheapest_solution()

print(result)


