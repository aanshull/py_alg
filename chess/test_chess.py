from chess_moves import get_position, get_knight_moves, get_piece_moves


def test_get_position():
    x,y = get_position('d2')
    print(x,y)
    assert y == 2
    assert x == 4


def test_invalid_piece():
    moves = get_piece_moves('king', 'h2')
    assert moves == 'Not implemented for king'


def test_knight_middle():
    x,y = get_position('c3')
    moves = get_knight_moves(x, y)
    expected = ['e4', 'e2', 'd5', 'd1', 'a2', 'a4', 'b5', 'b1']
    for i in range(8):
        assert expected[i] == moves[i]


def test_knight_corner():
    x,y = get_position('h1')
    moves = get_knight_moves(x, y)
    expected = ['f2', 'g3']
    for i in range(2):
        assert expected[i] == moves[i]


def test_rook_middle():
    moves = get_piece_moves('rook', 'e4')
    expected = ['a4', 'b4', 'c4', 'd4', 'e1', 'e2', 'e3', 'e5', 'e6', 'e7', 'e8', 'f4', 'g4', 'h4']
    for i in range(14):
        assert expected[i] == moves[i]


def test_rook_corner():
    moves = get_piece_moves('rook', 'h1')
    expected = ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8']
    for i in range(14):
        assert expected[i] == moves[i]


def test_queen_middle():
    moves = get_piece_moves('queen', 'e4')
    expected = ['a4', 'b4', 'c4', 'd4', 'e1', 'e2', 'e3', 'e5', 'e6', 'e7', 'e8', 'f4', 'g4', 'h4', 'a8', 'b1', 'b7', 'c2', 'c6', 'd3', 'd5', 'f3', 'f5', 'g2', 'g6', 'h1', 'h7']
    for i in range(27):
        assert expected[i] == moves[i]


def test_queen_corner():
    moves = get_piece_moves('queen', 'h1')
    expected = ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'a8', 'b7', 'c6', 'd5', 'e4', 'f3', 'g2']
    for i in range(21):
        assert expected[i] == moves[i]

