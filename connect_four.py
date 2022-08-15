from utility_function import save_board,make_dict_reader,Player,rewrite_board
from connect_four_cpu import move,connections

def setup_board(title):
    with open('./ConnectFour/reserve_board.csv','r') as rboard:
        list1 = make_dict_reader(rboard)
        b = rewrite_board(list1,title)
        return b
def trigger_victory(player2):
    print(player2.name + ' wins!')
    save = input('Save game? (y/n)\n')
    if save=='y':
        title = input('Title?\n')
        save_board(title)
    return True
def check_victory(player2):
    con = connections('board',player2)
    for list in con:
        if list.count('y')==3:
            trigger_victory(player2)
            return 'victory'
    return None
print('Welcome to Connect Four+\nTry to beat The Master... If you dare...')
player1 = input('Player 1 name? \n')
print(setup_board('board'))
switch10 = True
if player1:
    player = Player(player1,'O','plebe')
else:
    player = Player('CPU','O','plebe')
    switch10 = False
master = Player('The Master','X','master')
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
        move2 = input('The Master\'s move:\n')
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