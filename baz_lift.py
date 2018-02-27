#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# EXERCISE
# Votre client vous propose de développer un software pour faire fonctionner un ascenseur. Le hardware de cet ascenseur possède 2 commandes : goUp() et goDown().  Ecrire dans le langage de votre choix le software permettant de faire fonctionner les ascenseurs équipés de ce hardware. 

# ANSWER
# Hypothèses :
# 1. goUp() (respectivement goDown() ) déclenche sur l'ascenseur :
#   - la fermeture des portes,
#   - la montée (respectivement descente) d'autant d'étages que d'invocations successives,
#   - l'arrêt à l'étage atteint,
#   - l'ouverture des portes.

# tbd use wait 1 second, add sort or sort reverse to find next stop according to direction


def put_information(current_floor, way, floors_to_serve, mode):
    print('Lift stopped at floor:', current_floor, 'in mode:', mode, 'going:', way, 'serving floors:', floors_to_serve)


def put_information_start(lowest_floor, highest_floor, mode):
    print()
    print('Hello...')
    print('Lift starting in mode:', mode)
    print('Lowest_floor         :', lowest_floor)
    print('Highest_floor        :', highest_floor)
    print()


def put_information_stop(lowest_floor, highest_floor, mode):
    print()
    print('Hello, lift exiting operation mode and returning to floor 0 ...')
    print()


def updated_floors_to_serve(floors_to_serve):
#    print('At each stop, enter floors to serve separated by commas and/or STOP, and terminate entry by Enter.')
    return floors_to_serve


def move_lift(current_floor, target_floor):
    if target_floor > current_floor:
        for floor in range(target_floor - current_floor):
            goUp()
    elif target_floor < current_floor:
        for floor in range(target_floor - current_floor):
            goDown()
    else:
        pass


def serve_next_floor(current_floor, floors_to_serve, way, lowest_floor, highest_floor, mode):
    if 'STOP' in floors_to_serve:
        mode =  'stop'
        move_lift(current_floor, target_floor=0)
    else:
        floors_to_serve = [x for x in floors_to_serve if isinstance(x, int)]
        floors_to_serve = sorted(list(set(floors_to_serve)))
        put_information(current_floor  =current_floor,
                        way            =way,
                        floors_to_serve=floors_to_serve,
                        mode           =mode)
        return current_floor, floors_to_serve, way
# if lift_is_going_up, next_floor_to_serve = 
# else next_floor_to_serve = 


def run_lift(lowest_floor, highest_floor, floors_to_serve, mode):
    """
    tbd
    """
    lowest_floor    = lowest_floor
    highest_floor   = highest_floor
    floors_to_serve = floors_to_serve
    mode            = mode
    current_floor   = 0
    way             = 'upwards'
    put_information_start(lowest_floor, highest_floor, mode)
    while mode == 'operation' or mode == 'simulation':
        current_floor, floors_to_serve, way = serve_next_floor(current_floor, floors_to_serve, way, lowest_floor, highest_floor, mode)
        floors_to_serve = updated_floors_to_serve(floors_to_serve)


if __name__ == '__main__':
# when called directly, run simulation mode
    mode            = 'simulation'
    lowest_floor    = 0
    highest_floor   = 4
# run simple test with initial list of floors
    floors_to_serve = [-1, 5, 0, 4]
    run_lift(lowest_floor    = lowest_floor,
             highest_floor   = highest_floor,
             floors_to_serve = floors_to_serve,
             mode            = mode,
             )
## run test with initial list of floors
#    floors_to_serve = [-1, 5, 0, 4, 2, 3, 0, 1, -9, 10, 2, 3, 4]
#    run_lift(lowest_floor    = lowest_floor,
#             highest_floor   = highest_floor,
#             floors_to_serve = floors_to_serve,
#             mode            = mode,
#             )
## run test with initial list of floors + STOP order
#    floors_to_serve = [-1, 5, 0, 4, 2, 3, 0, 1, -9, 10, 'STOP', 2, 3, 4]
#    run_lift(lowest_floor    = lowest_floor,
#             highest_floor   = highest_floor,
#             floors_to_serve = floors_to_serve,
#             mode            = mode,
#             )
