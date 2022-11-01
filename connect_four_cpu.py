import random
from utility_function import Player,save_board,make_dict_reader
cpu = Player('CPU','O','plebe')
master = Player('The Master','X','master')
def condition_eval(list1,conditions,player):
    big_list = []
    if player.symbol==master.symbol:
        symbol1 = cpu.symbol
    else:
        symbol1 = master.symbol
    for condition_list in conditions:
        small_list = []
        for condition in condition_list:
            x = condition[0]
            y = condition[1]
            try:
                if x<0:
                    raise Exception
                if list1[x][str(y)]==player.symbol:
                    #print(list1[x][str(y)])
                    small_list.append('y')
                elif list1[x][str(y)]==symbol1:
                    small_list = ['n','n','n']
                    break
                else:
                    small_list.append('n')
            except Exception as err:
                #print(err)
                small_list = ['n','n','n']
                break
        big_list.append(small_list)
    return big_list
def check_horizontals(list1,i,n,player):
    condition_list1 = []
    condition_list2 = []
    for r in range(1,4):
        condition_list1.append((i,n+r))
        condition_list2.append((i,n-r))
    conditions = [condition_list1,condition_list2]
    return condition_eval(list1,conditions,player)
def check_verticals(list1,i,n,player):
    condition_list1 = []
    for r in range(1,4):
        condition_list1.append((i-r,n))
    conditions = [condition_list1]
    return condition_eval(list1,conditions,player)
def check_diagonals(list1,i,n,player):
    condition_list1 = []
    condition_list2 = []
    condition_list3 = []
    condition_list4 = []
    for r in range(1,4):
        condition_list1.append((i+r,n+r))
        condition_list2.append((i+r,n-r))
        condition_list3.append((i-r,n+r))
        condition_list4.append((i-r,n-r))
    conditions = [condition_list1,condition_list2,condition_list3,condition_list4]
    return condition_eval(list1,conditions,player)
def connections(title,player):
    with open('./{}.csv'.format(title),'r') as board:
        list1 = make_dict_reader(board)
        bigger_list = []
        for i in range(0,6):
            for n in range(1,8):
                if list1[i][str(n)]==player.symbol:
                    bigger_list+=check_horizontals(list1,i,n,player)
                    bigger_list+=check_verticals(list1,i,n,player)
                    bigger_list+=check_diagonals(list1,i,n,player)
        return bigger_list
def score(bigger_list):
    score1 = 0
    for list in bigger_list:
        count1 = list.count('y')
        if count1==1:
            score1+=1
        elif count1==2:
            score1+=2.5
        elif count1==3:
            score1+=1000
        else:
            pass
    return score1
def score10(bigger_list1):
    score1 = 0
    for list in bigger_list1:
        count1 = list.count('y')
        if count1==1:
            score1+=1.25
        elif count1==2:
            score1+=500
        else:
            pass
    return score1
def test_move(num):
    save_board('cpu_test_board')
    check = cpu.make_move(num,title='cpu_test_board')
    if not check:
        return connections('board',cpu),connections('board',master)+[['y','y','n']]
    bigger_list = connections('cpu_test_board',cpu)
    bigger_list1 = connections('cpu_test_board',master)
    return bigger_list,bigger_list1
def choose_move(score_dict):
    i = 1
    n = 1
    number5 = [1]
    while True:
        if i+n > 7:
            break
        if score_dict[i]>score_dict[i+n]:
            number5 = [i]
            n+=1
        elif score_dict[i]<score_dict[i+n]:
            number5 = [i+n]
            i+=n
            n = 1
        else:
            number5+=[i+n]
            n+=1
    return number5
def evaluate_board():
    score_dict = {}
    score3 = score(connections('board',cpu))
    score4 = score10(connections('board',master))
    for i in range(1,8):
        bigger_list,bigger_list1 = test_move(i)
        score1 = score(bigger_list)
        score2 = score10(bigger_list1)
        score_dict[i] = score1 - score3 + (score4 - score2)
    return choose_move(score_dict)
def move():
    choices = evaluate_board()
    #print(choices)
    choice = random.choice(choices)
    print('')
    print(cpu.make_move(choice))






