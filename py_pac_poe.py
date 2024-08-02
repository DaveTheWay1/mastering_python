state = {}
state['turn'] = 'X'
state['winner'] = False

def print_board():
    print(
    f'''
            A B C
    1) {state['board']['a1']} | {state['board']['b1']} | {state['board']['c1']}
        ---------------
    2) {state['board']['a2']} | {state['board']['b2']} | {state['board']['c2']}
        ---------------
    3) {state['board']['a3']} | {state['board']['b3']} | {state['board']['c3']}
    ''')

def change_turns():
    if state['turn'] == 'X':
        state['turn'] = 'Y'
        # print(f"turn:{state['turn']}")
        return state['turn'] 
    else:
        state['turn'] = 'X'
        # print(f"turn:{state['turn']}")
        return state['turn']
    
def check_win(move):
    count = 0
    board_spaces_length = len(list(state['board'].items()))
    board_spaces = list(state['board'].items())
    # print(board_spaces_length)
    # print(board_spaces)
    if '1' in move:
        for item in board_spaces:
            if move in item:
                print(f"move is here {item}")
                listed_move = list(item[0])
                listed_move[1] = str(int(listed_move[1]) + 1)
                below_space = "".join(listed_move)
                print(state['board'][move])
                print(state['board'][below_space])
                if state['board'][move] == state['board'][below_space]:
                    state['winner'] = True

                
                
                # num = int(num[0]) + 1
                # print(num)
                # # num = 
                # print(num)
                # num = str(num)
                # print(num)
                # print(f"num type: {type(num)}, num: {num}")
                # num = int(list(item[0][1])) + 1
                # num = str(num)
                # print(num)
        # print(board_spaces.index(move))
        # print(f"move: {state['board'][move]}")

        # print('first row')
        # # print(board_spaces)
        # for i in (board_spaces[3:6]):
        #     print(list(i[0]))
        #     if list(i[0][0]) == list(move[0]):
        #         print("letter matches")
        # print(" ")
    elif '2' in move:
        print('second row')
    else:
        print('third row')
    # for i in range(len(list(state['board'].items()))):
    #     print(board_spaces[i])


def get_move():
    letters_and_nums = ['a', 'b', 'c', 1, 2, 3]
    move = input(f"Player {state['turn']}'s Move (example B2):")
    # print(move)
    # print(list(move))
    if len(list(move)) != 2 or list(move)[0] not in letters_and_nums or int(list(move)[1]) not in letters_and_nums or state['board'][move] != None:
        print("Bogus move! Try again... not the required length")
        return 
    else:
        state['board'][move] = state['turn']
        # print(f"{state['board'][move]}")
        # print(state['board'])
        check_win(move)
        change_turns()

# The following works
def init_game():
    state['board'] = {
    'a1': None , 'b1': None, 'c1': None,
    'a2': None , 'b2': None, 'c2': None,
    'a3': None , 'b3': None, 'c3': None
}
    print(
    '''
    ----------------------
    Let's play Py-Pac-Poe!
    ----------------------
    ''')

init_game()
while state['winner'] != True:
    print_board()
    get_move()
print('You Win!')

# def get_winner():
#     state['winner']

# get_winner()
