# TicTacToe
- Application to play the TicTacToe game on the terminal

## Description
- This is a paper and pencil game for 2 players, X and O who take turns marking the spaces in a 3x3 grid.
- The game starts with one of the players and the game ends when one of the players has one whole row/ column/ diagonal filled with his/her respective character (‘O’ or ‘X’).
- The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.
- Players soon discover that the best play from both parties leads to a draw.

![Alt text](https://www.gameideasforkids.com/images/tictactoe.JPG "Optional Title")

## Features
- User can select whether to play with human or computer
- User can select the symbol they want to play with first
- User can select whether to play first or play last
- User can make a move
- Computer can also make a move automatically
- The application notifies of the winner, the draw or the loser

## Getting started
- Clone this repository by running `git clone https://github.com/mariamiah/TicTacToe-CLI.git`
- Navigate into the repository folder by running `cd Tic-TacToe-CLI`
- Set up a virtualenvironment `virtualenv venv -p python3`
- Activate the virtual environment `source venv/bin/activate` for unix based systems and `source venv\Scripts\activate` for windows
- Run `python main.py` to start the application

## Testing
- To run tests locally type `py.test` on the terminal
