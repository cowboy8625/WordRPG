import sys, traceback

import WordRPG
from WordRPG.gui.screen import Screen



if __name__ == "__main__":
    try:
        WordRPG.main.run(start=WordRPG.const.SETTINGS['start_state'])
    except Exception as err:
        print(f'Exception Error:{err}')
        print('Stack at time of error:')
        traceback.print_exc(file=sys.stdout)

        # If there was an exception, keep the console window open so we can see
        # the exception error and stack trace
        while True:
            pass
    finally:
        # If we've successfully exited the main loop, clear the terminal window
        # and exit the
        Screen.clear()
        sys.exit()
            