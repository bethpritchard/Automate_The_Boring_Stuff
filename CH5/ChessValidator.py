def isValidChessBoard(chessboard):
    letters = ['a','b','c','d','e','f','g','h']
    numbers = list(range(1,9))
    piece_names = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
    colours = ['w', 'b']
    pieces_count = {'b': 0, 'w': 0}
    pawn_count = {'b': 0, 'w': 0}
    board_coord = []
    pieces = []

    # create valid board coordinates
    for letter in letters:
        for number in numbers:
            board_coord.append(str(number) + letter)

    # create valid pieces
    for piece in piece_names:
        for colour in colours:
            pieces.append(colour + piece)

    # count number of pieces and number of pawns
    for piece in chessboard.values():
        if piece == 'wpawn':
            pawn_count['w'] += 1
        elif piece == 'wpawn':
            pawn_count['b'] += 1

    for piece in chessboard.values():
        if piece != "":
            if piece[0] in colours and piece[1:] in piece_names:
                if piece[0] == 'w':
                    pieces_count['w'] += 1
                elif piece[0] == 'b':
                    pieces_count['b'] += 1
            else:
                print(f'{piece}: invalid piece')
                return False

    if pawn_count['w'] > 8 or pawn_count['b'] > 8:
        print("too many pawns")
        return False
    elif pieces_count['w'] > 16 or pieces_count['b'] > 16:
        print("too many pieces")
        return False
    else:
        for coord_element in chessboard.keys():
            if coord_element not in board_coord:
                print(f"{coord_element}: invalid coordinate")
                return False
            else:
                return True


board = {'1a': 'bking','2a': 'bqueen','3a': 'brook','4a': 'brook',
'5a': 'bknight','6a': 'bknight','7a':'bbishop','8a': 'bbishop',
'1b': 'bpawn','2b': 'bpawn','3b': 'bpawn','4b':'bpawn',
'5b': 'bpawn','6b': 'bpawn','7b': 'bpawn','8b': 'bpawn',
'1c': 'wking','2c': 'wqueen','3c': 'wrook','4c': 'wrook',
'5c': 'wbishop','6c': 'wbishop','7c': 'wknight','8c':'wknight',
'1e': 'wpawn','2e': 'wpawn','3e': 'wpawn','4e': 'wpawn',
'5e': 'wpawn','6e': 'wpawn','7e': 'wpawn','8e': 'wpawn',
'1f': '','2f': '','3f': '','4f': '','5f': '','6f': '','7f': '','8f': '',
'1g': '','2g': '','3g': '','4g': '','5g': '','6g': '','7g': '','8g': '',
'1h': '','2h': '','3h': '','4h': '','5h': '','6h': '','7h': '','8h': '',}


print(isValidChessBoard(board))