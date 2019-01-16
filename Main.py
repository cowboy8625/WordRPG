import sys, traceback

import WordRPG



if __name__ == "__main__":
    try:
        WordRPG.main.run()
    except Exception as err:
        print(f'Exception Error:{err}')
        print('Stack at time of error:')
        traceback.print_exc(file=sys.stdout)

        # keep console window open so we can see error text
        while True:
            pass
