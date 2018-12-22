from time import sleep

import gui



if __name__ == '__main__':
    # testing stuff

    # always start by setting up the terminal
    gui.main.setup_terminal()

    gui.tests.empty()
    sleep(2)
    gui.tests.fill()
    sleep(2)
    gui.tests.splash()
    sleep(2)
    gui.tests.title()
    sleep(2)
    gui.tests.menu()
    sleep(2)

    for _ in range(3):
        gui.tests.random_words()
        sleep(1)

    sleep(3)