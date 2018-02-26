#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

def go
def next_floor_to_serve(current_floor, floors_to_serve, lift_direction):
    pass

def run_lift(lowest_floor, highest_floor, floors_to_serve=[]):
    """
    tbd
    """
    print('lowest_floor:', lowest_floor)
    print('highest_floor:', highest_floor)
    while floors_to_serve:
        print('floors_to_serve:', floors_to_serve)
        floors_to_serve = list(set(floors_to_serve))
        floors_to_serve.pop()
# if lift_is_going_up, next_floor_to_serve = 
# else next_floor_to_serve = 


if __name__ == '__main__':
    lowest_floor = 0
    highest_floor= 4
    floors_to_serve = [-1, 5, 0, 4, 2, 3, 0, 1, -9, 10, 2, 3, 4]
    run_lift(lowest_floor  = lowest_floor,
             highest_floor = highest_floor,
             floors_to_serve = floors_to_serve,
             )
