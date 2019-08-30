def get_position(pos):
    return (ord(pos[0])-96, int(pos[1]))


def get_knight_moves(x,y):
    moves = [(x+2, y+1), (x+2, y-1),
             (x+1, y+2), (x+1, y-2),
             (x-2, y-1), (x-2, y+1),
             (x-1, y+2), (x-1, y-2)]
    return [chr(96+mov[0])+str(mov[1]) for mov in moves if (mov[0]>0 and mov[0]<9) and (mov[1]>0 and mov[1]<9)]


def get_rook_moves(x, y):
    movs = [((x, y+i),(x, y-i),(x-i,y),(x+i,y)) for i in range(1,9)]
    moves = [chr(96+m[0])+str(m[1]) for mov in movs for m in mov if 0<m[0]<9 and 0<m[1]<9]
    return sorted(moves)


def bishop_moves(x,y):
    movs = [((x+i, y+i), (x+i, y-i), (x-i, y+i), (x-i, y-i)) for i in range(1,9)]
    moves = [chr(96+m[0])+str(m[1]) for mov in movs for m in mov if 0<m[0]<9 and 0<m[1]<9]
    return sorted(moves)


def get_queen_moves(x,y):
    return get_rook_moves(x,y) + bishop_moves(x,y)


def get_piece_moves(inp, pos):
    pieces = {'queen': get_queen_moves, 'rook': get_rook_moves, 'knight': get_knight_moves}
    if inp in pieces:
        x,y = get_position(pos)
        return pieces[inp](x, y)
    else:
        return "Not implemented for " + inp


def main():
    inp = input("Enter piece: ")
    pos = input("Enter position: ")
    print(get_piece_moves(inp, pos))


if __name__ == '__main__':
    main()

