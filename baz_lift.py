#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# EXERCISE
# Votre client vous propose de développer un software pour faire fonctionner un ascenseur.  Le hardware de cet
# ascenseur possède 2 commandes : goUp() et goDown().  Ecrire dans le langage de votre choix le software permettant
# de faire fonctionner les ascenseurs équipés de ce hardware.

# ANSWER
# Hypothèses :
# - goUp() (respectivement goDown() ) déclenche sur l'ascenseur :
#   - la fermeture des portes,
#   - la montée (respectivement descente) d'autant d'étages que d'invocations successives,
#   - l'arrêt à l'étage atteint,
#   - l'ouverture des portes.
# - pas de prise en compte des aspects temps réel,
# - pas de retour de l'ascenseur (dont position réelle de la cabine), donc pas de gestion des incidents,


def put_information(current_floor, lowest_floor, highest_floor, floors_to_serve, mode, way, command):
    """
    Display lift information for monitoring and testing.
    """
    print()
    if command == 'start':
        print('Hello.  Lift starting.')
    elif command == 'stop':
        print('Goodbye.  Lift stopped.')
    print('Mode           :', mode)
    print('Current floor  :', current_floor)
    print('Lowest floor   :', lowest_floor)
    print('Highest floor  :', highest_floor)
    print('Floors to serve:', floors_to_serve)
    print('Way            :', way)
    print()


def updated_floors_to_serve(floors_to_serve, lowest_floor, highest_floor):
    user_input = input('Enter STOP or floors to serve separated by space key, e.g.: 0 4. Terminate by Enter: ')
    user_input_split = user_input.split()
    if 'STOP' in user_input_split:
        new_floors_to_serve = ['STOP']
    else:
        try:
            old_floors_to_serve_int = [int(x) for x in floors_to_serve]
        except Exception:
            old_floors_to_serve_int = []
        old_floors_to_serve_in_range = [x for x in old_floors_to_serve_int if (lowest_floor <= x <= highest_floor)]
        try:
            new_floors_to_serve_int = [int(x) for x in user_input_split]
        except Exception:
            new_floors_to_serve_int = []
        new_floors_to_serve_in_range = [x for x in new_floors_to_serve_int if (lowest_floor <= x <= highest_floor)]
        new_floors_to_serve = sorted(list(set(old_floors_to_serve_in_range + new_floors_to_serve_in_range)))
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


def serve_next_floor(current_floor, lowest_floor, highest_floor, floors_to_serve, mode, way):
    if 'STOP' in floors_to_serve:
        move_lift(current_floor, target_floor=0)
        current_floor = 0
        floors_to_serve = []
        way = None
        command = 'stop'
        put_information(current_floor=current_floor,
                        lowest_floor=lowest_floor,
                        highest_floor=highest_floor,
                        floors_to_serve=floors_to_serve,
                        mode=mode,
                        way=way,
                        command=command,
                        )
    else:
        command = None
        floors_to_serve = [x for x in floors_to_serve if isinstance(x, int)]
        floors_to_serve = sorted(list(set(floors_to_serve)))
        put_information(current_floor=current_floor,
                        lowest_floor=lowest_floor,
                        highest_floor=highest_floor,
                        floors_to_serve=floors_to_serve,
                        mode=mode,
                        way=way,
                        command=command,
                        )
    return current_floor, floors_to_serve, way, command
# if lift_is_going_up, next_floor_to_serve = 
# else next_floor_to_serve = 


def run_lift(current_floor, lowest_floor, highest_floor, floors_to_serve, mode, way, command):
    """
    Operate the lift with provided settings.
    """
    put_information(current_floor=current_floor,
                    lowest_floor=lowest_floor,
                    highest_floor=highest_floor,
                    floors_to_serve=floors_to_serve,
                    mode=mode,
                    way=way,
                    command=command,
                    )
    while (mode == 'operation' or mode == 'simulation') and command != 'stop':
        floors_to_serve = updated_floors_to_serve(floors_to_serve, lowest_floor, highest_floor)
        current_floor, floors_to_serve, way, command =\
            serve_next_floor(current_floor, lowest_floor, highest_floor, floors_to_serve, mode, way)


if __name__ == '__main__':
    # when called directly, run simulation mode
    mode = 'simulation'
    current_floor = 0
    lowest_floor = -4
    highest_floor = 9
    way = None
    # run test with initial floors to serve empty
    floors_to_serve = []
    run_lift(current_floor=current_floor,
             lowest_floor=lowest_floor,
             highest_floor=highest_floor,
             floors_to_serve=floors_to_serve,
             mode=mode,
             way=way,
             command='start',
             )
    # run test with initial floors to serve
    floors_to_serve = [-1, 5, 0, 4, 2, 3, 0, 1, -9, 10, 2, 3, 4]
    run_lift(current_floor=current_floor,
             lowest_floor=lowest_floor,
             highest_floor=highest_floor,
             floors_to_serve=floors_to_serve,
             mode=mode,
             way=way,
             command='start',
             )
#TODO delete
print('OK, Dude')
