NUM_SQUARES = 9
EMPTY = " "
TIE = "TIE"

class Helper:
    def query_user(self, qtn):
        """Ask a yes or no question."""
        response = None
        try:
            while response not in ("y", "n"):
                response = input(qtn).lower()
            return response
        except KeyboardInterrupt:
            print("Goodbye!")
            exit()
        
    def get_input(self, question, min, max):
        """Ask for a number within a range."""
        response = None
        try:
            while response not in range(min, max):
                response = int(input(question))
            return response
        except KeyboardInterrupt:
            print("Goodbye!")
            exit()
    
    def new_board(self):
        """Create new game board."""
        board = []
        for square in range(NUM_SQUARES):
            board.append(EMPTY)
        return board


    def display_board(self, board):
        """Display game board on screen."""
        print("\n\t", board[0], "|", board[1], "|", board[2])
        print("\t", "---------")
        print("\t", board[3], "|", board[4], "|", board[5])
        print("\t", "---------")
        print("\t", board[6], "|", board[7], "|", board[8], "\n")
    

    def winner(self, board):
        """Determine the game winner."""
        WAYS_TO_WIN = ((0, 1, 2),
                    (3, 4, 5),
                    (6, 7, 8),
                    (0, 3, 6),
                    (1, 4, 7),
                    (2, 5, 8),
                    (0, 4, 8),
                    (2, 4, 6))

        for row in WAYS_TO_WIN:
            if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
                winner = board[row[0]]
                return winner

        if EMPTY not in board:
            return TIE

        return None
    
    def legal_moves(self, board):
        """Create list of legal moves."""
        moves = []
        for square in range(NUM_SQUARES):
            if board[square] == EMPTY:
                moves.append(square)
        return moves
    

    def human_move(self, board, human):
        """Get human move."""  
        legal = self.legal_moves(board)
        move = None
        while move not in legal:
            move = self.get_input("Where will you move? (0 - 8):", 0, NUM_SQUARES)
            if move not in legal:
                print("\nThat square is already occupied. Please select another.\n")
        print("Great move!...")
        return move