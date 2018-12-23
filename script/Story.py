from script import Screen


class gender_struct:
    def __init__(self, gender):
        is_female = gender == "female"
        self.he_she = 'she' if is_female else 'he'
        self.him_her = 'her' if is_female else 'him'
        self.his_her = 'her' if is_female else 'his'


# This is where the intro story will be told
def intro_story(player):
    pronouns = gender_struct(player.gender)
    intro = f"\tThere was smoke coming from over the hill...... That was strange to {player.name} because it wasn't time " \
        f"for dinner and it was too hot to just have a fire going. {player.name}'s mind started to race thinking maybe the " \
        f"Bandits have come back? No, no {pronouns.he_she} gave them a good beating last time. It was too far for {pronouns.him_her} " \
        f"to run due to the large deer on {pronouns.his_her} back. {pronouns.he_she.capitalize()} reassured {pronouns.him_her}self that other " \
        f"people in the village would keep {pronouns.his_her} village safe. But when {player.name} finally made it over the " \
        f"hill {pronouns.he_she} didn't believe {pronouns.his_her} eyes........."
    
    Screen.display(intro)
