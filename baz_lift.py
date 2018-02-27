#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# Votre client vous propose de développer un software pour faire fonctionner un ascenseur. Le hardware de cet ascenseur possède 2 commandes : goUp() et goDown().  Ecrire dans le langage de votre choix le software permettant de faire fonctionner les ascenseurs équipés de ce hardware. 

# Hypothèses :
# 1. goUp() (respectivement goDown() ) déclenche sur l'ascenseur :
#   - la fermeture des portes,
#   - la montée (respectivement descente) d'autant d'étages que d'invocations successives,
#   - l'arrêt à l'étage atteint,
#   - l'ouverture des portes.

# tbd use wait 1 second, add sort or sort reverse to find next stop according to direction


def put_information(current_floor, way, floors_to_serve=[], mode='operation'):
    print('Lift stopped at floor:', current_floor, 'in mode:', mode, 'going:', way, 'serving floors:', floors_to_serve)


def put_information_start(lowest_floor, highest_floor, mode='operation'):
    print()
    print('Hello, lift entering operation mode ...')
    print('Lowest_floor: ', lowest_floor)
    print('Highest_floor:', highest_floor)
    print('At each stop, enter floors to serve separated by commas and/or STOP, and terminate entry by Enter.')
    print()


def put_information_stop(lowest_floor, highest_floor):
    print()
    print('Hello, lift exiting operation mode and returning to floor 0 ...')
    print()


def move_lift(current_floor, to_floor=0):
    pass


def serve_next_floor(current_floor, floors_to_serve, way, lowest_floor, highest_floor):
    if 'STOP' in floors_to_serve:
        mode =  'stop'
        go_to(current_floor, floor=0)
    else:
        floors_to_serve = [x for x in floors_to_serve if isinstance(x, int)]
        floors_to_serve = sorted(list(set(floors_to_serve)))
        put_information(current_floor  = current_floor,
                        way            = way,
                        floors_to_serve=floors_to_serve)
# if lift_is_going_up, next_floor_to_serve = 
# else next_floor_to_serve = 
#    isinstance (integer) or str


def run_lift(lowest_floor, highest_floor, floors_to_serve=[], mode='operation'):
    """
    tbd
    """
    lowest_floor    = lowest_floor
    highest_floor   = highest_floor
    floors_to_serve = floors_to_serve
    mode            = mode
    current_floor   = 0
    way             = 'upwards'
    put_information_start(lowest_floor, highest_floor)
    while mode == 'operation' or mode == 'simulation':
        current_floor, floors_to_serve, way = serve_next_floor(current_floor, floors_to_serve, way, lowest_floor, highest_floor)
        floors_to_serve = updated_floors_to_serve


if __name__ == '__main__':
    mode = 'simulation'
    lowest_floor    = 0
    highest_floor   = 4
    floors_to_serve = [-1, 5, 0, 4, 2, 3, 0, 1, -9, 10, 2, 3, 4]
    run_lift(lowest_floor    = lowest_floor,
             highest_floor   = highest_floor,
             floors_to_serve = floors_to_serve,
             mode            = mode,
             )
    floors_to_serve = [-1, 5, 0, 4, 2, 3, 0, 1, -9, 10, 'STOP', 2, 3, 4]
    run_lift(lowest_floor    = lowest_floor,
             highest_floor   = highest_floor,
             floors_to_serve = floors_to_serve,
             mode            = mode,
             )
