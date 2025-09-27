import time
from turtle import Screen
from Day23_player import Player
from Day23_car_manager import CarManager
from Day23_scoreboard import Scoreboard
player = Player()
car_manager = CarManager()
screen = Screen()
screen.listen()
screen.onkey(player.move, "Up")
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.cars:
        if player.distance(car) < 20:
            print("Game Over")
            game_is_on = False
            scoreboard = Scoreboard("Game Over")
    if player.ycor() > 280:
        game_is_on = False
        scoreboard = Scoreboard("You Win")
screen.exitonclick()