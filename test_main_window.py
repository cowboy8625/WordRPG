""" test script """

from time import sleep

from WordRGP import gui


def tests(pause=2):
    """ Cycle through multiple tests of screen composition and drawing """

    gui.tests.empty()
    sleep(pause)

    gui.tests.fill()
    sleep(pause)

    gui.tests.logo()
    sleep(pause)

    gui.tests.splash()
    sleep(pause)

    gui.tests.title()
    sleep(pause)

    gui.tests.menu()
    sleep(pause)

    # test random words with pause
    for _ in range(3):
        gui.tests.random_words()
        sleep(pause)

    # test udpating screen as fast as possible
    for _ in range(30):
        gui.tests.random_words()


def main():
    # always start by setting up the terminal
    gui.main.setup_terminal()

    tests()



if __name__ == '__main__':
    while True:
        main()
