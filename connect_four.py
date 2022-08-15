from utility_function import save_board,make_dict_reader,Player,rewrite_board
from connect_four_cpu import move,connections

def setup_board(title):
    with open('./ConnectFour/reserve_board.csv','r') as rboard:
        list1 = make_dict_reader(rboard)
        b = rewrite_board(list1,title)
        return b
def trigger_victory(player3):
    print(player3.name + ' wins!')
    save = input('Save game? (y/n)\n')
    if save=='y':
        title = input('Title?\n')
        save_board(title)
    return True
def check_victory(player3):
    con = connections('board',player3)
    for list in con:
        if list.count('y')==3:
            trigger_victory(player3)
            return 'victory'
    return None
print('Welcome to Terminal Connect Four\n')
player1 = input('Player 1 name? \n')
if player1:
    master = Player(player1,'X','master')
else:
    master = Player('Player 1','X','master')
print(setup_board('board'))
switch10 = True
player2 = input('Player 2 name?\n')
switch10 = True
if player2:
    player = Player(player2,'O','plebe')
else:
    player = Player('CPU','O','plebe')
    switch10 = False
while True:
    if switch10:
        while True:
            move1 = input('{}\'s move:\n'.format(player.name))
            if move1 == 'place':
                player.place(move1)
            output = player.make_move(move1)
            if output==None:
                continue
            else:
                print(output)
            break
    else: 
        print('CPU move:')
        move()
    v = check_victory(player)
    if v:
        break
    while True:
        move2 = input('{}\'s move:\n'.format(master.name))
        if move2=='place':
            print('')
            output = master.place(input('Placement?\n'))
        else:
            output = master.make_move(move2)
        if output==None:
            continue
        else:
            print('')
            print(output)
        break
    v = check_victory(master)
    if v:
        break
