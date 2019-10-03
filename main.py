from main.computer import Computer

computer = Computer()
def human_computer():
    computer.play_game()
def human_human():
    pass

def main():
    computer.welcome_message()
    if computer.choose_opponent():
        human_computer()
    else:
        human_human()
    


if __name__ == '__main__':
    main()