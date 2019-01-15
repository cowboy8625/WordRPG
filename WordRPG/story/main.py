import textwrap


# TODO: Are there only 2 genders?
PRONOUNS = [
    'HE_SHE',
    'HIM_HER',
    'HIS_HER',
    'HIS_HERS',
    'HIMSELF_HERSELF',
]



def get_pronoun(pronoun, gender='MALE', sep='_'):
    """ Gets the correct gender pronoun
    
    Arguments:
        pronoun {str} -- HE_SHE pronoun that needs to be converted
    
    Keyword Arguments:
        gender {str} -- [description] (default: {'MALE'})
        sep {str} -- [description] (default: {'_'})
    
    Returns:
        str -- [description]
    """

    m, f = pronoun.split(sep)
    if gender == 'MALE':
        return m
    else:
        return f


def text_formatter(text, name='COWBOY', gender='MALE'):
    """[summary]
    
    Arguments:
        text {[type]} -- [description]
    
    Keyword Arguments:
        name {str} -- [description] (default: {'COWBOY'})
        gender {str} -- [description] (default: {'MALE'})
    
    TODO:
        Need to handle possesive form of name ending in 's'

    Returns:
        [type] -- [description]
    """

    _text = text.replace('[NAME]', name)
    
    for p in PRONOUNS:
        _text = _text.replace(f'[{p}]', get_pronoun(p, gender))
    
    return _text


def text_wrap(text, cols=80, rows=30, double_space=True):
    """ Wraps text to fit in contents

    Format long string into seperate lines that fit within a given column
    width.
        
    Arguments:
        text {[type]} -- [description]
    
    Keyword Arguments:
        cols {int} -- [description] (default: {80})
        rows {int} -- [description] (default: {30})
        double_space {bool} -- [description] (default: {True})

    TODO:
        Need to seperate into multiple lists that fit within given row height

    Returns:
        [type] -- [description]
    """

    lines = textwrap.wrap(text, width=cols)

    return lines


##------------------------------------------------------------------------------

test_text = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum.

Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium
doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore
veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam
voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia
consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque
porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur,
adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et
dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis
nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex
ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea
voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem
eum fugiat quo voluptas nulla pariatur?

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum.
'''

test_story = '''
THERE WAS SMOKE COMING FROM OVER THE HILL.

THAT WAS STRANGE TO [NAME] BECAUSE IT WASN'T TIME FOR DINNER AND IT WAS TO
HOT TO JUST HAVE A FIRE GOING. [NAME]'S MIND STARTED TO RACE THINKING MAYBE
THE BANDITS HAVE COME BACK?  NO, NO [HE_SHE] GAVE THEM A GOOD BEATING LAST
TIME. IT WAS TO FAR FOR [HIM_HER] TO RUN DUE TO THE LARGE DEER ON [HIS_HER]
BACK.  [HE_SHE] REASURED [HIMSELF_HERSELF] THAT OTHER PEOPLE IN THE VILLAGE
WOULD KEEP [HIS_HER] VILLAGE SAFE. BUT WHEN [NAME] FINALLY MADE IT OVER THE
HILL [HE_SHE] DIDN'T BELIEVE [HIS_HER] EYES...
'''

text = text_formatter(test_story, name='BOB', gender='MALE')
text = text_wrap(text, cols=20)
for line in text:
    print(line)