
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
        
class standing_row:
    def __init__(self, player, M, W, L, GD, Points):
        self.player = player
        self.M = M
        self.W = W
        self.L = L
        self.GD = GD
        self.Points = Points

player_list = []
match_list = []
standings = []

# -----------------------------------------------
#                  INIT FUNCTIONS
# ----------------------------------------------- 

def init(player_list):
    match_init(player_list)
    table_init(player_list)

def match_init(player_list):
    mid = 0
    for home, away in itertools.combinations(player_list, 2):
        match_list.append(match(mid, home, away, None, None))
        mid += 1

def table_init(player_list):
    for player in player_list:
        standings.append(standing_row(player, 0, 0, 0, 0, 0))

# -----------------------------------------------
#                  UTILITY FUNCTIONS
# ----------------------------------------------- 

def prompt():
    print(">", end='')


def update_table(homeP, awayP, homeG, awayG):
    
    winner = homeP if homeG > awayG else awayP
    gd = abs(homeG - awayG)

    for r in standings:
        if(r.player == homeP or r.player == awayP):
            r.M += 1
            if(r.player == winner):
                r.W += 1
                r.GD += gd
                r.Points += 3
            else:
                r.L += 1
                r.GD -= gd
    
    standings.sort(key=lambda x: (x.Points, x.GD, x.W), reverse=True)

# ----------------------------------------------- 
#                  COMMANDS FUNCTIONS
# ----------------------------------------------- 

def help_command():
    print("Try any of the following commands:\n\n"
        "1) help: show commands details\n"
        "2) list: show all matches\n"
        "3) add: add result for given match\n"
        "4) stand: show standings\n"
    )

def boot_command():
    print("Welcome in tournamanager!\n")
    help_command()

def esc_command():
    exit(0)

def list_command():
    print("\tid\thome\t\tscore\t\taway\n")

    for m in match_list:
        if(m.goal_home != None):
            print(f"\t{m.mid}\t{m.player_home}\t\t{m.goal_home}-{m.goal_away}\t\t{m.player_away}")
        else:
            print(f"\t{m.mid}\t{m.player_home}\t\t-\t\t{m.player_away}")
    
    print("------------------------------------------------------------------")


def standings_command():
    print("\tplayer\tM\tW\tL\tGD\tPoints\n")

    for r in standings:
        print(f"\t{r.player}\t{r.M}\t{r.W}\t{r.L}\t{r.GD}\t{r.Points}")

    print("------------------------------------------------------------------")


def add_command():
    try:
        mid = int(input("Select match ID from match list (0 to {}): ".format(len(match_list) - 1)))
    
        if mid < 0 or mid >= len(match_list):
            print("Invalid match ID. Please select a valid ID.")
        else:
            if match_list[mid].goal_home != None:
                confirm = input("Match already added. Confirm to overwrite? (y/n): ")
                if confirm.lower()!= "y":
                    # todo: handle overwrite case with coherent insertion of data
                    return
            homeP = match_list[mid].player_home
            awayP = match_list[mid].player_away
            print(f"Match selected: {homeP} - {awayP}")
            homeG = int(input("Insert Home's goal> "))
            awayG = int(input("Insert Away's goal> "))
            match_list[mid].goal_home = homeG
            match_list[mid].goal_away = awayG
            update_table(homeP, awayP, homeG, awayG)
            print(f"Match added successfully")
            list_command()
            standings_command()

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
    elif cmd == "stand":
        standings_command()
    else:
        print("Command not found!\n")
        help_command()
        

