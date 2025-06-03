import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Frog")
screen.listen()
list_of_car = []

player = Player()
scoreboard = Scoreboard()


screen.onkey(player.move, "Up")
# for _ in range(9):
#     car_manager = CarManager()
#
#     list_of_car.append(car_manager)
#     time.sleep(0.2)
#     screen.update()
i = 2
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    if i % 7 == 0:
        car_manager = CarManager()
        list_of_car.append(car_manager)

    for l in range(len(list_of_car)):
        list_of_car[l].drive()
        screen.update()

    # Deetect crash with car
        if list_of_car[l].head.distance(player) < 21:
            player.restart_position()
            game_is_on = False
            scoreboard.game_over()

        if player.ycor() >= 0:
            player.restart_position()
            scoreboard.level()
            list_of_car[l].add_speed()

    i += 1

    # Detect new level




    #     time.sleep(0.1)
    #     for _ in range(9):
    #         car_manager = CarManager()
    #         list_of_car.append(car_manager)
    #         time.sleep(1)
    #         screen.update()
    #         for i in range(len(list_of_car)):
    #             list_of_car[i].drive()
    #     screen.update()

    # for _ in range(9):
    #     car_manager = CarManager()
    #
    #     list_of_car.append(car_manager)
    # for i in range(len(list_of_car)):
    #     list_of_car[i].drive()
    # screen.update()
    # car_manager.drive()
    # Detect when turtle go all way


