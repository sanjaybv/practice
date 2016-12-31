class Pos(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __repr__(self):
        return '{0} {1}'.format(self.row, self.col)

def get_boards(col, positions):
    if col >= 8:
        return positions
    boards = []
    for row in xrange(8):
        pos = Pos(row, col)
        for position in positions:
            board = [pos]
            board.extend(position)
            if is_valid(board):
                boards.append(board)

    return get_boards(col+1, boards)

def is_valid(board):
    for i in xrange(len(board)-1):
        for j in xrange(i+1, len(board)):
            pos1 = board[i]
            pos2 = board[j]

            if pos1.row == pos2.row or abs(pos1.row - pos2.row) == abs(pos1.col - pos2.col):
                return False

    return True

b = get_boards(0, [[]])
for x in b:
    print ' --------'
    for pos in x:
        print ''.join([' ']*pos.row), '*', pos.row
