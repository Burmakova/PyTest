class Gift(object):
    def __init__(self, length=0, width=0, height=0) -> None:
        self.width = width
        self.height = height
        self.length = length

    def wrapping_paper(self):
        sides = [
            self.width * self.length, self.height * self.length,
            self.width * self.height
        ]
        minimal = min(sides)
        return sum(sides) * 2 + minimal

    def wrapping_ribbon(self):
        sides = [self.width, self.height, self.length]
        sides.sort()
        return (sides[0] +
                sides[1]) * 2 + self.width * self.length * self.height
