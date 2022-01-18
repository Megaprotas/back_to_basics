MAIN_MENU = "\nEnter:\n'a' to add game\n'l' to list games\n'f' to find games\n'q to quit'"
games = []


def add_game():
    game_title = input('Enter game title: ')
    studio = input('Enter the studio: ')
    game_year = int(input('Enter year of release: '))

    games.append({
        'game_title': game_title,
        'studio': studio,
        'game_year': game_year
    })


def list_games():
    for game in games:
        print_game_list(game)


def print_game_list(game):
    print(f"Title: {game['game_title']}")
    print(f"Title: {game['studio']}")
    print(f"Title: {game['game_year']}")


def find_game():
    search_title = input("Enter title: ")
    for game in games:
        if game['game_title'] == search_title:
            print(game)


user_choice = {
    'a': add_game,
    'l': list_games,
    'f': find_game
}


def choices():
    selection = input(MAIN_MENU)
    while selection != 'q':
        if selection in user_choice:
            selected_menu_function = user_choice[selection]
            selected_menu_function()

        # if selection == 'a':
        #     add_game()
        # elif selection == 'l':
        #     list_games()
        # elif selection == 'f':
        #     find_game()

        else:
            print("Can't recognize the choice")

        selection = input(MAIN_MENU)

choices()