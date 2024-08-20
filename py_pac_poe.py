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
    listed_element_in_move = list(move)
    letter = listed_element_in_move[0] 
    num = int(listed_element_in_move[1])
    center_space = state['board']['b2']
    coners = ['a1','c1', 'a3', 'c3']

    if move in coners:
        if state['board'][move] == center_space:
            if letter == 'a' and num == 1:
                if center_space == state['board']['c3']:
                    state['winner'] = True
            if letter == 'c' and num == 1:
                if center_space == state['board']['a3']:
                    state['winner'] = True
            if letter == 'a' and num == 3:
                if center_space == state['board']['c1']:
                    state['winner'] = True
            if letter == 'c' and num == 3:
                if center_space == state['board']['a1']:
                    state['winner'] = True

    # * diagnol from center win check
    if move == 'b2':
        if state['board']['a1'] == state['board'][move] and state['board']['c3'] == state['board'][move]:
            state['winner'] = True
        elif state['board']['c1'] == state['board'][move] and state['board']['a3'] == state['board'][move]:
            state['winner'] = True
    # * diagnol from center win check complete

    # * west and east space check
    if letter == "a":
        next_letter_right = "b"
        next_space_right = next_letter_right + str(num)
        if state['board'][move] == state['board'][next_space_right]:
            next_letter_right = "c"
            next_space_right = next_letter_right + str(num)
            if state['board'][move] == state['board'][next_space_right]:
                state['winner'] = True
                print(f"player {state['turn']} wins!")
    elif letter == "b":
        next_letter_right = "c"
        next_letter_left = "a"
        if state['board'][move] == state['board'][next_letter_right + str(num)] and state['board'][move] == state['board'][next_letter_left + str(num)]:
            state['winner'] = True
            print(f"player {state['turn']} wins!")
    else:
        next_letter_left = "b"
        next_space_left = next_letter_left + str(num)
        if state['board'][move] == state['board'][next_space_left]:
            next_letter_left = "a"
            next_space_left = next_letter_left + str(num)
            if state['board'][move] == state['board'][next_space_left]:
                state['winner'] = True
                print(f"player {state['turn']} wins!")
    # * west and east space check complete

    # * north and south check
    next_move_north = letter + str(num - 1)
    next_move_south = letter + str(num + 1)
    if next_move_north in state['board'] and next_move_south in state['board']:
        if state['board'][move] == (state['board'][next_move_north]) and state['board'][move] == state['board'][next_move_south]:
            state['winner'] = True
            print(f"Player {state['turn']} wins!")
    if next_move_north in state['board']: 
        if state['board'][move] == (state['board'][next_move_north]):
            next_move_north = letter + str(num - 2)
            if next_move_north in state['board']:
                if state['board'][move] == (state['board'][next_move_north]):
                    state['winner'] = True
                    print(f"Player {state['turn']} wins!")
    if next_move_south in state['board']: 
        if state['board'][move] == (state['board'][next_move_south]):
            next_move_south = letter + str(num + 2)
            if next_move_south in state['board']:
                if state['board'][move] == (state['board'][next_move_south]):
                    state['winner'] = True
                    print(f"Player {state['turn']} wins!")
    # * north and south check complete

def get_move():
    move = input(f"Player {state['turn']}'s Move (example B2):")
    if move == "quit":
        state['winner'] = True
    elif move in state['board'] and state['board'][move] == None:
        state['board'][move] = state['turn']
        check_win(move)
        change_turns()
    else:
        print("Bogus move! Try again... not the required length")
        return

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

    while state['winner'] != True:
        if all(space is not None for space in state['board'].values()) and state['winner'] == False:
            print("It's a tie")
            break
        print_board()
        get_move()
    print_board()

init_game()