from script import Screen

## TODO: Move gender into an appropriate class for a character.
##-- This sets the gender for the story --##

def set_gender(gender):
    global he_she, him_her, his_her
    if gender == 'male':

        he_she = 'he'
        him_her = 'him'
        his_her = 'his'
    
    elif gender == 'female':

        he_she = 'she'
        him_her = 'her'
        his_her = 'her'


##-- This is where the story will be told at --##

def intro_story(name):

    intro = f"\tThere was smoke coming from over the hill......  That was strange to {name} because it wasn't time for dinner and it was to hot to just have a\
 fire going. {name}'s mind started to race thinking maybe the Bandits have come back?  No, no {he_she} gave them a good beating last time. It was to far for\
 {him_her} to run due to the large deer on {his_her} back.  {he_she.capitalize()} reasured {him_her}self that other people in the village would keep {his_her}\
 village safe. But when {name} finally made it over the hill {he_she} didn't believe {his_her} eyes........."
    
    Screen.display(intro)
    #Screen.type_to_screen(intro)
