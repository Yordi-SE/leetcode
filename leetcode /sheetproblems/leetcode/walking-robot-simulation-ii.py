class Robot:

    def __init__(self, width: int, height: int):
        self.width = width - 1
        self.height = height - 1
        self.direction = "East"
        self.curr_step = 0
        self.curr_pos = [0,0]

    def step(self, num: int) -> None:
        self.curr_step += num
        reminder = self.curr_step % ((2 * self.width) + (2 * self.height))
        if reminder == 0:
            self.direction = "South"
            self.curr_pos = [0,0]
        elif reminder <= self.width and reminder > 0:
            self.direction = "East"
            self.curr_pos = [reminder,0]
        elif reminder <= (self.width + self.height) and reminder > self.width:
            self.direction = "North"
            self.curr_pos = [self.width, (reminder - self.width)]
        elif reminder <= ((2 * self.width) + self.height) and reminder > (self.width + self.height):
            self.direction = "West"
            self.curr_pos = [self.width -(reminder - (self.width + self.height)),self.height]
        elif reminder <= ((2 * self.width) + (2 * self.height)) and reminder > ((2 * self.width) + self.height):
            self.direction = "South"
            self.curr_pos = [0,self.height - (reminder - ((2 * self.width) + (self.height)))]
    def getPos(self) -> List[int]:
        return self.curr_pos

    def getDir(self) -> str:
        return self.direction

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()