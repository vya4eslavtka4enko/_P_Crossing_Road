from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()

    def create_player(self):
        self.shape('turtle')
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        new_pos_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_pos_y)
        print('hello')

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False