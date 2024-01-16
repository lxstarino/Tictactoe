import random 
import os

class bcolors:
    CEND      = '\33[0m'
    CBOLD     = '\33[1m'
    CITALIC   = '\33[3m'
    CURL      = '\33[4m'
    CBLINK    = '\33[5m'
    CBLINK2   = '\33[6m'
    CSELECTED = '\33[7m'
    CBLACK  = '\33[30m'
    CRED    = '\33[31m'
    CGREEN  = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE   = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE  = '\33[36m'
    CWHITE  = '\33[37m'
    CBLACKBG  = '\33[40m'
    CREDBG    = '\33[41m'
    CGREENBG  = '\33[42m'
    CYELLOWBG = '\33[43m'
    CBLUEBG   = '\33[44m'
    CVIOLETBG = '\33[45m'
    CBEIGEBG  = '\33[46m'
    CWHITEBG  = '\33[47m'
    CGREY    = '\33[90m'
    CRED2    = '\33[91m'
    CGREEN2  = '\33[92m'
    CYELLOW2 = '\33[93m'
    CBLUE2   = '\33[94m'
    CVIOLET2 = '\33[95m'
    CBEIGE2  = '\33[96m'
    CWHITE2  = '\33[97m'
    CGREYBG    = '\33[100m'
    CREDBG2    = '\33[101m'
    CGREENBG2  = '\33[102m'
    CYELLOWBG2 = '\33[103m'
    CBLUEBG2   = '\33[104m'
    CVIOLETBG2 = '\33[105m'
    CBEIGEBG2  = '\33[106m'
    CWHITEBG2  = '\33[107m' 

grid = [" ", " ", " ",  
         " ", " ", " ",  
         " ", " ", " "] 


def game_menu(content = bcolors.CBOLD + bcolors.CBLUE + "Welcome to TicTacToe!" + bcolors.CEND + bcolors.CBLUE + f"\nEnter !Help to get further information.\n\n{os.getcwd()}: " + bcolors.CEND): 
    menuinp = input(content)

    os.system("cls")
    if(menuinp.lower() == "!help"):
        game_menu(bcolors.CBOLD + bcolors.CBLUE + "- Help Menu -" + bcolors.CEND + bcolors.CBLUE + f"\n!Help - Shows the Help Menu\n!Start - Starts the game.\n!Credits - Shows the Credits\n!Exit - Exits the game\n\n{os.getcwd()}: " + bcolors.CEND)
    elif(menuinp.lower() == "!start"):
        start_game()
    elif(menuinp.lower() == "!credits"):
        game_menu(bcolors.CBLUE + f"This shitty tictactoe game was coded by lxst\nEnter !Help to get further information.\n\n{os.getcwd()}: " + bcolors.CEND)
    elif(menuinp.lower() == "!exit"):
        print(bcolors.CBLUE + "Have a good day!"  + bcolors.CEND)
        exit(1)
    else:
        game_menu(bcolors.CRED + f"Unknown Command!\nEnter !Help to get further information.\n\n{os.getcwd()}: "  + bcolors.CEND)

def start_game():
    beginner = random.randint(1, 2)
    if(beginner == 1):
        print_results()
        return get_user_input() 
    else: 
        return get_pc_input()

def restart_game():
    print(bcolors.CBLUE + "Do you want to play another round? (Y/N): " + bcolors.CEND)
    inp = input()
    if(inp == "" or inp.lower() == "yes" or inp.lower() == "y"):
        for i in range(len(grid)):
            if(grid[i] == "x" or grid[i] == "o"):
                grid[i] = " "
        os.system("cls")
        return start_game()
    else:
        os.system("cls")
        print(bcolors.CBLUE + "Have a good day!"  + bcolors.CEND)
        exit(1)

def get_user_input(): 
    inp = input(bcolors.CBLUE + "Enter a number in range of 1-9: " + bcolors.CEND) 

    try: 
        inp = int(inp) 
    except:  
        print(bcolors.CRED + "Provide a number!" + bcolors.CEND) 
        return get_user_input() 

    if(int(inp) not in range(1, 10)): 
        print(bcolors.CRED + "Enter a number in range of 1-9!" + bcolors.CEND) 
        return get_user_input() 

    if(grid[int(inp - 1)] == "x" or grid[int(inp - 1)] == "o"): 
        print(bcolors.CRED + "This grid is already taken!" + bcolors.CEND) 
        return get_user_input() 

    grid[int(inp - 1)] = "x"    
    get_pc_input() 


def get_pc_input(): 
    pc = random.randint(1, 9) 

    if grid[pc - 1] == " ": 
        grid[pc - 1] = "o" 
        get_results()
    else: 
        if(" " in grid):
            return get_pc_input() 
        else:  
            get_results()

def get_results(): 
    print_results()
    results = verify_results() 
    if(results == True): 
        print(bcolors.CGREEN + "You won!" + bcolors.CEND) 
        return restart_game()
    elif(results == False):
        print(bcolors.CRED2 + "You lost!" + bcolors.CEND)
        return restart_game()
    elif(results == "Tie"):
        print(bcolors.CGREY + "Tie! No one won this round." + bcolors.CEND)
        return restart_game()
    get_user_input() 

def verify_results(): 
    if(grid[0] == "x" and grid[0] == grid[1] and grid[1] == grid[2]  
    or grid[3] == "x" and grid[3] == grid[4] and grid[4] == grid[5] 
    or grid[6] == "x" and grid[6] == grid[7] and grid[7] == grid[8] 
    or grid[0] == "x" and grid[0] == grid[3] and grid[3] == grid[6]
    or grid[1] == "x" and grid[1] == grid[4] and grid[4] == grid[7]
    or grid[2] == "x" and grid[2] == grid[5] and grid[5] == grid[8]
    or grid[0] == "x" and grid[0] == grid[4] and grid[4] == grid[8]
    or grid[2] == "x" and grid[2] == grid[4] and grid[4] == grid[6]): 
        return True 

    if(grid[0] == "o" and grid[0] == grid[1] and grid[1] == grid[2]  
    or grid[3] == "o" and grid[3] == grid[4] and grid[4] == grid[5] 
    or grid[6] == "o" and grid[6] == grid[7] and grid[7] == grid[8]
    or grid[0] == "o" and grid[0] == grid[3] and grid[3] == grid[6]
    or grid[1] == "o" and grid[1] == grid[4] and grid[4] == grid[7]
    or grid[2] == "o" and grid[2] == grid[5] and grid[5] == grid[8]
    or grid[0] == "o" and grid[0] == grid[4] and grid[4] == grid[8]
    or grid[2] == "o" and grid[2] == grid[4] and grid[4] == grid[6]):
        return False

    if not " " in grid:
        return "Tie"

def print_results():
    os.system('cls')
    print(bcolors.CGREYBG + "-------------" + bcolors.CEND)
    print(bcolors.CGREYBG + f"| {grid[0]} | {grid[1]} | {grid[2]} |" + bcolors.CEND)
    print(bcolors.CGREYBG + "-------------" + bcolors.CEND) 
    print(bcolors.CGREYBG + f"| {grid[3]} | {grid[4]} | {grid[5]} |" + bcolors.CEND) 
    print(bcolors.CGREYBG + "-------------" + bcolors.CEND)
    print(bcolors.CGREYBG + f"| {grid[6]} | {grid[7]} | {grid[8]} |" + bcolors.CEND) 
    print(bcolors.CGREYBG + "-------------" + bcolors.CEND)

game_menu()
 

 

 

 

 

 

 