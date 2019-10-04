from .helpers import Helper, TIE

helper = Helper()

# Tic-Tac-Toe
# Plays the game of tic-tac-toe against a human opponent

# global constants
X = "X"
O = "O"


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


    def play_first(self):
        """Determine if player or computer goes first."""
        go_first = helper.query_user("Do you require the first move? (y/n): ")
        try:
            if go_first == "y":
                print("\nHuman takes the first move X")
                human = X
                computer = O
            else:
                print("\nComputer takes the first move X")
                computer = X
                human = O
            return computer, human
        except KeyboardInterrupt:
            print("Goodbye!")
            exit()




    def computer_move(self, board, computer, human):
        """Make computer move."""
        # make a copy to work with since function will be changing list
        board = board[:]
        # the best positions to have, in order
        BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

        print("I shall take square number", end=" ")

        # if computer can win, take that move
        for move in helper.legal_moves(board):
            board[move] = computer
            if helper.winner(board) == computer:
                print(move)
                return move
            # done checking this move, undo it
            board[move] = " "

        # if human can win, block that move
        for move in helper.legal_moves(board):
            board[move] = human
            if helper.winner(board) == human:
                print(move)
                return move
            # done checkin this move, undo it
            board[move] =" "

        # since no one can win on next move, pick best open square
        for move in BEST_MOVES:
            if move in helper.legal_moves(board):
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
        board = helper.new_board()
        helper.display_board(board)

        while not helper.winner(board):
            if turn == human:
                move = helper.human_move(board, human)
                board[move] = human
            else:
                move = self.computer_move(board, computer, human)
                board[move] = computer
            helper.display_board(board)
            turn = self.next_turn(turn)

        the_winner = helper.winner(board)
        self.congrat_winner(the_winner, computer, human)
