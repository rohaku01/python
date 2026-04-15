# 1. Создание словаря test_settings с несколькими значениями
test_settings = {
    'theme': 'light',
    'language': 'english',
    'notifications': 'enabled'
}

# 2-5. Определение функции add_setting
def add_setting(settings_dict, key_value_tuple):
    key, value = key_value_tuple
    key = key.lower()
    value = value.lower() if isinstance(value, str) else value
    
    if key in settings_dict:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    
    settings_dict[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

# 9-12. Определение функции update_setting
def update_setting(settings_dict, key_value_tuple):
    key, value = key_value_tuple
    key = key.lower()
    value = value.lower() if isinstance(value, str) else value
    
    if key in settings_dict:
        settings_dict[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

# 16-18. Определение функции delete_setting
def delete_setting(settings_dict, key):
    key = key.lower()
    
    if key in settings_dict:
        del settings_dict[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"

# 22-27. Определение функции view_settings
def view_settings(settings_dict):
    if len(settings_dict) == 0:
        return "No settings available."
    else:
        result = "Current User Settings:\n"
        for key, value in settings_dict.items():
            result += f"{key.capitalize()}: {value}\n"
        return result

# Примеры использования и тестирование
print("=== Тестирование add_setting ===")
test1 = {'theme': 'light'}
print(add_setting(test1, ('THEME', 'dark')))  # Setting 'theme' already exists!
print(add_setting(test1, ('volume', 'high')))  # Setting 'volume' added with value 'high' successfully!
print(test1)  # {'theme': 'light', 'volume': 'high'}

print("\n=== Тестирование update_setting ===")
test2 = {'theme': 'light'}
print(update_setting(test2, ('theme', 'dark')))  # Setting 'theme' updated to 'dark' successfully!
print(update_setting(test2, ('volume', 'high')))  # Setting 'volume' does not exist!
print(test2)  # {'theme': 'dark'}

print("\n=== Тестирование delete_setting ===")
test3 = {'theme': 'light', 'volume': 'high'}
print(delete_setting(test3, 'theme'))  # Setting 'theme' deleted successfully!
print(delete_setting(test3, 'language'))  # Setting not found!
print(test3)  # {'volume': 'high'}

print("\n=== Тестирование view_settings ===")
test4 = {}
print(view_settings(test4))  # No settings available.

test5 = {'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}
print(view_settings(test5))
# Current User Settings:
# Theme: dark
# Notifications: enabled
# Volume: high