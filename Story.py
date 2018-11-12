import Screen

##-- Global Pronouns --##

he_she = ''
him_her = ''





##-- This sets the gender for the story --##

def set_gender(gender):
    global he_she, him_her
    if gender == 'male':

        he_she = 'he'
        him_her = 'him'
    
    elif gender == 'female':

        he_she = 'she'
        him_her = 'her'


##-- This is where the story will be told at --##

def intro_story(name):

    intro = f"\tThere was smoke coming from over the hill......  That was strange to {name} because it wasn't time for dinner and it was to hot to just have a\
 fire going. {name}'s mind started to race thinking maybe the Bandits have come back?  No, no he gave them a good beating last time. It was to far for\
 him to run do to the large deer on his back.  He reasured him self that other men in the village would keep he village safe. But when {name} finally made\
 it over the hill he didn't believe his eye........."
    
    
    Screen.display(intro)
