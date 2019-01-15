import WordRPG



if __name__ == "__main__":
    try:
        WordRPG.main.run()
    except Exception as err:
        print(f'EXCEPTION ERROR!\n{err}')

        while True:
            pass
