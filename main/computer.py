# Tic-Tac-Toe
# Plays the game of tic-tac-toe against a human opponent

# global constants
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

class Computer:
    def welcome_message(self):
        """Display game instructions."""
        print("#################################################################################")  
        print(
        """
        Welcome to Tic-Tac-Toe. This game shall be played between the human and computer or
        The human vs another human.  

        You will make your move known by entering a number, 0 - 8.  The number 
        will correspond to the board position as illustrated:

                        0 | 1 | 2
                        ---------
                        3 | 4 | 5
                        ---------
                        6 | 7 | 8
        """
        )
        print("##################################################################################")


    def choose_opponent(self):
        """
        Allows human to choose to play with either computer or another human
        """
        while True:
            try:
                response = input("Select C to play with Computer or H to play with human(C/H)  :")
                if response.lower() not in ('c', 'h'):
                    print("Not an appropriate choice.")
                else:
                    if response.lower() == "c":
                        return True
                    else:
                        return False
                    break
            except KeyboardInterrupt:
                print("Goodbye!")
                exit()


    def query_user(self, qtn):
        """Ask a yes or no question."""
        response = None
        while response not in ("y", "n"):
            response = input(qtn).lower()
        return response


    def get_input(self, question, min, max):
        """Ask for a number within a range."""
        response = None
        while response not in range(min, max):
            response = int(input(question))
        return response


    def play_first(self):
        """Determine if player or computer goes first."""
        go_first = self.query_user("Do you require the first move? (y/n): ")
        if go_first == "y":
            print("\nHuman takes the first move X")
            human = X
            computer = O
        else:
            print("\nComputer takes the first move X")
            computer = X
            human = O
        return computer, human


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


    def legal_moves(self, board):
        """Create list of legal moves."""
        moves = []
        for square in range(NUM_SQUARES):
            if board[square] == EMPTY:
                moves.append(square)
        return moves


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


    def computer_move(self, board, computer, human):
        """Make computer move."""
        # make a copy to work with since function will be changing list
        board = board[:]
        # the best positions to have, in order
        BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

        print("I shall take square number", end=" ")

        # if computer can win, take that move
        for move in self.legal_moves(board):
            board[move] = computer
            if self.winner(board) == computer:
                print(move)
                return move
            # done checking this move, undo it
            board[move] = EMPTY

        # if human can win, block that move
        for move in self.legal_moves(board):
            board[move] = human
            if self.winner(board) == human:
                print(move)
                return move
            # done checkin this move, undo it
            board[move] = EMPTY

        # since no one can win on next move, pick best open square
        for move in BEST_MOVES:
            if move in self.legal_moves(board):
                print(move)
                return move


    def next_turn(self, turn):
        """Switch turns."""
        if turn == X:
            return O
        else:
            return X


    def congrat_winner(self, the_winner, computer, human):
        """Congratulate the winner."""
        if the_winner != TIE:
            print(the_winner, "won!\n")
        else:
            print("It's a tie!\n")

        if the_winner == computer:
            print("Computer Wins!!!")

        elif the_winner == human:
            print("Human wins!!!")

        elif the_winner == TIE:
            print("Its a Draw!!!")


    def play_game(self):  
        computer, human = self.play_first()
        turn = X
        board = self.new_board()
        self.display_board(board)

        while not self.winner(board):
            if turn == human:
                move = self.human_move(board, human)
                board[move] = human
            else:
                move = self.computer_move(board, computer, human)
                board[move] = computer
            self.display_board(board)
            turn = self.next_turn(turn)

        the_winner = self.winner(board)
        self.congrat_winner(the_winner, computer, human)
