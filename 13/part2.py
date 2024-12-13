with open("input.txt") as file:
    data = file.read()


class Game:
    def __init__(self, buttonA, buttonB, prize):
        self.buttonA = buttonA
        self.buttonB = buttonB
        self.prize = prize
        self.solution = None

    def find_solution(self):
        a = float(self.buttonA[0])
        b = float(self.buttonB[0])
        c = float(self.prize[0])
        d = float(self.buttonA[1])
        e = float(self.buttonB[1])
        m = float(self.prize[1])

        buttonB_presses = (c*d - a*m) / (b*d - a*e)
        buttonA_presses = (c - b*buttonB_presses) / a

        if buttonA_presses.is_integer() and buttonB_presses.is_integer():
            self.solution = (buttonA_presses, buttonB_presses)

    def get_solution_price(self):
        if not self.solution:
            return 0
        return 3 * self.solution[0] + self.solution[1]




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
    prizex = 10000000000000 + int(prizex[2:])
    prizey = 10000000000000 + int(prizey[2:])

    games.append(Game((buttonAx, buttonAy), (buttonBx, buttonBy), (prizex, prizey)))


result = 0
for game in games:
    # print(game.buttonA, game.buttonB, game.prize)
    game.find_solution()
    result += game.get_solution_price()

print(result)


