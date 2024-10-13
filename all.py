
import sys
import os
import itertools


class match:
    def __init__(self, mid, player_home, player_away, goal_home, goal_away):
        self.mid = mid
        self.player_home = player_home
        self.player_away = player_away
        self.goal_home = goal_home
        self.goal_away = goal_away
        
        
player_list = ['Pippo', 'Luca', 'Ciccio', 'Diego', 'Stef']
match_list = []

# -----------------------------------------------
#                  INIT FUNCTIONS
# ----------------------------------------------- 

def match_init(player_list):
    mid = 0
    for home, away in itertools.combinations(player_list, 2):
        match_list.append(match(mid, home, away, None, None))
        mid += 1

# -----------------------------------------------
#                  UTILITY FUNCTIONS
# ----------------------------------------------- 

def prompt():
    print(">", end='')

# ----------------------------------------------- 
#                  COMMANDS FUNCTIONS
# ----------------------------------------------- 

def help_command():
    print("Try any of the following commands:\n\n"
        "1) help: show commands details\n"
        "2) list: show all matches\n"
        "3) add: add result for given match\n"
    )

def boot_command():
    print("Welcome in fifatournament!\n")
    help_command()

def esc_command():
    exit(0)

def list_command():
    print("\tid\thome\t\tscore\t\taway\n")

    for m in match_list:
        print(f"\t{m.mid}\t{m.player_home}\t\t{m.goal_home}-{m.goal_away}\t{m.player_away}")


def add_command():
    mid = input("select match id from match list")

def add_command():
    try:
        mid = int(input("Select match ID from match list (0 to {}): ".format(len(match_list) - 1)))
    
        if mid < 0 or mid >= len(match_list):
            print("Invalid match ID. Please select a valid ID.")
        else:
            print(f"Match selected: {match_list[mid].player_home} - {match_list[mid].player_away}")
            homeG = int(input("Inser Home's goal> "))
            homeA = int(input("Inser Away's goal> "))
            match_list[mid].goal_home = homeG
            match_list[mid].goal_away = homeA
            # update_table()
            print(f"Match added successfully")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

def clear_command():
    if os.name == 'nt':  
        os.system('cls')
    else: 
        os.system('clear')

def read_command():
    prompt()
    cmd = input()

    if cmd in ("clear", "cls"):
        clear_command()
    elif cmd == "esc":
        esc_command()
    elif cmd == "help":
        help_command()
    elif cmd == "list":
        list_command()
    elif cmd == "add":
        add_command()
    else:
        print("Command not found!\n")
        help_command()
        

match_init(player_list)
