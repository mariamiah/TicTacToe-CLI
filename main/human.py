# Command-line Tic Tac Toe for two humans written in Python.

boxes = [ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ]
first_player = 'X'
turn = 1
winning_combos = [  [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                    [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6], ]

class Human:
    def print_board(self, initial=False):
        """ Print the game board. If this is the beginning of the game,
            print out 0-8 in the boxes to show players how to pick a
            box. Otherwise, update each box with X or 0 from boxes[].
        """
        print("""
                {} | {} | {} 
                -----------
                {} | {} | {}
                -----------
                {} | {} | {} """.format(*([x for x in range(0, 9)] if initial else boxes)))

    def take_turn(self, player, turn):
        """ Create a loop that keeps asking the current player for
            their input until a valid choice is made.
        """
        while True:
            try:
                box = input('Player %s, type a number from 0-8 to select a box: ' % player)
                box = int(box) # subtract 1 to sync with boxes[] index numbers
                if 0 <= box <= 8:
                    if boxes[box] == ' ': # initial value
                        boxes[box] = player # set to value of current player
                        break
                    else:
                        print('That box is already marked, try again.\n')
                        continue
                else:
                    print('That number is out of range, try again.\n')
                    continue

            except ValueError:
                # Not an integer
                print('That\'s not a valid number, try again.\n')
                continue
            except KeyboardInterrupt:
                print("Goodbye!")
                exit()

    def switch_player(self, turn):
        """ Switch the player based on how many moves have been made.
            X starts the game so if this turn # is even, it's 0's turn. 
        """
        current_player = '0' if turn % 2 == 0 else 'X'
        return current_player

    def check_for_win(self, player, turn):
        """ Check for a win (or a tie).
            If a player's score count reaches 3, return a win.
            If it doesn't, and this is already turn # 9, return a tie. If
            neither, return False so the game continues.
        """
        win = False
        tie = False
        if turn > 4: # need at least 5 moves before a win is possible
            for x in range(len(winning_combos)):
                score = 0
                for y in range(len(winning_combos[x])):
                    if boxes[winning_combos[x][y]] == player:
                        score += 1
                    if score == 3:
                        win = True

            if turn == 9:
                tie = True

        return win, tie

    def play(self, player, turn):
        """ Create a loop that keeps the game in play
            until it ends in a win or tie
        """
        while True:
            self.take_turn(player, turn)
            self.print_board()
            win, tie = self.check_for_win(player, turn)
            if win or tie:
                if win:
                    print('Game over. %s wins!\n' % player)
                else:
                    print('Game over. It\'s a tie.\n')
                break
            turn += 1
            player = self.switch_player(turn)

