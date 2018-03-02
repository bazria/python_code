#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# EXERCISE
# Votre client vous propose de développer un software pour faire fonctionner un ascenseur. Le hardware de cet ascenseur possède 2 commandes : goUp() et goDown().  Ecrire dans le langage de votre choix le software permettant de faire fonctionner les ascenseurs équipés de ce hardware. 

# ANSWER
# Hypothèses :
# - goUp() (respectivement goDown() ) déclenche sur l'ascenseur :
#   - la fermeture des portes,
#   - la montée (respectivement descente) d'autant d'étages que d'invocations successives,
#   - l'arrêt à l'étage atteint,
#   - l'ouverture des portes.
# - pas de prise en compte des aspects temps réel ,
# - pas de retour de l'ascenseur (dont position réelle de la cabine), donc pas de gestion des incidents,


def put_information(current_floor, lowest_floor, highest_floor, floors_to_serve, mode, way, command=None):
    """
    Display lift information for monitoring and testing.
    """
    print()
    if command == 'start':
        print('Hello.  Lift starting in mode:', mode)
    elif command == 'stop':
        print('Goodbye.  Lift stopping in mode:', mode)
    print('Current floor                  :', current_floor)
    print('Lowest floor                   :', lowest_floor)
    print('Highest floor                  :', highest_floor)
    print('Floors to serve                :', floors_to_serve)
    print('Way                            :', way)
    print()


def updated_floors_to_serve(floors_to_serve):
    user_input = input('Enter STOP or floors to serve separated by space key. Terminate by Enter: ')
    if 'STOP' in user_input:
        new_floors_to_serve = ['STOP']
    else:
        new_floors_to_serve = [int(x) for x in user_input.split()]
    new_floors_to_serve = sorted(list(set(floors_to_serve + new_floors_to_serve)))
    return new_floors_to_serve


def move_lift(current_floor, target_floor):
    if target_floor > current_floor:
        for floor in range(target_floor - current_floor):
            goUp()
# tbd use wait 1 second, add sort or sort reverse to find next stop according to direction
    elif target_floor < current_floor:
        for floor in range(current_floor - target_floor):
            goDown()
# tbd use wait 1 second, add sort or sort reverse to find next stop according to direction
    else:
# tbd
        pass


def serve_next_floor(current_floor, floors_to_serve, way, lowest_floor, highest_floor, mode):
    if 'STOP' in floors_to_serve:
        mode =  'stop'
        move_lift(current_floor, target_floor=0)
    else:
        floors_to_serve = [x for x in floors_to_serve if isinstance(x, int)]
        floors_to_serve = sorted(list(set(floors_to_serve)))
        put_information(current_floor=current_floor,
                         lowest_floor=lowest_floor,
                         highest_floor=highest_floor,
                         floors_to_serve=floors_to_serve,
                         mode=mode,
                         way=way,
                         )
        return current_floor, floors_to_serve, way
# if lift_is_going_up, next_floor_to_serve = 
# else next_floor_to_serve = 


def run_lift(current_floor, lowest_floor, highest_floor, floors_to_serve, mode, way, command):
    """
    tbd
    """
    lowest_floor    = lowest_floor
    highest_floor   = highest_floor
    floors_to_serve = floors_to_serve
    mode            = mode
    current_floor   = 0
    way             = 'upwards'
    put_information(current_floor=current_floor,
                     lowest_floor=lowest_floor,
                     highest_floor=highest_floor,
                     floors_to_serve=floors_to_serve,
                     mode=mode,
                     way=way,
                     )
    while mode == 'operation' or mode == 'simulation':
        current_floor, floors_to_serve, way = serve_next_floor(current_floor, floors_to_serve, way, lowest_floor, highest_floor, mode)
        floors_to_serve = updated_floors_to_serve(floors_to_serve)


if __name__ == '__main__':
# when called directly, run simulation mode
    mode            = 'simulation'
    current_floor = 0
    lowest_floor    = 0
    highest_floor   = 4
    way = 'upwards'
# run simple test with initial list of floors
    floors_to_serve = [-1, 5, 0, 4]
    run_lift(current_floor=current_floor,
             lowest_floor    = lowest_floor,
             highest_floor   = highest_floor,
             floors_to_serve = floors_to_serve,
             mode            = mode,
             way=way,
             command='start',
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
