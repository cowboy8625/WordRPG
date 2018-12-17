import os


# Downloads modules
def setup():
    if os.path.isfile("Worldmap.db"):
        return
    else:
        if os.name == 'nt':
            os.system("pip install colorama > NUL")
            os.system("pip install Pandas > NUL")
        else:
            os.system("pip install colorama > /dev/null")
            os.system("pip install Pandas > /dev/null")
    
# Clears Print Screen
def clear():
    if os.name == 'nt':
        _ = os.system('cls')

    else:
        _ = os.system('clear')


# This maybe fast then retyping input a bunch
def pause():
    input("Press Enter To Continue:> ")