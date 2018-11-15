##- This will grab the changes from CHANGELOG.md and put them in a variable to
##- be used in the game for the changelog menu.
with open('CHANGELOG.md', 'r') as f:
    f_contents = f.read()
    print(f_contents)

