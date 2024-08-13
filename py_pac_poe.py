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
        return state['turn'] 
    else:
        state['turn'] = 'X'
        return state['turn']

    
def check_win(move):
    board_spaces_length = len(list(state['board'].items()))
    board_spaces = list(state['board'].items())

    for space in board_spaces:
        move_in_board_space_item = space[0]
        # print(type((list(move_in_board_space_item))[0]))
        if move == move_in_board_space_item:

            # * the work for all the way up and all the way up and all the way down
            print(f"move: {move}")
            print(f"move value: {state['board'][move]}")
            count = 0
            # if count  == 0:
            letter = (list(move_in_board_space_item))[0]
            num = str(int((list(move_in_board_space_item))[1]) + 1)
            next_space = letter + num
            print(f"next space down: {next_space}")
            result = state['board'].get(next_space)
            print(f"next space value: {result}")
            if state['board'][move] == result:
                print("match")
                count += 1
                num = str(int((list(move_in_board_space_item))[1]) + 2)
                next_space = letter + num
                print(f"next space down: {next_space}")
                result = state['board'].get(next_space)
                print(f"next space value: {result}")
                if state['board'][move] == result:
                    count += 1
                    print(count)
                    print("you win!")
            else:
                print("no match")
                letter = (list(move_in_board_space_item))[0]
                num = str(int((list(move_in_board_space_item))[1]) - 1)
                next_space = letter + num
                print(f"next space up: {next_space}")
                result = state['board'].get(next_space)
                print(f"next space value: {result}")
                if state['board'][move] == result:
                    print("match")
                    num = str(int((list(move_in_board_space_item))[1]) - 2)
                    next_space = letter + num
                    print(f"next space up: {next_space}")
                    result = state['board'].get(next_space)
                    print(f"next space value: {result}")
                    if state['board'][move] == result:
                        count += 1
                        print(count)
                        print("you win!")
                else:
                    print("no match")
        # else:
        #     print("")

def get_move():
    letters_and_nums = ['a', 'b', 'c', 1, 2, 3]
    move = input(f"Player {state['turn']}'s Move (example B2):")
    if len(list(move)) != 2 or list(move)[0] not in letters_and_nums or int(list(move)[1]) not in letters_and_nums or state['board'][move] != None:
        print("Bogus move! Try again... not the required length")
        return 
    else:
        state['board'][move] = state['turn']
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
