from main.computer import Computer
from main.human import Human

computer = Computer()
human = Human()
first_player = 'X'
turn = 1
def human_computer():
    computer.play_game()
    
def human_human():
    print('\n\nWelcome to Tic Tac Toe for two humans!')
    human.print_board(initial=True)
    human.play(first_player, turn)

def main():
    computer.welcome_message()
    if computer.choose_opponent():
        human_computer()
    else:
        human_human()
    


if __name__ == '__main__':
    main()