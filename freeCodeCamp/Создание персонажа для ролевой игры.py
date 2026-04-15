full_dot = '●'
empty_dot = '○'
def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return 'The character name should be a string'
    if not len(name):
        return 'The character should have a name'
    if len(name) > 10:
        return 'The character name is too long'
    if ' ' in name:
        return 'The character name should not contain spaces'
    stats = [strength, intelligence, charisma]
    
    if not all(isinstance(stat, int) for stat in stats):
        return 'All stats should be integers'
    if any(stat < 1 for stat in stats):
        return 'All stats should be no less than 1'
    if any(stat > 4 for stat in stats):
        return 'All stats should be no more than 4'
    if sum(stats) != 7:
        return 'The character should start with 7 points'
    strength_dots = full_dot * strength + empty_dot * (10 - strength)
    intelligence_dots = full_dot * intelligence + empty_dot * (10 - intelligence)
    charisma_dots = full_dot * charisma + empty_dot * (10 - charisma)
    return f"{name}\nSTR {strength_dots}\nINT {intelligence_dots}\nCHA {charisma_dots}"

name = input('Введите ваше имя: ')
str1 = int(input('Введите вашу силу: '))
int1 = int(input('Введите ваш интеллект: '))
cha1 = int(input('Введите вашу харизму: '))
print(create_character(name, str1, int1, cha1))
