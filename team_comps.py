from pprint import pprint
import champ_and_item


def valid_name(name):
    found = False
    for i in champ_and_item.champ_data:
        if name == i:
            found = True
    return bool(found)


def get_team_data():
    pprint(team_data)
    return team_data


def add_champ(champ_name):
    if valid_name(champ_name):
        user_team.append(champ_name)
        print(user_team)
    else:
        print("Champion %s is not valid, please enter a valid champion's name" % champ_name)
        print(user_team)


def delete_champ(champ_string):                            # -champion_name
    champ_name_length = len(champ_string) - 1              # length = len(champion_name)
    champ_name = champ_string[-champ_name_length:]

    if champ_name in user_team:
        user_team.remove(champ_name)  # remove("champion_name")
        print(user_team)
    else:
        print("Champion %s is not in the user champion list, please enter a valid champion's name" % champ_name)


tier_S = []
user_team = []

# TODO: use web scraper to pull the following data automatically
team_data = {
    'void_brawlers':
        ['khazix',
         'blitzcrank',
         'reksai',
         'vi',
         'akali',
         'chogath',
         'jinx',
         'kaisa']
    ,

    'imperial_knights':
        ['darius',
         'garen',
         'mordekaiser',
         'poppy',
         'katarina',
         'draven',
         'sejuani',
         'kayle',
         'swain']
}