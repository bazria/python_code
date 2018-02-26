#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# Votre client vous propose de développer un software pour faire fonctionner un ascenseur. Le hardware de cet ascenseur possède 2 commandes : goUp() et goDown().  Ecrire dans le langage de votre choix le software permettant de faire fonctionner les ascenseurs équipés de ce hardware. 

# tbd use wait 1 second, add sort or sort reverse to find next stop according to direction


def put_information(current_floor, way, floors_to_serve):
    pass


def serve_next_floor(current_floor, floors_to_serve, lift_direction):
    pass


def run_lift(lowest_floor, highest_floor, floors_to_serve=[]):
    """
    tbd
    """
    print()
    print('Hello, entering lift operating mode ...')
    print('lowest_floor:', lowest_floor)
    print('highest_floor:', highest_floor)
    print('At each stop, enter floors to serve separated by commas and/or STOP, and terminate entry by Enter')
    print()
    current_floor = 0
    is_operating = True
    while is_operating:
        floors_to_serve = sorted(list(set(floors_to_serve)))
        print('floors_to_serve:', floors_to_serve)
        floors_to_serve.pop()
# if lift_is_going_up, next_floor_to_serve = 
# else next_floor_to_serve = 


if __name__ == '__main__':
    lowest_floor    = 0
    highest_floor   = 4
    floors_to_serve = [-1, 5, 0, 4, 2, 3, 0, 1, -9, 10, 2, 3, 4]
    run_lift(lowest_floor    = lowest_floor,
             highest_floor   = highest_floor,
             floors_to_serve = floors_to_serve,
             )
