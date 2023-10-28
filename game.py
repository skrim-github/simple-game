import os
import subprocess
import time
from random import *

player_health = int(100)
enemy_health = int(100)
menu_input = 0

def clear_terminal():   #clear terminal depending on what opperating system
    if os.name == 'nt':
        subprocess.call('cls', shell=True)
    else:
        subprocess.call('clear', shell=True)

clear_terminal()
print("Game\n-----\n1.Start\n2.Exit")
main_menu_input = int(input())  #get main menu input

def player_attack(player_health, enemy_health):    #player damaging enemy
    clear_terminal()
    random_number = randint(0,20)
    if enemy_health - random_number < 0:    #if enemy health is below 0 you won
        print("you won!")
    else:   #else damage enemy for random value between 0 - 20
        enemy_health = enemy_health - random_number
        print("damage dealt for " + str(random_number) + " remaining enemy health = " + str(enemy_health))
        time.sleep(3)
        enemy_turn(player_health, enemy_health)

def player_heal(player_health, enemy_health):
    clear_terminal()
    random_number = randint(0,20)
    if player_health + random_number > 100: #if health will be above 100 set it to 100
        player_health = 100
        print("healed to max health")
        time.sleep(3)
        enemy_turn(player_health, enemy_health)
    else:   #else heal for random value between 0-20
        player_health = player_health + random_number
        print("healed for " + random_number)
        time.sleep(3)
        enemy_turn(player_health, enemy_health)

def player_turn(player_health, enemy_health):
    clear_terminal()
    print("your turn")
    print("your health > " + str(player_health) + "             enemy health > " + str(enemy_health))
    print("------------------------------------------------")
    print("your turn")
    print("1. Attack\n2. Heal")

    menu_input = int(input())
    if menu_input == 1: #if input is 1 call player_attack
        player_attack(player_health, enemy_health)
    else:   #if input is 2 call player_heal
        player_heal(player_health, enemy_health)

def enemy_turn(player_health, enemy_health):
    clear_terminal()
    print("enemy turn")
    print("your health > " + str(player_health) + "             enemy health > " + str(enemy_health))
    print("------------------------------------------------")

    time.sleep(3)
    clear_terminal()
    random_number = randint(0,4)
    if random_number < 4:   #if number is below 4 attack player
        random_number = randint(0,20)
        if player_health - random_number < 0:   #if health drops below 0 lose
            print("you lost!")
        else:   #else attack player for random number between 0 - 20
            player_health = player_health - random_number
            print("enemy attacked you for " + str(random_number))
            time.sleep(3)
            player_turn(player_health, enemy_health)
    else:   #if number is 4 enemy heal
        random_number = randint(0,20)
        if enemy_health + random_number > 100:  #if enemy health goes above 100 set it to 100
            enemy_health = 100
            print("enemy healed to max health")
            time.sleep(3)
            player_turn(player_health, enemy_health)
        else:   #else heal for the random value
            enemy_health = enemy_health + random_number
            print("enemy healed for "+ str(random_number))
            time.sleep(3)
            player_turn(player_health, enemy_health)

if  main_menu_input == 1:   #if main menu input is 1 play game
    player_turn(player_health, enemy_health)
else:   #else exit
    exit()
