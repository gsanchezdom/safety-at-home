import dumb_menu

options = ["[1]Option 1", "[2]Option 2", "[3]Option 3","[q]quit"]

index = dumb_menu.get_menu_choice(options)

print(f"You selected option {index + 1}: {options[index]}")