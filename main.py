import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
player.create_player()
cars = CarManager()
screen.listen()
screen.onkey(player.go_up, 'Up')
scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    cars.car_move()
    cars.create_car()
    screen.update()
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.update_scoreboard()
        scoreboard.increase_level()



screen.exitonclick()



