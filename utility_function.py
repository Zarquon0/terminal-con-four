import csv
def rewrite_board(list1,title):
    with open('./ConnectFour/{}.csv'.format(title),'w') as board:
        writer = csv.DictWriter(board,fieldnames=['w1','1','w2','2','w3','3','w4','4','w5','5','w6','6','w7','7','w8']) 
        writer.writeheader()
        for row in list1:
            writer.writerow(row)
    with open('./ConnectFour/{}.csv'.format(title),'r') as board:
        next(board)
        return board.read()
def make_dict_reader(board):
    dict1 = csv.DictReader(board)
    list1 = []
    for row in dict1:
        list1.append(row)
    return list1
def save_board(title):
    with open('./ConnectFour/board.csv','r') as board:
        next(board)
        board1 = board.read()
        with open('./ConnectFour/{}.csv'.format(title),'w') as new_board:
            new_board.write(board1)
class Player():
    def __init__(self,name,symbol,level):
        self.name = name
        self.symbol = symbol
        self.level = level
    def make_move(self,location,func=rewrite_board,title='board'):
        location = str(location)
        with open('./ConnectFour/board.csv','r') as board:
            list1 = make_dict_reader(board)
            num = 5
            try:
                while True:
                    if list1[num][location]=='_':
                        list1[num][location] = self.symbol
                        break
                    elif num!=0:
                        num-=1
                    else:
                        if title=='board':
                            print('Column full. Make a different move.')
                        return None
            except KeyError as err:
                print(err,'Try again.')
                return None
        return func(list1,title) 
    def place(self,position,func=rewrite_board,title='board'):
        if self.level!='master':
            print('You dirty cheater! How dare you?! \nTry again.')
            return None
        else:
            try:
                position1 = tuple(position.split())
                with open('./ConnectFour/board.csv','r') as board:
                    list1 = make_dict_reader(board)
                    list1[int(position1[0])][position1[1]] = self.symbol
                return func(list1,title)
            except Exception as err:
                print(err,'\nTry again.')
                return None